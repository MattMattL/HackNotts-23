# import the child classes
from particles.particle_handler import ParticleHandler
import numpy as np

# extend your particle class with ParticleHandler
class ExampleParticle(ParticleHandler):

	def __init__(self):
		self.ID = "EXAMPLE PARTICLE"
		self.posY = 300
		self.posX = 300
		self.pos = np.array([])

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "EXAMPLE PARTICLE":
			return True

		return False

	def F(self,x,y):
		r = np.array[x - self.posX, y - self.posY]
		rn  = np.linalg.norm(r)
		return (1/rn***3)*r
	def update(self, particles):
		""" Called at the start of each frame. Update x and y here """
		for pType in particles:
			for particle in pType:
				dx , dy = particle.F(self.posX,self.posY) 
				self.posX += dx
				self.posY += dy
				pass

	def postUpdate(self):
		""" Called at the end of each frame """
		pass