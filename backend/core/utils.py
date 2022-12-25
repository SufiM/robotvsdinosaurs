#import serializers
from rest_framework import serializers


def validate_position(value):
    if value[0] < 0 or value[0] > 9 or value[1] < 0 or value[1] > 9:
        raise serializers.ValidationError('Position is out of range')


def set_object_validator(value):
    if value[0] < 0 or value[0] > 11 or value[1] < 0 or value[1] > 11:
        raise serializers.ValidationError('Position is out of range')

    if value[2] < 0 or value[2] > 3:
        raise serializers.ValidationError('Direction is out of range')

    if value[3] < 0 or value[3] > 3:
        raise serializers.ValidationError('Speed is out of range')

    if value[4] < 0 or value[4] > 3:
        raise serializers.ValidationError('Size is out of range')