'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals
import pygame;


currentchestImage = 0;
currentchestImageDelta = 0;


chestImages = [
    pygame.image.load('images/chest/chest-0.png'),
    pygame.image.load('images/chest/chest-1.png'),
    pygame.image.load('images/chest/chest-2.png'),
    pygame.image.load('images/chest/chest-3.png'),
    pygame.image.load('images/chest/chest-4.png'),
    pygame.image.load('images/chest/chest-5.png'),
    pygame.image.load('images/chest/chest-6.png'),
    pygame.image.load('images/chest/chest-7.png'),
    pygame.image.load('images/chest/chest-8.png'),
    pygame.image.load('images/chest/chest-9.png'),
    pygame.image.load('images/chest/chest-10.png'),
    pygame.image.load('images/chest/chest-11.png'),
    pygame.image.load('images/chest/chest-12.png'),
    pygame.image.load('images/chest/chest-13.png'),
    pygame.image.load('images/chest/chest-14.png'),
    pygame.image.load('images/chest/chest-15.png'),
    pygame.image.load('images/chest/chest-16.png'),
    pygame.image.load('images/chest/chest-17.png')
]

def roomLogicFunction (object, roomObject) :

    #draw chest
    global chest, currentchestImageDelta, currentchestImage;

    globals.screen.blit(chestImages [currentchestImage],(450,150));

    currentchestImageDelta += 1;


    if (currentchestImageDelta > 15):
        currentchestImageDelta = 0;

        if (currentchestImage < len (chestImages) - 1):
            currentchestImage += 1;


    print ("DDDDDDDDDD", currentchestImage)



#room description
roomData = {
    'name':"Room with chest of memories",
    'backgroundColor': (0, 155, 225),
    'speed': 8,
    'roomLogic':roomLogicFunction,
    'objects':[
               {
                'name':'door',
                'dimension' : (0, globals.screenHeight/2 - 100, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':9,
                'exitTo':'left'
               }
    ]
}
