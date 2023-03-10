from rest_framework import serializers


class DefenseSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ip = serializers.CharField()
    attack_date = serializers.DateTimeField(read_only=True) 
    route = serializers.CharField()