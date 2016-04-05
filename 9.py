from pygame.time import Clock
import random
import time
import itertools
import pygame
import os, sys
os.environ['SDL_VIDEO_CENTERED'] = '1'
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1000,100)
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

## Egg -----------------------------------------------

Egg = Digimon(0,0,0,0,0,0)

## In training I -----------------------------------------------
Botamon = Digimon(0,2,1,0,0,0)
Ketomon = Digimon(0,2,2,0,0,0)
Kuamon  = Digimon(0,2,0,1,0,0)
Poyomon = Digimon(0,2,0,0,0,1)
Punimon = Digimon(0,2,0,0,1,0)

## In training II ----------------------------------------------
Koromon = Digimon(2,4,3,1,1,1)
## Rookie ------------------------------------------------------
#Agumon
Elecmon = Digimon(4,5,5,3,4,4)
#Patamon
#Wormmon
#Veemon
Terriermon = Digimon(4,4,3,3,5,4)
Keramon    = Digimon(4,3,6,2,2,6)


## Ultimate ----------------------------------------------------
Pumpkinmon = Digimon(12,8,12,8,6,8)


 
Egg_idle = []
for image in glob.glob("image/Egg/?.png"):
    Egg_idle.append(pygame.image.load(image))
    Eggcycle = itertools.cycle(Egg_idle)
	
Botamon_idle = []
for image in glob.glob("image/In training_II/Koromon_idle/?.png"):
    Botamon_idle.append(pygame.image.load(image))
    Botamoncycle = itertools.cycle(Botamon_idle)
	
Koromon_idle = []
for image in glob.glob("image/Champion/Greymon_idle/?.png"):
    Koromon_idle.append(pygame.image.load(image))
    Koromoncycle = itertools.cycle(Koromon_idle)

Elecmon_idle = []
for image in glob.glob("image/Ultimate/MetalGreymon_idle/?.png"):
    Elecmon_idle.append(pygame.image.load(image))
    Elecmoncycle = itertools.cycle(Elecmon_idle)	
	
Meat = []
for image in glob.glob("meat/?.png"):
    Meat.append(pygame.image.load(image))
    Meatcycle = itertools.cycle(Meat)
 
   
## INIT -------------------------------------------------
 
pygame.init()
screen = pygame.display.set_mode([300, 100])
pygame.display.set_caption('Digimon Simulator')
onTop(pygame.display.get_wm_info()['window'])
font = pygame.font.Font("Digimonbasic.ttf", 15)
black = (  0,  0,  0) 
background_image = pygame.image.load("background3.png").convert()
bar_full = pygame.image.load("bar_background.png").convert()
bar = pygame.image.load("bar.png").convert()
bar_length_x, bar_length_y = (50, 2)
Digimon_x_pos, Digimon_y_pos = 105, 2
 
# TIME -------------------------------------------------
clock = pygame.time.Clock()
fps = 60
dt = 0
clock.tick()

Egg_timer, Egg_delay, Egg_change = 0,40, False 
Botamon_timer, Botamon_delay, Botamon_change = 0, 40, False
Koromon_timer, Koromon_delay, Koromon_change = 0, 40, False
Elecmon_timer, Elecmon_delay, Elecmon_change = 0, 40, False
Age_timer, Age_delay, Age_change = 0, 1200000, False
Hunger_timer, Hunger_delay, Hunger_change = 0,40,False
Sleep_timer, Sleep_delay, Sleep_change = 0,60000,False
Random_timer, Random_delay, Random_change = 0,6000,False
Meat_timer, Meat_delay, Meat_change = 0,80,False

Egg_sprite = True
Digimon_sprite = True

left = False
right = False
idle = False
 
done = False # loop control
 
