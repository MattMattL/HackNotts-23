# import the child classes
import random

import numpy as np
import pygame

from particles.particle_handler import ParticleHandler

# extend your particle class with ParticleHandler
class ExampleParticle(ParticleHandler):

	def __init__(self):
		self.ID = "EXAMPLE PARTICLE"
		self.posY = random.randint(0, 1000)
		self.posX = random.randint(0, 600)

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "EXAMPLE PARTICLE":
			return True

		return False

	def F(self, x, y):
		rx, ry = x - self.posX, y - self.posY
		rn = (rx*rx + ry*ry)**0.5

		return (0, 0) if rn == 0 else ((1 / rn**3)*rx, (1 / rn**3)*ry)

	def update(self, pGroups, dt):
		""" Called at the start of each frame. Update x and y here """
		for pType in pGroups:
			for particle in pType:
				# dx , dy = particle.F(self.posX,self.posY)
				self.posX += random.randint(-1, 1)
				self.posY += random.randint(-1, 1)
				pass

	def draw(self, window):
		return pygame.draw.circle(window, color=(0, 255, 0), center=(self.posX, self.posY), radius=5)

	def postUpdate(self):
		""" Called at the end of each frame """
		pass
