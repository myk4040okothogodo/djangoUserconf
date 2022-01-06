# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User accounts serializer
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'is_active','is_staff', 'is_superuser', 'date_joined',)
        read_only_fields = ('username', 'auth_token', 'date_joined',)


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
