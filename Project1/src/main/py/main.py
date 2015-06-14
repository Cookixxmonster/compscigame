'''
Created on Jun 1, 2015

@author: Marina K
'''

import pygame;
import sys;

from room import rooms
from movement import movement
from globals import globals

startScreen= True
    



pygame.init();
startImage = pygame.image.load ('images/Start Screen.png');

while (startScreen):
    
    globals.screen.blit (startImage, (0, 0));
    pygame.display.update()

    # check for quit and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

        #process keyboard input
        if event.type == pygame.KEYDOWN  and event.key == pygame.K_RETURN:
            startScreen = False;

instructionImage = pygame.image.load ('images/Instructions.jpg');

instructionScreen = True;

while (instructionScreen):
    
    globals.screen.blit (instructionImage, (0, 0));
    pygame.display.update()

    # check for quit and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

        #process keyboard input
        if event.type == pygame.KEYDOWN  and event.key == pygame.K_RETURN:
            instructionScreen = False;


while (True):
    

    # check for quit and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

        #process keyboard input
        if event.type == pygame.KEYDOWN:
            movement.processInput (event);

        if event.type == pygame.MOUSEBUTTONDOWN:
            movement.processMouse (event);

    #draw room
    rooms.drawRoom ();

    #move character
    movement.moveCharacter ();

    #call room logic
    roomDef=rooms.getCurrentRoom();
    if ('roomLogic' in roomDef):
        roomDef['roomLogic'] ("", roomDef);

    #update screen
    pygame.display.update()


