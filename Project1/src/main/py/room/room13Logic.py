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

    globals.screen.blit(chestImages [currentchestImage],(250,150));

    currentchestImageDelta += 1;


    if (currentchestImageDelta > 7):
        currentchestImageDelta = 0;

        if (currentchestImage < len (chestImages) - 1):
            currentchestImage += 1;
            



#room description
roomData = {
    'name':"Room with chest of memories",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Memoryroom.jpg',
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
               },
               {
                'name':'leftwall',
                'dimension' : (-2, 0, 2, globals.screenHeight),
                'shape':'rect',
                'backgroundColor':(255, 0, 0)
               },
               {
                'name':'rightwall',
                'dimension' : (globals.screenWidth, 0, 2, globals.screenHeight),
                'shape':'rect',
                'backgroundColor':(0, 255, 0)
               },
               {
                'name':'topwall',
                'dimension' : (0, 0, globals.screenWidth, 2),
                'shape':'rect',
                'backgroundColor':(0, 0, 255)
               },
               {
                'name':'bottomwall',
                'dimension' : (0, globals.screenHeight-2, globals.screenWidth, globals.screenHeight),
                'shape':'rect',
                'backgroundColor':(0, 0, 0)
               }
    ]
}
