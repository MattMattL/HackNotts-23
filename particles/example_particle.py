# import the child classes
from particles.particle_handler import ParticleHandler
import numpy

# extend your particle class with ParticleHandler
class ExampleParticle(ParticleHandler):

	def __init__(self):
		self.ID = "EXAMPLE PARTICLE"
		self.posY = 300
		self.posX = 300

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "EXAMPLE PARTICLE":
			return True

		return False

	def update(self, particles, dt):
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
