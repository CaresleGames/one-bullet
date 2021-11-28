import pygame, sys
from pygame.locals import *
from bullet import Bullet
from player import Player
from utils import check_collision

pygame.init()

WIDTH, HEIGHT = 800, 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("One bullet")

position_x = WIDTH // 2
position_y = HEIGHT // 2

background_color = pygame.Color(0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

current_scene : str = "game"
winner = ""
# Font
font = pygame.font.Font("assets/KenneyPixelSquare.ttf", 32)
FONT_COLOR = pygame.Color(255, 255, 255)

# Player left
player_left = Player(0, 0, "assets/player_left.png")
bullet_left = Bullet(-100, -100)

# Player right
player_right = Player(50, 50, "assets/player_right.png")
bullet_right = Bullet(-300, -300)

def restart_game():
	# Player left
	player_left.shoot = False
	player_left.is_alive = True
	player_left.position.x = position_x - (player_left.position.width // 2) - 128
	player_left.position.y = position_y - (player_left.position.height // 2) - 128
	# Bullet left
	bullet_left.position.x = -100
	bullet_left.position.y = -100
	
	# Player right
	player_right.shoot = False
	player_right.is_alive = True
	player_right.position.x = position_x + (player_right.position.width // 2) + 128
	player_right.position.y = position_y + (player_right.position.height // 2) + 128
	# Bullet right
	bullet_right.position.x = -300
	bullet_right.position.y = -300

# Change bullet position, direction and image rotation
def shoot_logic(bullet: Bullet, player: Player):
	bullet.position.x = player.position.x
	bullet.position.y = player.position.y
	bullet.direction = player.direction
	bullet.rotate_image()
	player.shoot = True


def no_win() -> bool:
	global winner
	if (
		player_left.is_alive and player_right.is_alive
		and bullet_left.exit_screen(WIDTH, HEIGHT)
		and bullet_right.exit_screen(WIDTH, HEIGHT)
		and player_left.shoot and player_right.shoot
	):
		winner = "Draw"
		return True
	return False


# Main game, draw the players and their movement
def game():
	run = True
	global current_scene
	global winner
	restart_game()
	while run:
		clock.tick(FPS)

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

		player_left.move(keys, [K_a, K_d, K_s, K_w], WIDTH, HEIGHT)
		player_right.move(keys, [K_LEFT, K_RIGHT, K_DOWN, K_UP], WIDTH, HEIGHT)
		
		if player_right.shoot:
			bullet_right.move()

		if player_left.shoot:
			bullet_left.move()

		if check_collision(bullet_right.position, player_left.position):
			player_left.is_alive = False
			winner = "PLAYER 2"

		if check_collision(bullet_left.position, player_right.position):
			player_right.is_alive = False
			winner = "PLAYER 1"

		# Draw
		screen.fill((125, 100, 125))

		screen.blit(bullet_right.image, bullet_right.position)
		screen.blit(bullet_left.image, bullet_left.position)

		if player_left.is_alive:
			screen.blit(player_left.image, player_left.position)
		
		if player_right.is_alive:
			screen.blit(player_right.image, player_right.position)
		
		if not player_left.is_alive or not player_right.is_alive or no_win():
			current_scene = "game_end"
			run = False
		pygame.display.update()


def game_end():
	run = True
	global winner
	text_surface : pygame.Surface = font.render(winner, False, FONT_COLOR)
	text_restart : pygame.Surface = font.render("PRESS SPACE TO PLAY AGAIN", False, FONT_COLOR)
	global current_scene
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					current_scene = "game"
					run = False
		screen.fill(background_color)
		screen.blit(text_surface, (position_x - text_surface.get_width() // 2, position_y - text_surface.get_height()))
		screen.blit(text_restart, (position_x - text_restart.get_width() // 2, position_y + text_restart.get_height()))

		pygame.display.update()


def main():
	run = True
	global current_scene
	while run:
		clock.tick(FPS)
		if current_scene == "game":
			game()
		if current_scene == "game_end":
			game_end()




if __name__ == '__main__':
	main()