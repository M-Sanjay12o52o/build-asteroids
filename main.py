import pygame
from constants import *

def main():
	pygame.init()
	print("Starting Asteroids!")
	print("Screen width:",SCREEN_WIDTH)
	print("Screen height:",SCREEN_HEIGHT)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		black = (0, 0, 0)
		# pygame.Surface.fill(black)
		screen.fill(black)
		pygame.display.flip()


if __name__ == "__main__":
	main()
