import time
import pygame

from particles.example_particle import ExampleParticle
from particles.matticle import MattsParticle
from particles.LParticle import LParticle

# import circle_test
# circle_test.circleTest()

def main():
	pygame.init()
	window = pygame.display.set_mode((1000, 600))
	pygame.display.set_caption("Conway's Particles just like Schrodinger's Cat")

	# Pre-initialisations
	shouldContinueRunning = True
	deltaTime = pygame.time.get_ticks()

	particles = [[ExampleParticle() for _ in range(5)], \
				 [LParticle() for _ in range(10)]]

	while shouldContinueRunning:
		# Initialisations
		deltaTime = pygame.time.get_ticks() - deltaTime
		window.fill((0, 0, 0))
		pygame.time.delay(33) # 30 FPS

		# Update
		for target in particles:
			referenceParticles = []

			# find and save particle types that affect 'target'
			for ref in particles:
				if target[0].isAffectedBy(ref[0].ID):
					referenceParticles.append(ref)

			# pass the array to target particles
			for particle in target:
				particle.update(referenceParticles, deltaTime)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				shouldContinueRunning = False

			keysPressed = pygame.key.get_pressed()

		# Draw particles
		for pType in particles:
			for particle in pType:
				particle.draw(window)

		# Post-initialisations
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()