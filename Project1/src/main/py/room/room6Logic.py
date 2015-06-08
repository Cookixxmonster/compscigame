'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals

'''
Logic pertaining to various events in room6
'''
def roomLogicFunction (object, roomObject) :
    return 0;


#room description
roomData = {
    'name':"Door To Hallway",
    'startX':globals.screenWidth/2 - 50,
    'startY':globals.screenHeight - 200,
    'startMovement':'stand',
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Hallway Door.jpg',
    'speed':5,
    'roomLogic':roomLogicFunction,
    'objects':[
               {
                'name':'door',
                'dimension' : (globals.screenWidth/2 - 50, globals.screenHeight-50, 150, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':4,
                'exitTo':'down'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth/2 - 110, globals.screenHeight/2, 220, 50),
                'shape':'rect',
                'backgroundColor':(255, 0, 100),
                'toRoom':6,
                'exitTo':'up'
               }
    ]
}
