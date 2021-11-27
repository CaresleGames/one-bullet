import pygame
from pygame.locals import *

class Bullet:
	def __init__(self, x, y):
		self.position = pygame.Rect(x, y, 32, 16)
		
		self.image = pygame.image.load("assets/bullet.png").convert_alpha()
		self.image_normal = self.image
		self.image_rotate = pygame.transform.rotate(self.image, 90)
		
		self.speed = 10
		self.direction = pygame.Vector2(1, 0)

	def move(self):
		self.position.x += self.speed * self.direction.x
		self.position.y += self.speed * self.direction.y


	def rotate_image(self):
		if self.direction.y != 0:
			self.image = self.image_rotate
		else:
			self.image = self.image_normal