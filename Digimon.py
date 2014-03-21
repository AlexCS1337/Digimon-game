import pygame # Import library of functions called 'pygame'
from pygame.time import Clock
import random
import time
import itertools
import pygame, os 
os.environ['SDL_VIDEO_CENTERED'] = '1'

class Digimon(object):
	def __init__(self,age,weight,strength,defence,speed,intelligence):
		self.age = age 	
		self.weight = weight 	
		self.strength = strength 
		self.defence = defence 	
		self.speed = speed 	
		self.intelligence = intelligence 
		
############################ GET PLAYER STATS FROM FILE TO CREATE OBJECT##############################

def create_file(): # creates Digimon_stats.txt if not exist
	if os.path.isfile("Digimon_stats.txt"):
		pass
	else:
		open("Digimon_stats.txt", "a")
		write_stats = open("Digimon_stats.txt", "w")
		write_stats.write("0,2,0,0,0,0") # if no text, then write basic stats to file
		write_stats.close()

create_file()

f = open("Digimon_stats.txt", "r") 
data = f.read()

string_list = data.split(',')
integer_list = []

for string_item in string_list:
	integer_list.append(int(string_item))
 
age, weight, strength, defence, speed, intelligence = integer_list
 
Player = Digimon(age, weight, strength, defence, speed, intelligence) 

############################ EGG OBJECT #################################

# Egg = Digimon(0,2,0,0,0,0) 
# Egg_idle = [pygame.image.load("images/egg_sprite_1.png"), pygame.image.load("images/egg_sprite_2.png"), pygame.image.load("images/egg_sprite_3.png") ]

# Egg_sprites = itertools.cycle(Egg_idle) # cycles through egg images

############################ LEAFMON OBJECT ##############################

Leafmon_right = [pygame.image.load("images/leaf_1.png"), pygame.image.load("images/leaf_2.png"), pygame.image.load("images/leaf_3.png"), pygame.image.load("images/leaf_4.png")]

Leafmon_sprites = itertools.cycle(Leafmon_right) # cycles through egg images

############################ INITIALISE GAME ENGINE ##############################
pygame.init() 
 
[screen_width, screen_height] = [425,175]
screen = pygame.display.set_mode([screen_width,screen_height])
 
black = (  0,  0,  0) # defines colours for ease of use
white = (255,255,255)
red = (255,0,0)

clock = pygame.time.Clock() # controls how fast the game runs
elapsed = 0.

pygame.display.set_caption('Digimon Simulator 1   %d fps' % clock.get_fps())
 
font = pygame.font.Font(None, 15)

Digimon_x_pos = 160
Digimon_y_pos = 50

done = False # loop control

draw_egg=False
draw_Leafmon= False



############################ Main Program Loop #################################
while not done:
	counter = 0

############################ ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT #################################
	for event in pygame.event.get():	# User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # exits the loop 
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos # gets the x, y position of the mouse click
			if ( x  in range(150,170)) and ( y in range(10,30)): # if in range, add age +1 to player
				Player.age += 1
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos # gets the x, y position of the mouse click
			if ( x  in range(175,195)) and ( y in range(10,30)): # if in range, add age +1 to player
				Player.weight += 1
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos # gets the x, y position of the mouse click
			if ( x  in range(200,220)) and ( y in range(10,30)): # if in range, add age +1 to player
				Player.strength += 1
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos # gets the x, y position of the mouse click
			if ( x  in range(225,245)) and ( y in range(10,30)): # if in range, add age +1 to player
				Player.defence += 1
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos # gets the x, y position of the mouse click
			if ( x  in range(250,275)) and ( y in range(10,30)): # if in range, add age +1 to player
				Player.speed += 1
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos # gets the x, y position of the mouse click
			if ( x  in range(275,295)) and ( y in range(10,30)): # if in range, add age +1 to player
				Player.intelligence += 1
				
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos # gets the x, y position of the mouse click
			if ( x  in range(300,320)) and ( y in range(10,30)): # if in range, add age +1 to player
				age_stat,weight_stat,strength_stat,defence_stat,speed_stat,intelligence_stat = Player.age, Player.weight, Player.strength, Player.defence, Player.speed, Player.intelligence 
				f = open('Digimon_stats.txt',"w")
				f.write(str(age_stat) + "," + str(weight_stat) + "," + str(strength_stat) + "," + str(defence_stat) + "," + str(speed_stat) + "," + str(intelligence_stat))
				f.close() 
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos # gets the x, y position of the mouse click
			if ( x  in range(320,350)) and ( y in range(10,30)):
				Player = Digimon(0,2,0,0,0,0) # returns stats to original (Egg)
				
