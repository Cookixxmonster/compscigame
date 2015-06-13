'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals

'''
Logic pertaining to various events in room10
'''
def roomLogicFunction (object, roomObject) :
    return 0;


#room description
roomData = {
    'name':"Greed",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Greed.jpg',
    'speed': 8,
    'roomLogic':roomLogicFunction,
    'objects':[

               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight/2 - 100, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':11,
                'exitTo':'right'
               },
               {
                'name':'leftwall',
                'dimension' : (5, 0, 2, globals.screenHeight),
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
