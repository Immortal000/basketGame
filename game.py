import pygame
import random
import string
characters = string.ascii_lowercase+string.digits+string.punctuation
basket_numbers = string.digits 
basket_alphabets = string.ascii_lowercase
basket_punc = string.punctuation

'''a = alphabets  
n = numbers       
p = punctuation'''
pygame.init() 

background = (0,0,0)
red = (255,0,0)
white = (255,255,255)

X = 600
Y = 400
speed = 0
points = 0 
def generate_word(): 
	global comp_word, u_word, word_x, word_y, text, point_note, speed,choice
	word_x = random.randint(100,500)
	word_y = 0 
	speed += 0.005
	comp_word = random.choice(characters)
	if comp_word in basket_alphabets: 
		choice = 'a'
	elif comp_word in basket_numbers:
		choice = 'n'
	elif comp_word in basket_punc:
		choice = 'p'
	text = font.render(comp_word,True,white)
	u_word = ""

win = pygame.display.set_mode((X,Y))
pygame.display.set_caption('Typing game')
font = pygame.font.SysFont("Garamond",32)
generate_word()
while True: 
	win.fill(background)
	word_y += speed 

	win.blit(text,(word_x,word_y))
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
		    pygame.quit()
		    quit()
		elif event.type==pygame.KEYDOWN:
                    if pygame.key.name(event.key) == choice:
                        points = points + 3
                        generate_word()
                    else:
                        points = points - 3
                        generate_word()
	point_note = font.render(str(points),True,red)
	win.blit(point_note,(10,5))
	pygame.draw.rect(win, (100, 100, 150),((150, 150), (100, 100)),3)
	pygame.display.update()


