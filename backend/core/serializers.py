from rest_framework import serializers
from .models import Game, Board, Robot, Dinosaur
from django.core import validators


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'game', 'cells']
        read_only_fields = ('id', 'game', 'cells')

class StartGameSerializer(serializers.Serializer):
    player = serializers.CharField(max_length=100)
    
class OutputGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['id']

class OutputGetGameSerializer(serializers.ModelSerializer):
    board = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'player', 'status', 'board']

    def get_board(self, obj):
        board = Board.objects.get(game=obj)
        return BoardSerializer(board).data

class OutputSetRobotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Robot
        fields = ['id', 'game', 'x_position', 'y_position']

class SetRobotSerializer(serializers.ModelSerializer):

    robot_position = serializers.ListField(
        child=serializers.IntegerField(),
        validators=[validators.MinLengthValidator(2), validators.MaxLengthValidator(2)]
    )

    class Meta:
        model = Robot
        fields = ['id', 'robot_position']

class OutputSetDinosaurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dinosaur
        fields = ['id', 'game', 'x_position', 'y_position']

class SetDinosaursSerializer(serializers.ModelSerializer):

    dinosaurs_positions = serializers.ListField(
        child=serializers.ListField(
            child=serializers.IntegerField(),
            validators=[validators.MinLengthValidator(2), validators.MaxLengthValidator(2)]
        ),
    )

    class Meta:
        model = Dinosaur
        fields = ['id', 'dinosaurs_positions']
        
class MoveActionSerializer(serializers.Serializer):

    action = serializers.DictField(
        child=serializers.CharField(max_length=8),
        validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(8)]
    )

    def validate_action(self, value):
        if value['direction'] not in ['N', 'S', 'E', 'W']:
            raise serializers.ValidationError("Direction must be N, S, E or W")
        if value['action_type'] not in ['move']:
            raise serializers.ValidationError("Action must be move ")
        return value