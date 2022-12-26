from django.shortcuts import render
from rest_framework import generics, status, serializers
from .serializers import(StartGameSerializer, OutputGameSerializer, OutputGetGameSerializer, 
                    SetRobotSerializer, SetDinosaursSerializer, MoveActionSerializer)
from rest_framework.response import Response
from .models import Game, Board, Robot, Dinosaur
from .utils import validate_position, error_response
import inspect
from traceback import format_exc
from rest_framework.exceptions import ValidationError

error_response = error_response.copy()

def update_board(game: Game, x: int, y: int, object_type:str, prev_location: tuple) -> None:
    try:
        board = Board.objects.get(game=game)
        cells = board.cells
        value = 1 if object_type == 'robot' else 2 if object_type == 'dinosaur' else 0

        if prev_location:
            cells[prev_location[0]][prev_location[1]] = 0

        cells[x][y] = value
        board.cells = cells
        board.save()
    except Exception as e:
        raise Exception(f"{str(e)} in {inspect.stack()[0][3]}")

class GetGame(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        try:
            game = Game.objects.get(pk=kwargs['pk'])
            return Response(OutputGetGameSerializer(game).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f"{str(e)} in {inspect.stack()[0][3]}"}, status=status.HTTP_400_BAD_REQUEST)
        

