'''
Created on Jun 1, 2015

@author: Marina K
'''

import pygame.key;
from globals import globals
from room import rooms
'''
Process keyboard events
'''
def processInput (event):
    #print (event);

    if (event.key == pygame.K_UP):
        globals.direction="up"
    elif (event.key == pygame.K_DOWN):
        globals.direction="down"
    elif (event.key == pygame.K_RIGHT):
        globals.direction="right"
    elif (event.key == pygame.K_LEFT):
        globals.direction="left"
    elif (event.key == pygame.K_SPACE):
        globals.direction="none"

    #call room logic if any
    roomDef=rooms.getCurrentRoom();
    if ('roomLogic' in roomDef):
        roomDef['roomLogic'] (event, rooms.getCurrentRoom ());

'''
Move main character
'''
def moveCharacter ():

    lastHitObject = hitObject ();

    if (globals.direction == "up"):
        if (not lastHitObject):
            globals.currentYPos -= 1;
    elif (globals.direction == "down"):
        if (not lastHitObject):
            globals.currentYPos += 1;
    elif (globals.direction == "left"):
        if (not lastHitObject):
            globals.currentXPos -= 1;
    elif (globals.direction == "right"):
        if (not lastHitObject):
            globals.currentXPos += 1;

    #draw rectangle for now
    pygame.draw.rect(rooms.screen, (255,255,0), (globals.currentXPos,globals.currentYPos, 100, 100), 0)

    #call room logic if any
    if (lastHitObject):
        roomDef=rooms.getCurrentRoom();
        if ('roomLogic' in roomDef):
            roomDef['roomLogic'] (lastHitObject, rooms.getCurrentRoom ());

    #check if it's the door
    if (lastHitObject and lastHitObject ['name'] == 'door'):
        if (globals.direction == lastHitObject['exitTo']):
            globals.currentRoom = lastHitObject ['toRoom'];

            roomDef=rooms.getCurrentRoom();

            #move the person to starting point

            if (globals.direction=="left"):
                globals.currentXPos=globals.screenWidth-150;
            elif (globals.direction=="right"):
                globals.currentXPos=50;
            elif (globals.direction=="up"):
                globals.currentYPos=globals.screenHeight - 150;
            elif (globals.direction=="down"):
                globals.currentYPos=50;

            print ("Got to another room !!!", globals.currentRoom);

    #print (globals.currentYPos, '-', globals.currentYPos, '-', globals.direction)



'''
Check if the main character can move further
'''
def hitObject ():
    roomDef=rooms.getCurrentRoom();
    roomObjects=roomDef['objects'];
    delta = 2;

    for roomObject in roomObjects:
        #print (roomObject);

        roomDimensions = roomObject ['dimension'];
        x,y,width,height=roomDimensions;

        if (globals.direction == "up"):
            #test upper side
            for testX in range (globals.currentXPos, globals.currentXPos + 100):
                if (testX >= x and testX <= x + width and globals.currentYPos - delta > y  and globals.currentYPos - delta < y + height):
                    return roomObject;
        elif (globals.direction == "right"):
            #test right side
            for testY in range (globals.currentYPos, globals.currentYPos + 100):
                if (globals.currentXPos + 100 >= x and globals.currentXPos + 100 <= x + width and testY >= y and testY <= y + height):
                    return roomObject;
        elif (globals.direction == "left"):
            #test left side
            for testY in range (globals.currentYPos, globals.currentYPos + 100):
                if (globals.currentXPos - delta >= x and globals.currentXPos - delta <= x + width and testY >= y and testY <= y + height):
                    return roomObject;
        elif (globals.direction == "down"):
            #test bottom side
            for testX in range (globals.currentXPos, globals.currentXPos + 100):
                if (testX >= x and testX <= x + width and globals.currentYPos + 100 >= y and globals.currentYPos + 100 <= y + height):
                    return roomObject;

    return False;