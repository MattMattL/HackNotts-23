# import the child classes
from particles.particle_handler import ParticleHandler

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

	def update(self, particles):
		""" Called at the start of each frame. Update x and y here """
		pass

	def postUpdate(self):
		""" Called at the end of each frame """
		pass