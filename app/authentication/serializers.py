from rest_framework import serializers 


class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)


class CredentialSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)


class DeleteUserSerializers(serializers.Serializer):
    password = serializers.CharField(write_only=True)