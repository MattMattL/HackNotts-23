import pygame

def circleTest():

	pygame.init()

	window = pygame.display.set_mode((800, 500))
	pygame.display.set_caption("pygame test")

	shouldRunGame = True

	x, y = 100, 100

	while shouldRunGame:
		pygame.time.delay(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				shouldRunGame = False

			keys = pygame.key.get_pressed()

			if keys[pygame.K_d]:
				x += 6

			if keys[pygame.K_a]:
				x -= 6

			if keys[pygame.K_w]:
				y -= 6

			if keys[pygame.K_s]:
				y += 6

		pygame.draw.circle(surface=window, color=(255, 255, 0), center=(x, y), radius=5)

		pygame.display.update()

	pygame.quit()