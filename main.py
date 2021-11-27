import pygame, sys
from pygame.locals import *
from bullet import Bullet
from player import Player
from utils import check_collision

pygame.init()

WIDTH, HEIGHT = 800, 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("One bullet")

background_color = pygame.Color(0, 0, 0)
clock = pygame.time.Clock()

player_left = Player(0, 0)
player_right = Player(50, 50)

bullet_left = Bullet(-100, -100)
bullet_right = Bullet(-300, -300)

def restart_game():
	player_left.shoot = False
	player_right.shoot = False


def main():
	run = True

	while run:
		clock.tick(60)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				# Player right shoot
				# Change bullet position, direction and image rotation
				if event.key == pygame.K_SPACE and not player_right.shoot:
					bullet_right.position.x = player_right.position.x
					bullet_right.position.y = player_right.position.y
					bullet_right.direction = player_right.direction
					bullet_right.rotate_image()
					player_right.shoot = True

		keys = pygame.key.get_pressed()
		
		if keys[K_k]:
			restart_game()

		player_left.move(keys, [K_a, K_d, K_s, K_w], WIDTH, HEIGHT)
		player_right.move(keys, [K_LEFT, K_RIGHT, K_DOWN, K_UP], WIDTH, HEIGHT)
		
		if player_right.shoot:
			bullet_right.move()

		if check_collision(bullet_right.position, player_left.position):
			player_left.is_alive = False

		screen.fill(background_color)

		screen.blit(bullet_right.image, bullet_right.position)
		
		if player_left.is_alive:
			screen.blit(player_left.image, player_left.position)
		
		if player_right.is_alive:
			screen.blit(player_right.image, player_right.position)
		
		pygame.display.update()


if __name__ == '__main__':
	main()