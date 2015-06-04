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
    'name':"Room6",
    'startX':50,
    'startY':350,
    'backgroundColor': (0, 155, 225),
    'roomLogic':roomLogicFunction,
    'objects':[
               {
                'name':'door',
                'dimension' : (0, globals.screenHeight/2 - 100, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':4,
                'exitTo':'left'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth/2 - 50, 0, 150, 50),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':6,
                'exitTo':'up'
               }
    ]
}
