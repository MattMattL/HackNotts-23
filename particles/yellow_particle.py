import math
import random
import pygame

from particles.particle_handler import ParticleHandler

class YellowParticle(ParticleHandler):

	def __init__(self):
		self.ID = "YELLOW PARTICLE"
		self.posX = random.randint(0, 1600)
		self.posY = random.randint(0, 1000)
		self.m = 1

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID in ["RED PARTICLE", "GREEN PARTICLE"] : return True

		return False

	def F(self, x, y):
		rx, ry = -x + self.posX, -y + self.posY
		rn = (rx*rx + ry*ry)

		fx = math.exp(-rx*rx)
		fy = math.exp(-ry*ry)

		if rn <= 80: # repel
			return fx, fy
		elif rn <= 140: # attract
			return -fx, -fy
		else:
			return fx, fy

	def draw(self, window):
		return pygame.draw.circle(window, color=(255, 255, 0), center=(self.posX, self.posY), radius=3)


	def postUpdate(self):
		""" Called at the end of each frame """
		pass