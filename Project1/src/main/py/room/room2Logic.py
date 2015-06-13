'''
Created on Jun 1, 2015

@author: Marina K
'''

from globals import globals

'''
Logic pertaining to various events in room2
'''
def roomLogicFunction (object, roomObject) :
    return 0;


#room description
roomData = {
    'name':"Go into Machine",
    'backgroundColor': (255, 255, 255),
    'backgroundImage' : 'images/Second Room.jpg',
    'roomLogic':roomLogicFunction,
    'speed': 8,
    'objects':[
               #define borders
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
               },
              
               {
                'name':'door',
                'dimension' : (globals.screenWidth-150, globals.screenHeight - 500, 100, 250),
                'shape':'machinedoor',
                'backgroundColor':(0, 255, 100),
                'toRoom':2,
                'exitTo':'right'
               }
    ]
}