class InitiateGame(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        
        try:
            serializer = StartGameSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            game = Game.objects.create(player=request.data['player'])
            board = Board.objects.create(game=game)
            return Response(OutputGameSerializer(game).data, status=status.HTTP_201_CREATED)
   
        except Exception as e:
            return Response({'error': f"{str(e)} in {inspect.stack()[0][3]}"}, status=status.HTTP_400_BAD_REQUEST)

class SetRobot(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        try:
            serializer = SetRobotSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            game = Game.objects.get(pk=kwargs['pk'])
            if game.game_robot.exists():
                return Response({'error': 'Robot already exists'}, status=status.HTTP_400_BAD_REQUEST)

            board_cells = Board.objects.get(game=game).cells
            robot_position = serializer.validated_data['robot_position']

            validate_position(value=robot_position)

            if board_cells[robot_position[0]][robot_position[1]] == 2:
                return Response({'error': 'Robot cannot be placed on a dinosaur'}, status=status.HTTP_400_BAD_REQUEST)

            robot = Robot.objects.create(game=game, x_position=robot_position[0] , y_position=robot_position[1])
            update_board(game=game, x=robot_position[0], y=robot_position[1], object_type="robot", prev_location=None)
            robot.game.status = 1
            robot.game.save()
            return Response(OutputGetGameSerializer(robot.game).data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            error_response['error'] = e.detail[0]
            error_response['error_code'] = e.default_code
            return Response(error_response , status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f"Unhandled Error: {format_exc()}")
            return Response({'error': f"{str(e)} in {inspect.stack()[0][3]}"}, status=status.HTTP_400_BAD_REQUEST)

class SetDinosaur(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):

        try:
            serializer = SetDinosaursSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            game = Game.objects.get(pk=kwargs['pk'])

            board_cells = Board.objects.get(game=game).cells
            dinosaurs_positions = serializer.validated_data['dinosaurs_positions']

            for dinosaur_position in dinosaurs_positions:
                if validate_position(value=dinosaur_position):
                    return Response({f'error': 'Position in {dinosaur_position} is out of range'}, status=status.HTTP_400_BAD_REQUEST)

                if board_cells[dinosaur_position[0]][dinosaur_position[1]] == 1 or board_cells[dinosaur_position[0]][dinosaur_position[1]] == 2:
                    return Response({'error': 'Dinosaur cannot be placed on a robot or dinosaur'}, status=status.HTTP_400_BAD_REQUEST)

                dinosaur = Dinosaur.objects.create(game=game, x_position=dinosaur_position[0],
                                                   y_position=dinosaur_position[1])
                update_board(game=game, x=dinosaur_position[0], y=dinosaur_position[1], object_type="dinosaur", prev_location=None)
            game.status = 2
            game.save()
            return Response(OutputGetGameSerializer(dinosaur.game).data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': f"{str(e)} in {inspect.stack()[0][3]}"}, status=status.HTTP_400_BAD_REQUEST)

class MoveAction(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):

        try:
            serializer = MoveActionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            game = Game.objects.get(pk=kwargs['pk'])
            robot = Robot.objects.get(game=game)
            board = Board.objects.get(game=game)
            board_cells = board.cells
            action = serializer.validated_data['action']['action_type']
            direction = serializer.validated_data['action']['direction']

            if direction == 'N':
                if robot.y_position - 1 < 0:
                    return Response({'error': 'Robot cannot move out of range'}, status=status.HTTP_400_BAD_REQUEST)
                if board_cells[robot.x_position][robot.y_position - 1] == 2:
                    return Response({'error': 'Robot cannot move to a dinosaur'}, status=status.HTTP_400_BAD_REQUEST)
                robot.y_position -= 1
                update_board(game=game, x=robot.x_position, y=robot.y_position, object_type="robot", prev_location=[robot.x_position, robot.y_position + 1])
                robot.save()
                return Response(OutputGetGameSerializer(robot.game).data, status=status.HTTP_201_CREATED)
            elif direction == 'S':
                if robot.y_position + 1 > 9:
                    return Response({'error': 'Robot cannot move out of range'}, status=status.HTTP_400_BAD_REQUEST)
                if board_cells[robot.x_position][robot.y_position + 1] == 2:
                    return Response({'error': 'Robot cannot move to a dinosaur'}, status=status.HTTP_400_BAD_REQUEST)
                robot.y_position += 1
                update_board(game=game, x=robot.x_position, y=robot.y_position, object_type="robot", prev_location=[robot.x_position, robot.y_position - 1])
                robot.save()
                return Response(OutputGetGameSerializer(robot.game).data, status=status.HTTP_201_CREATED)
            elif direction == 'E':
                if robot.x_position + 1 > 9:
                    return Response({'error': 'Robot cannot move out of range'}, status=status.HTTP_400_BAD_REQUEST)
                if board_cells[robot.x_position + 1][robot.y_position] == 2:
                    return Response({'error': 'Robot cannot move to a dinosaur'}, status=status.HTTP_400_BAD_REQUEST)
                robot.x_position += 1
                update_board(game=game, x=robot.x_position, y=robot.y_position, object_type="robot", prev_location=[robot.x_position - 1, robot.y_position])
                robot.save()
                return Response(OutputGetGameSerializer(robot.game).data, status=status.HTTP_201_CREATED)
            elif direction == 'W':
                if robot.x_position - 1 < 0:
                    return Response({'error': 'Robot cannot move out of range'}, status=status.HTTP_400_BAD_REQUEST)
                if board_cells[robot.x_position - 1][robot.y_position] == 2:
                    return Response({'error': 'Robot cannot move to a dinosaur'}, status=status.HTTP_400_BAD_REQUEST)
                robot.x_position -= 1
                update_board(game=game, x=robot.x_position, y=robot.y_position, object_type="robot", prev_location=[robot.x_position + 1, robot.y_position])
                robot.save()
                return Response(OutputGetGameSerializer(robot.game).data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': f"{str(e)} in {inspect.stack()[0][3]}"}, status=status.HTTP_400_BAD_REQUEST)

class AttackAction(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        try:
            game = Game.objects.get(pk=kwargs['pk'])
            robot = Robot.objects.get(game=game)
            dinosaurs = Dinosaur.objects.filter(game=game)

            if robot.y_position - 1 >= 0:
                for dinosaur in dinosaurs:
                    if dinosaur.x_position == robot.x_position and dinosaur.y_position == robot.y_position - 1:
                        dinosaur.delete()
                        update_board(game=game, x=dinosaur.x_position, y=dinosaur.y_position, object_type="empty", prev_location=None)
            if robot.y_position + 1 <= 9:
                for dinosaur in dinosaurs:
                    if dinosaur.x_position == robot.x_position and dinosaur.y_position == robot.y_position + 1:
                        dinosaur.delete()
                        update_board(game=game, x=dinosaur.x_position, y=dinosaur.y_position, object_type="empty", prev_location=None)
            if robot.x_position - 1 >= 0:
                for dinosaur in dinosaurs:
                    if dinosaur.x_position == robot.x_position - 1 and dinosaur.y_position == robot.y_position:
                        dinosaur.delete()
                        update_board(game=game, x=dinosaur.x_position, y=dinosaur.y_position, object_type="empty", prev_location=None)
            if robot.x_position + 1 <= 9:
                for dinosaur in dinosaurs:
                    if dinosaur.x_position == robot.x_position + 1 and dinosaur.y_position == robot.y_position:
                        dinosaur.delete()
                        update_board(game=game, x=dinosaur.x_position, y=dinosaur.y_position, object_type="empty", prev_location=None)

            # check if game is over
            if len(Dinosaur.objects.filter(game=game)) == 0:
                game.status = 3
                game.save()

            return Response(OutputGetGameSerializer(robot.game).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f"{str(e)} in {inspect.stack()[0][3]}"}, status=status.HTTP_400_BAD_REQUEST)