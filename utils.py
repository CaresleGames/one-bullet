import pygame
from pygame.locals import *

def check_collision(rect : pygame.Rect, rect2: pygame.Rect) -> bool:
	if (
		rect.x > rect2.x + rect2.width
		or rect.x + rect.width < rect2.x
		or rect.y > rect2.y + rect2.height
		or rect.y + rect.height < rect2.y
	):
		return False

	return True