'''
Created on Jun 1, 2015

@author: Marina K
'''

import pygame;
import sys;

from room import rooms
from movement import movement
from globals import globals



pygame.init();

while (True):

    # check for quit and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

        #process keyboard input
        if event.type == pygame.KEYDOWN:
            movement.processInput (event);

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