############################ ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT #################################
	screen.fill((white))
	
	
	
	
	Leafmon_sprites_next = Leafmon_sprites.next() # sets it up to cycle through leafmon images
		
	if Player.age == 2 and Player.speed >= 2 and Player.intelligence >= 5: 
		# and Player.defence == 5 and Player.speed == 5 and Player.intelligence == 5: 
			# draw_egg = False # draws Egg (refer to below for the command)		
		draw_egg = False
		draw_Leafmon = True
	# else:
		# draw_egg = True # draws Egg (refer to below for the command)
		# draw_Leafmon = False 
	
	
	n = random.randint (0,1000)	
	p = random.randint(1,4) # 1,2,3, 4
	if n < 1:
		for x in range(0, p):
			Digimon_x_pos -= 1 
            
	elif n > 970:
		for x in range(0, p):
			Digimon_x_pos += 1
			
			print Digimon_x_pos
	
	elif Digimon_x_pos >= 340: 
# 	or Digimon_x_pos <= 0:
		for x in range(0,5):
			Digimon_x_pos -= 1 
		
############################ ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT #################################

############################ ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT #################################

	Age_button = pygame.draw.rect(screen, black, [150,10, 20,20], 0) # [x,y top left point, width, height], how wide the line around the rectangle is. If 0, rect is filled.
	
	Weight_button = pygame.draw.rect(screen, black, [175,10, 20,20], 0) # [x,y top left point, width, height], how wide the line around the rectangle is. If 0, rect is filled.
	
	Strength_button = pygame.draw.rect(screen, black, [200,10, 20,20], 0) # [x,y top left point, width, height], how wide the line around the rectangle is. If 0, rect is filled.
	
	Defence_button = pygame.draw.rect(screen, black, [225,10, 20,20], 0) # [x,y top left point, width, height], how wide the line around the rectangle is. If 0, rect is filled.
	
	Speed_button = pygame.draw.rect(screen, black, [250,10, 20,20], 0) # [x,y top left point, width, height], how wide the line around the rectangle is. If 0, rect is filled.
	
	Intelligence_button = pygame.draw.rect(screen, black, [275,10, 20,20], 0) # [x,y top left point, width, height], how wide the line around the rectangle is. If 0, rect is filled.
	
	Save_button = pygame.draw.rect(screen, black, [300,10, 20,20], 0) # [x,y top left point, width, height], how wide the line around the rectangle is. If 0, rect is filled.
	
	reset_button = pygame.draw.rect(screen, red, [325,10, 20,20], 0) # [x,y top left point, width, height], how wide the line around the rectangle is. If 0, rect is filled.
		
	if draw_Leafmon:
		
				screen.blit((Leafmon_sprites_next), (Digimon_x_pos,Digimon_y_pos))
		
	else: 
		pass 
		
		
	Player_age_text    = font.render("Player Age " + str(Player.age), True, black) # font uses the font fuction above, (what to draw, anti-alias, colour)
	Player_weight_text = font.render("Player Weight " + str(Player.weight), True, black)
	Player_strength_text = font.render("Player Strength " + str(Player.strength), True, black)
	Player_defence_text = font.render("Player Defence " + str(Player.defence), True, black)
	Player_speed_text = font.render("Player Speed " + str(Player.speed), True, black)
	Player_intelligence_text = font.render("Player Intelligence " + str(Player.intelligence), True, black)
	
	screen.blit(Player_age_text, [10, 10])
	screen.blit(Player_weight_text, [10, 20])
	screen.blit(Player_strength_text, [10, 30])
	screen.blit(Player_defence_text, [10, 40])
	screen.blit(Player_speed_text, [10, 50])
	screen.blit(Player_intelligence_text, [10, 60])
	

	pygame.display.flip() # shows screen fill.
	
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
	clock.tick(5) # Limit to 20 frames per second
	
pygame.quit()