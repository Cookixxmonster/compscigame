'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals
import pygame

'''
Logic pertaining to various events in room4
'''
def roomLogicFunction (object, roomObject) :
    return 0;


#room description
roomData = {
    'name':"Sad World",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/sad image.png',
    'roomLogic':roomLogicFunction,
    'objects':[
             {
                'name':'door',
                'dimension' : (0, globals.screenHeight-150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':2,
                'exitTo':'left'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight - 150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':4,
                'exitTo':'right'
               },
               {
                'name':'sadness',
                'data' : pygame.image.load('images/Sadness.png'),
                'dimension' : (-450, -200, 0, 0),
                'shape':'image'
                }
    ]
}
