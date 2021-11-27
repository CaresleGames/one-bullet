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

# Change bullet position, direction and image rotation
def shoot_logic(bullet: Bullet, player: Player):
	bullet.position.x = player.position.x
	bullet.position.y = player.position.y
	bullet.direction = player.direction
	bullet.rotate_image()
	player.shoot = True


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
				if event.key == pygame.K_SPACE and not player_right.shoot and player_right.is_alive:
					shoot_logic(bullet_right, player_right)

				# player left shoot
				if event.key == pygame.K_j and not player_left.shoot and player_left.is_alive:
					shoot_logic(bullet_left, player_left)

		keys = pygame.key.get_pressed()
		
		if keys[K_k]:
			restart_game()

		player_left.move(keys, [K_a, K_d, K_s, K_w], WIDTH, HEIGHT)
		player_right.move(keys, [K_LEFT, K_RIGHT, K_DOWN, K_UP], WIDTH, HEIGHT)
		
		if player_right.shoot:
			bullet_right.move()

		if player_left.shoot:
			bullet_left.move()

		if check_collision(bullet_right.position, player_left.position):
			player_left.is_alive = False

		if check_collision(bullet_left.position, player_right.position):
			player_right.is_alive = False

		screen.fill(background_color)

		screen.blit(bullet_right.image, bullet_right.position)
		screen.blit(bullet_left.image, bullet_left.position)

		if player_left.is_alive:
			screen.blit(player_left.image, player_left.position)
		
		if player_right.is_alive:
			screen.blit(player_right.image, player_right.position)
		
		pygame.display.update()


if __name__ == '__main__':
	main()