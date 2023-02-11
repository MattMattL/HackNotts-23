# handler class containing things to be used in parent classes

class ParticleHandler():

	def __init__(self):
		self.ID = None
		self.posY = None
		self.posX = None

		self.color = (255, 255, 255)
		self.size = 5

	def start(self):
		pass

	def isAffectedBy(self, particleID):
		return False

	def update(self, pGroups, dt):
		pass

	def postUpdate(self):
		pass