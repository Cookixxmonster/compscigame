'''
Created on Jun 1, 2015

@author: Marina K
'''

import pygame.key;
from globals import globals
from room import rooms



currentDudeImage = 0;
currentDudeImageDelta = 0;

dudeImages = [
    pygame.image.load('images/move/tmp-01.png'),
    pygame.image.load('images/move/tmp-110.png'),
    pygame.image.load('images/move/tmp-21.png'),
    pygame.image.load('images/move/tmp-31.png'),
    pygame.image.load('images/move/tmp-41.png'),
    pygame.image.load('images/move/tmp-51.png'),
    pygame.image.load('images/move/tmp-61.png'),
    pygame.image.load('images/move/tmp-71.png'),
    pygame.image.load('images/move/tmp-81.png'),
    pygame.image.load('images/move/tmp-91.png'),
    pygame.image.load('images/move/tmp-101.png'),
    pygame.image.load('images/move/tmp-111.png')
]


'''
Process keyboard events
'''
def processMouse (event):
    print (event);

    #call room logic if any
    roomDef=rooms.getCurrentRoom();
    if ('roomLogic' in roomDef):
        roomDef['roomLogic'] (event, rooms.getCurrentRoom ());

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

    print ("X/Y:", globals.currentXPos, globals.currentYPos);
    global currentDudeImageDelta, currentDudeImage;

    roomDef=rooms.getCurrentRoom();

    speed=globals.defaultSpeed;
    if ('speed' in roomDef):
        speed = roomDef ['speed'];

    lastHitObject = hitObject ();

    if (globals.direction == "up"):
        if (not lastHitObject):
            globals.currentYPos -= speed;
    elif (globals.direction == "down"):
        if (not lastHitObject):
            globals.currentYPos += speed;
    elif (globals.direction == "left"):
        if (not lastHitObject):
            globals.currentXPos -= speed;
    elif (globals.direction == "right"):
        if (not lastHitObject):
            globals.currentXPos += speed;

    #draw rectangle for now
    #pygame.draw.rect(rooms.screen, (255,255,0), (globals.currentXPos,globals.currentYPos, 100, 100), 0)
    globals.screen.blit(dudeImages [currentDudeImage],(globals.currentXPos,globals.currentYPos));
    currentDudeImageDelta += 1;


    if (currentDudeImageDelta > 3):
        currentDudeImageDelta = 0;
        currentDudeImage += 1;
        if (currentDudeImage > 10):
            currentDudeImage = 0;


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


            #it coule be overridden in room data
            if ('startX' in roomDef):
                globals.currentXPos=roomDef ['startX'];
            if ('startY' in roomDef):
                globals.currentYPos=roomDef ['startY'];
            if ('startMovement' in roomDef):
                globals.direction=roomDef ['startMovement'];

            print ("Got to another room !!!", globals.currentRoom);

    #print (globals.currentYPos, '-', globals.currentYPos, '-', globals.direction)



'''
Check if the main character can move further
'''
def hitObject ():
    roomDef=rooms.getCurrentRoom();
    roomObjects=roomDef['objects'];
    delta = 5;

    testValue=155;

    for roomObject in roomObjects:
        #print (roomObject);

        roomDimensions = roomObject ['dimension'];
        x,y,width,height=roomDimensions;

        if (globals.direction == "up"):
            #test upper side
            for testX in range (globals.currentXPos, globals.currentXPos + testValue):
                if (testX >= x and testX <= x + width and globals.currentYPos - delta > y  and globals.currentYPos - delta < y + height):
                    return roomObject;
        elif (globals.direction == "right"):
            #test right side
            for testY in range (globals.currentYPos, globals.currentYPos + testValue):
                if (globals.currentXPos + testValue >= x and globals.currentXPos + testValue <= x + width and testY >= y and testY <= y + height):
                    return roomObject;
        elif (globals.direction == "left"):
            #test left side
            for testY in range (globals.currentYPos, globals.currentYPos + testValue):
                if (globals.currentXPos - delta >= x and globals.currentXPos - delta <= x + width and testY >= y and testY <= y + height):
                    return roomObject;
        elif (globals.direction == "down"):
            #test bottom side
            for testX in range (globals.currentXPos, globals.currentXPos + testValue):
                if (testX >= x and testX <= x + width and globals.currentYPos + testValue >= y and globals.currentYPos + testValue <= y + height):
                    return roomObject;

    return False;