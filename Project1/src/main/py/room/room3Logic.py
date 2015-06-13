'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals
import pygame;


currentBananaImage = 0;
currentBananaImageSpeed = 0;


BananaImages = [
    pygame.image.load('images/Banana/tmp-0.png'),
    pygame.image.load('images/Banana/tmp-1.png'),
    pygame.image.load('images/Banana/tmp-2.png'),
    pygame.image.load('images/Banana/tmp-3.png'),
    pygame.image.load('images/Banana/tmp-4.png'),
    pygame.image.load('images/Banana/tmp-5.png'),
    pygame.image.load('images/Banana/tmp-6.png'),
    pygame.image.load('images/Banana/tmp-7.png')

]

'''
Logic pertaining to various events in room3
'''
def roomLogicFunction (object, roomObject) :

    #draw Banana
    global Banana, currentBananaImageSpeed, currentBananaImage;

    globals.screen.blit(BananaImages [currentBananaImage],(450,350));

    currentBananaImageSpeed += 1;


    if (currentBananaImageSpeed > 2):
        currentBananaImageSpeed = 0;

        currentBananaImage += 1;
        if (currentBananaImage > len (BananaImages) - 1):
            currentBananaImage = 0;


    print ("DDDDDDDDDD", currentBananaImage)



#room description
roomData = {
    'name':"Happy World",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/a-happy-place-sunrise.png',
    'speed': 8,
    'roomLogic':roomLogicFunction,
    'objects':[
               {
                'name':'door',
                'dimension' : (0, globals.screenHeight-150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':1,
                'exitTo':'left'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight - 150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':3,
                'exitTo':'right'
               }
    ]
}
