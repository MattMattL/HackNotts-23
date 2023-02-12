import time
import pygame
import random as rand

from particles.green_particle import GreenParticle
from particles.yellow_particle import YellowParticle
from particles.red_particle import RedParticle

# import circle_test
# circle_test.circleTest()

def main():
	pygame.init()
	window = pygame.display.set_mode((1500, 1000))
	pygame.display.set_caption("Conway's Particles just like Schrodinger's Cat")

	# Pre-initialisations
	shouldContinueRunning = True
	deltaTime = pygame.time.get_ticks()

	particles = [[GreenParticle() for _ in range(100)], \
				 [YellowParticle() for _ in range(100)], \
				 [RedParticle() for _ in range(100)]]

	while shouldContinueRunning:
		# Initialisations
		deltaTime = pygame.time.get_ticks() - deltaTime
		window.fill((0, 0, 0))
		pygame.time.delay(20) # 30 FPS

		# Update
		for target in particles:
			referenceParticles = []

			# find and save particle types that affect 'target'
			for ref in particles:
				if target[0].isAffectedBy(ref[0].ID):
					referenceParticles.append(ref)

			# pass the array to target particles
			for particle in target:
				particle.update(referenceParticles, deltaTime/1000)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				shouldContinueRunning = False

			keysPressed = pygame.key.get_pressed()

		# Draw particles
		for pType in particles:
			for particle in pType:
				if 0<= particle.posX <= 1500 and 0<=particle.posY<=1000:
					particle.draw(window)
				else:
					if particle.posX>1500:
						particle.posX = rand.randint(1450,1500)
					else:
						particle.posX = rand.randint(0,50)
					if particle.posY<0:
						particle.posY = rand.randint(0,50)
					else:
						particle.posY = rand.randint(950,1000)
					particle.draw(window)


		# Post-initialisations
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()