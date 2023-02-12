# import the child classes
import random
import math

import numpy as np
import pygame

from particles.particle_handler import ParticleHandler

# extend your particle class with ParticleHandler
class GreenParticle(ParticleHandler):

	def __init__(self):
		self.ID = "GREEN PARTICLE"
		self.posX = random.randint(0, 1500)
		self.posY = random.randint(0, 1000)
		self.m = 1

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID in ["RED PARTICLE", "GREEN PARTICLE"] : return True #red attracts green, green repels yellow

		return False

	def FR(self, x, y): #attract stuff
		rx, ry = x - self.posX, y - self.posY
		rn = (rx*rx + ry*ry)

		if rn <= 5: # repel
			return 0,0
		elif rn <= 10: # attract
			return 0,0
		else:
			return (-(1 / rn**3)*rx, -(1 / rn**3)*ry)

	def FG(self, x, y): #attract stuff
		rx, ry = x - self.posX, y - self.posY
		rn = (rx*rx + ry*ry)

		if rn <= 100: # repel
			return 1/rx, 1/ry
		elif rn <= 10: # attract
			return 0,0
		else:
			return (-(1 / rn)*rx, -(1 / rn)*ry)

	def FY(self, x, y): #attract stuff
		rx, ry = x - self.posX, y - self.posY
		rn = (rx*rx + ry*ry)

		if rn <= 5: # repel
			return 0,0
		elif rn <= 10: # attract
			return 0,0
		else:
			return (-(1 / rn**3)*rx, -(1 / rn**3)*ry)

	def update(self, pGroups, dt):
		""" Called at the start of each frame. Update x and y here """
		dxB, dyB = self.baseField()
		self.posX += dxB / 10000
		self.posY += dyB / 10000

		for pType in pGroups:
			for particle in pType:
				if particle.ID == "RED PARTICLE":
					if (self.posX != particle.posX and self.posY != particle.posY):
						deltaX, deltaY = particle.FR(self.posX, self.posY)
						self.posX += self.m*deltaX*dt
						self.posY += self.m*deltaY*dt
				elif particle.ID == "GREEN PARTICLE":
					if (self.posX != particle.posX and self.posY != particle.posY):
						deltaX, deltaY = particle.FG(self.posX, self.posY)
						self.posX += self.m*deltaX*dt
						self.posY += self.m*deltaY*dt

	def draw(self, window):
		pygame.draw.circle(window, color=(0, 255, 0), center=(self.posX, self.posY), radius=5)

	def postUpdate(self):
		""" Called at the end of each frame """
		pass
