'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals

'''
Logic pertaining to various events in room8
'''
def roomLogicFunction (object, roomObject) :
    return 0;


#room description
roomData = {
    'name':"Gluttony",
    'speed':10,
    'startX':50,
    'startY':350,
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Gluttony.jpg',
    'roomLogic':roomLogicFunction,
    'objects':[

               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight/2 - 100, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':11,
                'exitTo':'right'
               }
    ]
}
