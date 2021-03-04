import pygame # imports pygame library
pygame.init() # starts up pygame library
import random

screen = pygame.display.set_mode((700, 500)) # creates display called screen 700x500
pygame.display.set_caption("This means WAR") # sets the title of the window

doExit = False # gameloop variable
clock = pygame.time.Clock() # the clock

font = pygame.font.Font('freesansbold.ttf', 32)

turn = False


class card: # creates class card
    def __init__(self, suit, number): # sets up starting variables for the suit and number of a card
        self.suit = suit # puts the arguments given to the card into the classes self variables
        self.number = number
    def draw(self, x, y): # drawing function
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 180)) # draws white part of card
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 100, 180), 3) # draws black outline
        
        value = font.render(str(int(self.number)), False, (0, 0, 0)) # the actual number of the card
        screen.blit(value, (x+60,y+10))
        
        if self.suit == 0: # 0 = hearts, 1 = diamonds, 2 = clubs, 3 = spades
            text = font.render('H', False, (200, 25, 55)) # renders the suit of the card depending on its value
            screen.blit(text, (x+10,y+10))
        if self.suit == 1:
            text = font.render('D', False, (200, 25, 55))
            screen.blit(text, (x+10,y+10))
        if self.suit == 2:
            text = font.render('C', False, (25, 25, 25))
            screen.blit(text, (x+10,y+10))
        if self.suit == 3:
            text = font.render('S', False, (25, 25, 25))
            screen.blit(text, (x+10,y+10))
            
deck = list() # creates lIsT(array) called deck
for j in range(4):
    for i in range(13):
        deck.append(card(j,i))
random.shuffle(deck) # randomizes the deck / shuffles

p1hand = list()
p2hand = list()
p1Discard = list()
p2Discard = list()

for i in range(26):
    p1hand.append(deck[i])
for j in range(26,52):
    p2hand.append(deck[j])

while not doExit: # loop ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    clock.tick(60) # ticks clock at 60 times per second

    queue = pygame.event.wait() # event queue
    
    if queue.type == pygame.QUIT: # if the event is quit(red x)
        doExit = True # exit game loop

    if queue.type == pygame.MOUSEBUTTONDOWN: # if mouse is clicked
        turn = True

    if queue.type == pygame.MOUSEBUTTONUP: # checks if mouse isn't clicked
        turn = False
    
    if queue.type == pygame.MOUSEMOTION: # checks for mouse position
        mousePos = queue.pos # sets mouse position into mousePos

    # game logic -----------------------------------------------------

    if turn == True and len(p1hand) > 0 and len(p2hand) > 0:

    if p1hand[len(p1hand)]-1 > len(p2hand):

    # render --------------------------------------------------------------------------
    screen.fill((50,205,50)) # fills the screen to black every frame

    for i in range(0,len(p1hand)):
        p1hand[i].draw(100,50)

    for i in range(0,len(p2hand)):
        p2hand[i].draw(300,50)

    for i in range(0,len(p1Discard)):
        p1Discard[i].draw(100, 200)
    for i in range(0,len(p2Discard)):
        p2Discard[i].draw(300, 200)

    
    #for i in range(52): # goes through 
    #    card.draw(deck[i], 20 + i*5, 20+i*3)
    
    pygame.display.flip() # puts the memory onto the actual screen
    # end loop ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

pygame.quit() # quits pygame
