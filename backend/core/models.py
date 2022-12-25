from django.db import models

# Create your models here.

STATUS_CHOICES = (
    (0, 'Set Robot'),
    (1, 'Set Dinosaur'),
    (2, 'Playing'),
    (3, 'Game finished'),
)


class Game(models.Model):
    player = models.CharField(max_length=100, default='Player')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.player} Game"


class Board(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_board')
    cells = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.game.player
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.cells = self.generate_cells()
        super(Board, self).save(*args, **kwargs)
        
    def generate_cells(self):
        cells = []
        for i in range(10):
            row = [0] * 10
            cells.append(row)
        return cells


class Robot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_robot')
    x_position = models.IntegerField(null=False)
    y_position = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.game.player

class Dinosaur(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_dinosaur')
    x_position = models.IntegerField(null=False)
    y_position = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.game.player
