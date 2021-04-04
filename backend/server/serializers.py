from rest_framework import serializers
from .models import Variable, BooleanValue, StringValue


class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variable
        fields = ('name', 'type')


class BooleanValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooleanValue
        fields = ('value', 'name', 'type')


class StringValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = StringValue
        fields = ('value', 'name', 'type')
