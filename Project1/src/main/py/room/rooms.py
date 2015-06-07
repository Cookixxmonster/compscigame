'''
Created on Jun 1, 2015

@author: Marina K
'''

import pygame;

from room import room1Logic;
from room import room2Logic;
from room import room3Logic;
from room import room4Logic;
from room import room5Logic;
from room import room6Logic;
from room import room7Logic;
from room import room8Logic;
from room import room9Logic;
from room import room10Logic;
from room import room11Logic;
from room import room12Logic;
from room import room13Logic;
from globals import globals


#define screen
globals.screen = pygame.display.set_mode((globals.screenWidth, globals.screenHeight));
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
   room11Logic.roomData,
   room12Logic.roomData,
   room13Logic.roomData

]

'''
Draw room
'''
def drawRoom ():


    roomObj=roomData [globals.currentRoom];

    globals.screen.fill (roomObj ['backgroundColor'])

    if ('backgroundImage' in roomObj):
        if (not 'backgroundImageLoaded' in roomObj):
            bg = pygame.image.load(roomObj ['backgroundImage']);
            roomObj ['backgroundImageLoaded'] = bg;

        globals.screen.blit(roomObj ['backgroundImageLoaded'],(0, 0));

    #Room title
    font=pygame.font.SysFont("monospace", 15);
    label = font.render(roomObj['name'], 1, (0,0,0))
    globals.screen.blit(label, (400, 10))

    #Room objects
    for object in roomObj['objects']:
        drawObject (globals.screen, object);


'''
Draw room object
'''
def drawObject (screen, object):

    #get shape type
    shape=object['shape'];

    #for different shape types draw different shapes
    if (shape == 'rect'):
        pygame.draw.rect(screen, object['backgroundColor'], object ['dimension'], 0)

    if (shape == 'label'):
        font=pygame.font.SysFont("monospace", object['size'], 700);
        label = font.render(object['text'], 10, object['color'])
        globals.screen.blit(label, (object ['dimension'] [0], object ['dimension'][1]))

    if (shape == 'image'):
        globals.screen.blit (object ['data'], (object ['dimension'] [0], object ['dimension'][1]));


'''
Get current room definition
'''
def getCurrentRoom ():
    return roomData [globals.currentRoom];