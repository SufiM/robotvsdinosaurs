from django.urls import path

from .views import InitiateGame, SetRobot, SetDinosaur, GetGame, MoveAction, AttackAction

urlpatterns = [
    path('games/<int:pk>', GetGame.as_view(), name='get-game'),
    path('games/initiate-game/start', InitiateGame.as_view(), name='initiate-game'),
    path('games/initiate-game/<int:pk>/set-robot', SetRobot.as_view(), name='set-robot'),
    path('games/initiate-game/<int:pk>/set-dinosaur', SetDinosaur.as_view(), name='set-Dinosaur'),
    path('games/<int:pk>/action/move', MoveAction.as_view(), name='robot-action'),
    path('games/<int:pk>/action/attack', AttackAction.as_view(), name='robot-action'),
]