'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals
import pygame

'''
Logic pertaining to various events in room5
'''
def roomLogicFunction (object, roomObject) :
    return 0;


#room description
roomData = {
    'name':"Anger World",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/angry background.png',
    'speed': 8,
    'roomLogic':roomLogicFunction,
    'objects':[
               {
                'name':'door',
                'dimension' : (0, globals.screenHeight-150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':3,
                'exitTo':'left'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight - 150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':5,
                'exitTo':'right'
               },
               {
                'name':'anger',
                'data' : pygame.image.load('images/anger1.png'),
                'dimension' : (450, globals.screenHeight-310, 0, 0),
                'shape':'image'
                }
    ]
}
