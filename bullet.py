import pygame
from pygame.locals import *

class Bullet:
	def __init__(self, x, y):
		self.position = pygame.Rect(x, y, 32, 16)
		self.image = pygame.image.load("assets/bullet.png").convert_alpha()
		self.speed = 10

	def move(self):
		self.position.x += self.speed