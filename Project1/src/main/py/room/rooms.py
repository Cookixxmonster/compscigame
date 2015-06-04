'''
Created on Jun 1, 2015

@author: Marina K
'''

import pygame;

import room1Logic;
import room2Logic;
import room3Logic;
import room4Logic;
import room5Logic;
import room6Logic;
import room7Logic;
import room8Logic;
import room9Logic;
import room10Logic;
import room11Logic;
import rooms
from globals import globals


#define screen
screen = pygame.display.set_mode((globals.screenWidth, globals.screenHeight));
pygame.display.set_caption ("Welcome to the Game")

#list of all rooms data
roomData= [
   room1Logic.roomData,
   room2Logic.roomData,
   room3Logic.roomData,
   room4Logic.roomData,
   room5Logic.roomData,
   room6Logic.roomData,
   room7Logic.roomData,
   room8Logic.roomData,
   room9Logic.roomData,
   room10Logic.roomData,
   room11Logic.roomData

]

'''
Draw room
'''
def drawRoom ():


    roomObj=roomData [globals.currentRoom];

    screen.fill (roomObj ['backgroundColor'])

    #bg = pygame.image.load(r"images\bg_room1.jpg");
    #screen.blit(bg,(0, 0))

    #Room title
    font=pygame.font.SysFont("monospace", 15);
    label = font.render(roomObj['name'], 1, (0,0,0))
    screen.blit(label, (400, 10))

    #Room objects
    for object in roomObj['objects']:
        drawObject (screen, object);


'''
Draw room object
'''
def drawObject (screen, object):

    #get shape type
    shape=object['shape'];

    #for different shape types draw different shapes
    if (shape == 'rect'):
        pygame.draw.rect(screen, object['backgroundColor'], object ['dimension'], 0)


'''
Get current room definition
'''
def getCurrentRoom ():
    return roomData [globals.currentRoom];