import time
import math
import random
import pygame

from particles.green_particle import GreenParticle
from particles.yellow_particle import YellowParticle
from particles.red_particle import RedParticle
from particles.particle_handler import ParticleHandler

# import circle_test
# circle_test.circleTest()

atoms=[]
window_size = 1500

def draw(surface, x, y, color, size):
    for i in range(0, size):
        pygame.draw.line(surface, color, (x, y-1), (x, y+2), abs(size))

def atom(x, y, c):
    return {"x": x, "y": y, "vx": 0, "vy": 0, "color": c}

def randomxy():
    return round(random.random()*window_size + 1)

def create(number, color):
    group = []
    for i in range(number):
        group.append(atom(randomxy(), randomxy(), color))
        atoms.append((group[i]))
    return group

def rule(atoms1, atoms2, g):
    field = ParticleHandler()

    for i in range(len(atoms1)):
        fx = 0
        fy = 0
        for j in range(len(atoms2)):
            a = atoms1[i]
            b = atoms2[j]
            dx = a["x"] - b["x"]
            dy = a["y"] - b["y"]
            d = (dx*dx + dy*dy)**0.5
            if( d > 0 and d < 80):
                F = g/d
                fx += F*dx
                fy += F*dy
        a["vx"] = (a["vx"] + fx)*0.5
        a["vy"] = (a["vy"] + fy)*0.5

        field.posX, field.posY = a["x"], a["y"]
        dxB, dyB = field.baseField()

        a["x"] += a["vx"] + 0.003 * dxB
        a["y"] += a["vy"] + 0.003 * dyB
        if(a["x"] <= 0 or a["x"] >= window_size):
            a["vx"] *=-1
        if(a["y"] <= 0 or a["y"] >= window_size):
            a["vy"] *=-1

def main():
	pygame.init()
	window = pygame.display.set_mode((1500, 1000))
	pygame.display.set_caption("Conway's Particles just like Schrodinger's Cat")

	# Pre-initialisations
	shouldContinueRunning = True
	deltaTime = pygame.time.get_ticks()

	cyan = create(100, "cyan")
	magenta = create(100, "magenta")
	white = create(100, "white")

	particles = [[GreenParticle() for _ in range(100)], \
				 [YellowParticle() for _ in range(100)], \
				 [RedParticle() for _ in range(100)]]

	while shouldContinueRunning:
		# Initialisations
		deltaTime = pygame.time.get_ticks() - deltaTime
		window.fill((0, 0, 0))
		pygame.time.delay(20) # 30 FPS

		# Update
		for target in particles:
			referenceParticles = []

			# find and save particle types that affect 'target'
			for ref in particles:
				if target[0].isAffectedBy(ref[0].ID):
					referenceParticles.append(ref)

			# pass the array to target particles
			for particle in target:
				particle.update(referenceParticles, deltaTime/1000)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				shouldContinueRunning = False

			keysPressed = pygame.key.get_pressed()

		# Draw particles
		for pType in particles:
			for particle in pType:
				if 0<= particle.posX <= 1500 and 0<=particle.posY<=1000:
					particle.draw(window)
				else:
					if particle.posX > 1500:
						particle.posX = 3000 - particle.posX
					else:
						particle.posX = -particle.posX

					if particle.posY < 0:
						particle.posY = -particle.posY
					else:
						particle.posY = 2000 - particle.posY
					particle.draw(window)

		#
		rule(magenta, magenta, 14)
		rule(magenta, cyan, -50)
		rule(cyan, cyan, -10)
		rule(white, white, math.sin(deltaTime))
		rule(white, magenta, -10)

		for i in range(len(atoms)):
			draw(window, atoms[i]["x"], atoms[i]["y"], atoms[i]["color"], 3)

		# Post-initialisations
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()