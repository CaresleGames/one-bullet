import pygame
from pygame.locals import *

class Player:
	def __init__(self, x, y):
		self.position = pygame.Rect(x, y, 16, 16)
		self.speed = 4
		self.image = pygame.image.load("assets/player.png").convert_alpha()

	def move(self, keys, keys_pressed, WIDTH, HEIGHT):
		if keys[keys_pressed[0]] and self.position.x > 0:
			self.position.x -= self.speed
		if keys[keys_pressed[1]] and self.position.x + self.position.width < WIDTH:
			self.position.x += self.speed
		if keys[keys_pressed[2]] and self.position.y + self.position.height < HEIGHT:
			self.position.y += self.speed
		if keys[keys_pressed[3]] and self.position.y > 0:
			self.position.y -= self.speed