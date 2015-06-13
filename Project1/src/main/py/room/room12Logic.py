'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals
import pygame

SpiderImage = [
    pygame.image.load('images/Spider.png'),
    
]
    
currentSpiderImage = 0;
currentSpiderImageSpeed = 0;
'''
Logic pertaining to various events in room11
'''
def roomLogicFunction (object, roomObject) :

    #draw Spider
    global Spider, currentSpiderImageSpeed, currentSpiderImage;

    globals.screen.blit(SpiderImage [currentSpiderImage],(450,350));

    currentSpiderImageSpeed += 1;


    if (currentSpiderImageSpeed > 2):
        currentSpiderImageSpeed = 0;

        currentSpiderImage += 1;
        if (currentSpiderImage > len (SpiderImage) - 1):
            currentSpiderImage = 0;


    print ("DDDDDDDDDD", currentSpiderImage)




#room description
roomData = {
    'name':"Fight Room",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Evil Room.png',
    'speed': 8,
    'roomLogic':roomLogicFunction,
    'startX':400,
    'startY':500,
    'startMovement':'none',
    'objects':[
              {
                'name':'door',
                'dimension' : (globals.screenWidth - 50, globals.screenHeight/2 - 100, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':12,
                'exitTo':'right'
               },
               {
                'name':'spider',
                'data' : pygame.image.load('images/Spider1.png'),
                'dimension' : (-450, -200, 0, 0),
                'shape':'image',
                'startX': 950,
                'startY':670
                }

    ]
}
