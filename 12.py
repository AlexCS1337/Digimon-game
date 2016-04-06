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
	
class Digimon(object):
    def __init__(self,age ,weight):
        self.age = age
        self.weight = weight   
Player  = Digimon(0,0)

Sprite_list = []
def sprite_load(sprite_location):
	for image in glob.glob(sprite_location):
		Sprite_list.append(pygame.image.load(image))
		Sprite_iter = itertools.cycle(Sprite_list)


		
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
Digimon_x_pos, Digimon_y_pos = 50, 2 # 105, 2

clock = pygame.time.Clock()
fps = 60
dt = 0
clock.tick()

done = False # loop control

while not done:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT:
			done = True # ends loop. game exit	
			
	screen.blit(background_image, [0, 0])
	sprite_load("image/Egg/?.png")
	Sprite_cycle = Sprite_iter.next()
	screen.blit((Sprite_cycle), (Digimon_x_pos, Digimon_y_pos))	
	pygame.display.flip() # shows screen fill.


	pygame.display.flip() # shows screen fill.
	clock.tick(fps) # Limit to 60 frames per second
pygame.quit()





























