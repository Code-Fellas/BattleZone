from rest_framework import serializers

from users import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        exclude = ('updated_on',)