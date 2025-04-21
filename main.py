import pygame
import sys

from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = (updatable,)

	asteroid_field = AsteroidField()

	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		for a in asteroids:
			if CircleShape.collision(player, a):
				sys.exit()

		pygame.Surface.fill(screen, (0,0,0))
		for d in drawable:
			d.draw(screen)
		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
