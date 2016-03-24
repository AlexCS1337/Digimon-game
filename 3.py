from pygame.time import Clock
import random
import time
import itertools
import pygame
import os, sys
# os.environ['SDL_VIDEO_CENTERED'] = '1'
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1000,100)
import glob
from ctypes import windll, Structure, c_long, byref #windows only


class RECT(Structure):
    _fields_ = [
    ('left',    c_long),
    ('top',     c_long),
    ('right',   c_long),
    ('bottom',  c_long),
    ]
    def width(self):  return self.right  - self.left
    def height(self): return self.bottom - self.top


def onTop(window):
    SetWindowPos = windll.user32.SetWindowPos
    GetWindowRect = windll.user32.GetWindowRect
    rc = RECT()
    GetWindowRect(window, byref(rc))
    SetWindowPos(window, -1, rc.left, rc.top, 0, 0, 0x0001)
	

 
## CLASSES ----------------------------------------------
 
class Digimon(object):
    def __init__(self,age ,weight,strength,defence,speed,intelligence):
        self.age = age
        self.weight = weight    
        self.strength = strength
        self.defence = defence  
        self.speed = speed  
        self.intelligence = intelligence
       
Player  = Digimon(0,0,0,0,0,0)
## In training I -----------------------------------------------
Botamon = Digimon(0,2,1,0,0,0)
Ketomon = Digimon(0,2,1,0,0,0)
Kuamon  = Digimon(0,2,0,1,0,0)
Poyomon = Digimon(0,2,0,0,0,1)
Punimon = Digimon(0,2,0,0,1,0)

## In training II ----------------------------------------------

## Rookie ------------------------------------------------------
#Agumon
#Gabumon
Elecmon = Digimon(4,5,5,3,4,4)
#Patamon
#Wormmon
#Veemon
Terriermon = Digimon(4,4,3,3,5,4)
Keramon    = Digimon(4,3,6,2,2,6)


## Ultimate ----------------------------------------------------
Pumpkinmon = Digimon(12,8,12,8,6,8)

#Agumon = Digimon(5,2,2,2,1,1)
#Terriermon = Digimon(5,2,1,1,3,2)
 
Agumon_idle_right = []
for image in glob.glob("image/In training_I/Poyomon_idle/?.png"):
    Agumon_idle_right.append(pygame.image.load(image))
    Agumon_idle_right_cycle = itertools.cycle(Agumon_idle_right)
Elecmon_idle_right = []
for image in glob.glob("image/In training_II\Koromon_idle/?.png"):
    Elecmon_idle_right.append(pygame.image.load(image))
    Elecmon_idle_right_cycle = itertools.cycle(Elecmon_idle_right)
Botamon_idle_right = []
for image in glob.glob("image/In training_I/Poyomon_idle/?.png"):
    Botamon_idle_right.append(pygame.image.load(image))
    Botamon_idle_right_cycle = itertools.cycle(Botamon_idle_right)
 
   
## INIT -------------------------------------------------
 
pygame.init()
screen = pygame.display.set_mode([300, 100])
pygame.display.set_caption('Digimon Simulator')
onTop(pygame.display.get_wm_info()['window'])
background_image = pygame.image.load("background.png").convert()
bar_full = pygame.image.load("bar_background.png").convert()
bar = pygame.image.load("bar.png").convert()
meat = pygame.image.load("0.png").convert()
bar_length_x, bar_length_y = (50, 2)
Digimon_x_pos, Digimon_y_pos = 150, 59
 
# TIME -------------------------------------------------
delay = 40
test_delay = 100
age_delay = 500
clock = pygame.time.Clock()
fps = 60
timer = 0
test_timer = 0
age_timer = 0
change = False
test_change = False
age_change = False
dt = 0
clock.tick()
 
loop = True
done = False # loop control
 
while not done:
	screen.blit(background_image, [0, 0])
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT:
			done = True # ends loop. game exit		
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos # gets the x, y position of the mouse click
			
			if x >= Digimon_x_pos:
			#if ( x  in range(10,100)) and ( y in range(10,100)): # if in range, add age +1 to player
				print "hello"
				difference = (50 - bar_length_x)
				bar_length_x += difference
				Player.__dict__ = Elecmon.__dict__
			if x <= Digimon_x_pos:
			#if ( x  in range(10,100)) and ( y in range(10,100)): # if in range, add age +1 to player
				print "hello"
				difference = (50 - bar_length_x)
				bar_length_x += difference
				Player.__dict__ = Botamon.__dict__

	timer += dt
	test_timer += dt
	age_timer += dt
	dt = clock.tick(fps)

	bar_transform = pygame.transform.scale(bar, (bar_length_x, bar_length_y)) # transforms the bar to 50 x, 2 y. can be changed now
	screen.blit(bar_full, [6,10])
	screen.blit(bar_transform ,[24,15])
	screen.blit(meat ,[50,40])
		
	Agumon_idle_right_cycle_next = Agumon_idle_right_cycle.next()
	Elecmon_idle_right_cycle_next = Elecmon_idle_right_cycle.next()
	Botamon_idle_right_cycle_next = Botamon_idle_right_cycle.next()
	if loop:
	#for the age. increases incrementally
		if age_timer >= age_delay:
			age_timer -= age_delay
			age_change = not age_change
			if age_change:
				Player.age += 0.01
				print Player.age
	#for the digimon sprites#
		if timer >= delay:
			timer -= delay
			change = not change
			if change:
				if Player.__dict__ == Elecmon.__dict__:
					screen.blit((Elecmon_idle_right_cycle_next), (Digimon_x_pos, Digimon_y_pos))
					pygame.display.flip() # shows screen fill.
				elif Player.__dict__ == Botamon.__dict__:
					screen.blit((Botamon_idle_right_cycle_next), (Digimon_x_pos, Digimon_y_pos))
					pygame.display.flip() # shows screen fill.					
				else:
					screen.blit((Agumon_idle_right_cycle_next), (Digimon_x_pos, Digimon_y_pos))
					pygame.display.flip() # shows screen fill.
	#for the happiness bar
		if test_timer >= test_delay:
			test_timer -= test_delay
			test_change = not test_change
			if test_change:
				if bar_length_x == 0:
					bar_length_x == 0
				else:
					bar_length_x -= 1
					pygame.display.flip() # shows screen fill.
	#pygame.display.flip() # shows screen fill.	
	clock.tick(fps) # Limit to 60 frames per second
pygame.quit()