while not done:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT:
			done = True # ends loop. game exit		
	dt = clock.tick(fps)

	Age_timer += dt
	Hunger_timer += dt
	Sleep_timer += dt
	Random_timer += dt
	Meat_timer += dt

	screen.blit(background_image, [0, 0])
	bar_transform = pygame.transform.scale(bar, (bar_length_x, bar_length_y)) # transforms the bar to 50 x, 2 y. can be changed now
	screen.blit(bar_full, [6,10])
	screen.blit(bar_transform ,[24,15])
	age_text = font.render("AGE:   " + str(Player.age), True, black)
	screen.blit(age_text, [200, 10])
	
	Eggcycle_next = Eggcycle.next()
	Botamoncycle_next = Botamoncycle.next()
	Koromoncycle_next = Koromoncycle.next()
	Elecmoncycle_next = Elecmoncycle.next()	
	Meatcycle_next = Meatcycle.next()	
	#for the age. increases incrementally
	if Age_timer >= Age_delay:
		Age_timer -= Age_delay
		Age_change = not Age_change
		if Age_change:
			Player.age += 1
	# for the digimon sprite change
	
	if Digimon_sprite:
		if Player.age == 1:
			Botamon_timer += dt
			if Botamon_timer >= Botamon_delay:
				Botamon_timer -= Botamon_delay
				Botamon_change = not Botamon_change
				if Botamon_change:
					screen.blit((Botamoncycle_next), (Digimon_x_pos, Digimon_y_pos))	
					pygame.display.flip() # shows screen fill.
					if left == True:
						if Digimon_x_pos <= 10:
							print "hm"
							Digimon_x_pos += 0
						else:
							Digimon_x_pos -= 1
							pygame.display.flip() # shows screen fill.
					elif right == True:
						Digimon_x_pos += 1
						pygame.display.flip() # shows screen fill
					elif idle == True:
						Digimon_x_pos += 0
		if Player.age == 2:
			Koromon_timer += dt
			if Koromon_timer >= Koromon_delay:
				Koromon_timer -= Koromon_delay
				Koromon_change = not Koromon_change
				if Koromon_change:
					print "hello"
					screen.blit((Koromoncycle_next), (Digimon_x_pos, Digimon_y_pos))	
					pygame.display.flip() # shows screen fill.	
		if Player.age >= 3:
			Elecmon_timer += dt
			if Elecmon_timer >= Elecmon_delay:
				Elecmon_timer -= Elecmon_delay
				Elecmon_change = not Elecmon_change
				if Elecmon_change:
					print "hello"
					screen.blit((Elecmoncycle_next), (Digimon_x_pos, Digimon_y_pos))	
					pygame.display.flip() # shows screen fill.
		if Player.age == 0:
			Egg_timer += dt
			if Egg_timer >= Egg_delay:
				Egg_timer -= Egg_delay
				Egg_change = not Egg_change
				if Egg_change:
					Player.__dict__ == Egg.__dict__
					screen.blit((Eggcycle_next), (Digimon_x_pos, Digimon_y_pos))
					pygame.display.flip() # shows screen fill.	
					if left == True:
							print "left = true"
							Digimon_x_pos -= 1

							pygame.display.flip() # shows screen fill.
					elif right == True:
						print "right = true"
						Digimon_x_pos += 1

						pygame.display.flip() # shows screen fill


								
	#for the hunger bar
	if Hunger_timer >= Hunger_delay:
		Hunger_timer -= Hunger_delay
		Hunger_change = not Hunger_change
		if Hunger_change:
			if bar_length_x == 0:
				bar_length_x == 0
			else:
				bar_length_x -= 1
	if bar_length_x <= 20:
		if Meat_timer >= Meat_delay:
			Meat_timer -= Meat_delay
			Meat_change = not Meat_change
			if Meat_change:
				screen.blit((Meatcycle_next), (Digimon_x_pos, Digimon_y_pos))
				pygame.display.flip() # shows screen fill
	if Sleep_timer >= Sleep_delay:
		Sleep_timer -= Sleep_delay
		Sleep_change = not Sleep_change
		if Sleep_change:
			print "Sleep"

	if Random_timer >= Random_delay:
		Random_timer -= Random_delay
		Random_change = not Random_change
		if Random_change:
			print "random"
			random_choice = random.randint(0,100)
			if random_choice >= 50:
				print "left"
				right = False
				idle = False
				left = True
			elif random_choice <= 50:
				print "right"
				left = False
				idle = False
				right = True
			else:
				left = False
				right = False
				idle = True
				
			
	clock.tick(fps) # Limit to 60 frames per second
pygame.quit()