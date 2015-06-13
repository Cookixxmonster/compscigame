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
    'speed': 8,
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
                'dimension' : (-250, globals.screenHeight-550, 0, 0),
                'shape':'image'
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
