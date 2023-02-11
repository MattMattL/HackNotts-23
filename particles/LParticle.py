# import the child classes
import random

from particles.particle_handler import ParticleHandler
import numpy as np
import pygame

# extend your particle class with ParticleHandler
class LParticle(ParticleHandler):

	def __init__(self):
		self.ID = "EXAMPLE PARTICLE"
		self.posY = random.randint(0, 600)
		self.posX = random.randint(0, 1000)
		self.pos = np.array([])

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "EXAMPLE PARTICLE":
			return True

		return False

	def F(self, x, y):
		r = np.array([x - self.posX, y - self.posY])
		rn = np.linalg.norm(r)

		return 0*r if rn == 0 else (1 / rn**3) * r

	def update(self, particles, dt):
		""" Called at the start of each frame. Update x and y here """
		for pType in particles:
			for particle in pType:
				dx, dy = particle.F(self.posX, self.posY) * dt / 1000
				self.posX += 1000 * dx
				self.posY += 1000 * dy

				# print(self.posX, self.posY)

	def draw(self, window):
		return pygame.draw.circle(window, color=(255, 0, 0), center=(self.posX, self.posY), radius=5)

	def postUpdate(self):
		""" Called at the end of each frame """
		pass