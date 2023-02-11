# import the child classes
import random
import math

from particles.particle_handler import ParticleHandler
import numpy as np
import pygame

# extend your particle class with ParticleHandler
class RedParticle(ParticleHandler):

	def __init__(self):
		self.ID = "RED PARTICLE"
		self.posY = random.randint(0, 600)
		self.posX = random.randint(0, 1000)
		self.pos = np.array([])

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "EXAMPLE PARTICLE": return True
		if particleID == "RED PARTICLE": return True

		return False

	def F(self, x, y):
		dx, dy = self.posX - x, self.posY - y

		return dx*math.exp(-dx*dx), dy*math.exp(-dy*dy)

	def update(self, pGroups, dt):
		""" Called at the start of each frame. Update x and y here """
		dxB, dyB = self.baseField()
		newX, newY = self.posX, self.posY

		for pType in pGroups:
			if pType[0].ID == "RED PARTICLE":
				for particle in pType:
					dx, dy = particle.F(self.posX, self.posY)
					newX += 500*dx * dt
					newY += 500*dy * dt

			if pType[0].ID == "EXAMPLE PARTICLE":
				for particle in pType:
					dx, dy = particle.F(self.posX, self.posY)
					newX -= 800*dx * dt
					newY -= 800*dy * dt

		self.posX = newX
		self.posY = newY

	def draw(self, window):
		return pygame.draw.circle(window, color=(255, 0, 0), center=(self.posX, self.posY), radius=2)

	def postUpdate(self):
		""" Called at the end of each frame """
		pass