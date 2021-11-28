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


	def exit_screen(self, width: int, height: int) -> bool:
		if (
			self.position.x > width
			or self.position.x < 0
			or self.position.y < 0
			or self.position.y > height
		):
			return True
		return False

	def rotate_image(self):
		if self.direction.y != 0:
			self.image = self.image_rotate
		else:
			self.image = self.image_normal