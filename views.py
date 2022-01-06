# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import list_route
from rest_framework.views import APIView

from .models import User
from .permissions import IsSuperuserOrIsSelf
from .serializers import UserSerializer, PasswordSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    list:
    Return a list of all the existing users.

    read:
    Return the given user.

    me:
    Return authenticated user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrIsSelf,)


    @list_route(methods=['put'], serializer_class=PasswordSerializer)
    def set_password(self, request):
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']}, 
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'password set'}, status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
