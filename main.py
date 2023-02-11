import time
import pygame

# import circle_test
# circle_test.circleTest()

def preInit():
	pass

def init():
	pass

def postInit():
	pygame.display.update()
	pass

def main():

	pygame.init()
	window = pygame.display.set_mode((1000, 600))
	pygame.display.set_caption("Conway's Particles just like Schrodinger's Cat")

	# Pre-initialisations
	shouldContinueRunning = True

	preInit()

	while shouldContinueRunning:
		# Initialisations
		pygame.time.delay(int(1000 / 30)) # 30 FPS
		init()

		# Run important stuff
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				shouldContinueRunning = False

			keysPressed = pygame.key.get_pressed()

		# Post-initialisations
		window.fill((0, 0, 0))

		postInit()

	pygame.quit()

if __name__ == "__main__":
	main()