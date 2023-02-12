"""
import pygame
import random
import numpy as np
import math

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

radius = 5

red_particles = []

cyan_particles = []
"""
"""
# importing the required libraries
import pygame
from pygame.locals import *
import random
import math

class Particle:
    def __init__(self, running, width, height, color):
        # initialising pygame
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Particle Life")  # setting title
        self.screen.fill(color)

        pygame.display.update()
        self.running = running

        # initialising clock
        self.clock = pygame.time.Clock()

        # colors
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.yellow = (255, 255, 0)

    # function to create
    # one particle on the scree

    def createParticle(self, x, y, color):
        pygame.draw.rect(self.screen, color, (x, y, 2, 2))

    # returns a dict

    def returnParticle(self, x, y, color, vx, vy):
        return {"x": x, "y": y, "color": color, "vx": vx, "vy": vy}

    # returns a list consisting
    # of all the necessary things

    def manyParticles(self, number, color):
        group = []
        for i in range(number):
            x = random.randint(1, self.width-1)
            y = random.randint(1, self.height-1)
            vx = 0
            vy = 0

            group.append(self.returnParticle(x, y, color, vx, vy))
        return group

    # the function to create
    # many particles

    def createParticles(self, particles):
        for particle in particles:
            self.createParticle(
                particle["x"], particle["y"], particle["color"])

    # this is the mainrule function
    # which follows F = GMm/r^2
    # and this will move the particles towards each other
    # and also coordinate geometry = squareroot[(x2-x1)^2 + (y2-y1)^2]
    # and also F = ma

    def mainRule(self, particles1, particles2, g):
        # first iterating over all the particles in the particles1
        for i in range(len(particles1)):
            # setting the force to be applied
            # in the x and y coordinates
            fx = 0
            fy = 0

            # now iterating over the particles2
            for j in range(len(particles2)):
                a = particles1[i]
                b = particles2[j]
                dx = a["x"]-b["x"]
                dy = a["y"]-b["y"]
                # using coordinate geometry to find the distance between two particles
                d = math.sqrt(dx*dx+dy*dy)
                if (d > 0):
                    F = g*1/d
                    fx += (F*dx)
                    fy += (F*dy)

            a["vx"] = (a["vx"] + fx)*0.5
            a["vy"] = (a["vy"] + fy)*0.5
            # due to the forc applied
            # the particles also face acceleration
            # so setting the velocity using the force formula
            a["x"] += a["vx"]
            a["y"] += a["vy"]

            # now reversing the particles
            # when they hit the wall
            if (a["x"] <= 0 or a["x"] >= 700):
                a["vx"] *= -1
            elif (a["y"] <= 0 or a["y"] >= 500):
                a["vy"] *= -1
        self.screen.fill(0)

    # the main loop

    def gameLoop(self):
        # defining particles
        self.yellowParticles = self.manyParticles(200, self.yellow)
        self.redParticles = self.manyParticles(200, self.red)
        self.greenParticles = self.manyParticles(200, self.green)
        self.blueParticles = self.manyParticles(200, self.blue)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # creating the particles
            self.createParticles(self.yellowParticles)
            self.createParticles(self.redParticles)
            self.createParticles(self.greenParticles)
            self.createParticles(self.blueParticles)

            # updating the display
            pygame.display.update()

            # enter your rules here
            # defining the rules
            self.mainRule(self.yellowParticles, self.yellowParticles, -0.1)

            self.clock.tick(78)
        pygame.quit()

# the main function


def main():
    particleLife = Particle(True, 700, 500, (0, 0, 0))
    particleLife.gameLoop()


if __name__ == "__main__":
    main()

"""
## A simple Python port - You need: pip install pygame. Note the code here is not efficient but it's made to be educational and easy
import pygame
import random
import math

atoms=[]
window_size = 300
pygame.init()
window = pygame.display.set_mode((1920, 1080))
#deltaTime = pygame.time.get_ticks()


def draw(surface, x, y, color, radius):
    for i in range(0, radius):
        pygame.draw.circle(surface, color, (x, y), radius)
               
def atom(x, y, c):
    return {"x": x, "y": y, "vx": 0, "vy": 0, "color": c}

def randomxy():
    return round(random.random()*1920 + 1)

def create(number, color):
    group = []
    for i in range(number):
        group.append(atom(randomxy(), randomxy(), color))
        atoms.append((group[i])) #all particles
    return group


def rule(atoms1, atoms2, g):
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
        a["x"] += a["vx"]
        a["y"] += a["vy"]
        if(a["x"] <= 0 or a["x"] >= 1920):
            a["vx"] *=-1
        if(a["y"] <= 0 or a["y"] >= 1080):
            a["vy"] *=-1        


""" def rule2(atoms1, atoms2):
    for i in range(len(atoms1)):
        for j in range(len(atoms2)):
            pA = atoms1[i]
            pB = atoms2[j]
            dx = pA["x"] - pB["x"]
            dy = pA["y"] - pB["y"]
            r = math.sqrt(dx**2 + dy**2)
            if r < 20:
                t = pygame.time.get_ticks() - deltaTime
                pA["x"] += math.sin(t) + 5
                pA["y"] += math.sin(t) + 5
            elif r > 20:
                pass """



cyan = create(200, "cyan")
magenta = create(200, "magenta")
#white = create(200, "white")


run = True
while run:
    window.fill(0)
    rule(magenta, magenta, 14)
    rule(magenta, cyan, -15)
    rule(cyan, cyan, -200)
    for i in range(len(atoms)):
        draw(window,  atoms[i]["x"], atoms[i]["y"], atoms[i]["color"], 2)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
exit()
