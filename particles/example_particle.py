# import the child classes
from particles.particle_handler import ParticleHandler

# extend your particle class with ParticleHandler
class ExampleParticle(ParticleHandler):

	def __init__(self):
		pass

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def update(self):
		""" Called at the start of each frame """
		pass

	def postUpdate(self):
		""" Called at the end of each frame """
		pass