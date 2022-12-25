from django.contrib import admin
from .models import Game, Board, Robot, Dinosaur

# Register your models here.

admin.site.register(Game)
admin.site.register(Board)
admin.site.register(Robot)
admin.site.register(Dinosaur)
