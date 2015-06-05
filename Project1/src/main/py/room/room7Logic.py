'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals

'''
Logic pertaining to various events in room7
'''
def roomLogicFunction (object, roomObject) :
    return 0;


#room description
roomData = {
    'name':"Choose a sin",
    'startX':50,
    'startY':350,
    'backgroundColor': (0, 155, 225),
    'roomLogic':roomLogicFunction,
    'objects':[
               {
                'name':'door',
                'dimension' : (globals.screenWidth-globals.doorWidth, globals.screenHeight/3-80 , 50, 150),
                'shape':'rect',
                'backgroundColor':(255, 0, 0),
                'toRoom':7,
                'exitTo':'right'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight/2 + 50, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 0),
                'toRoom':8,
                'exitTo':'right'
               },
               {
                'name':'door',
                'dimension' : (0, globals.screenHeight/3-80 , 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 0, 255),
                'toRoom':9,
                'exitTo':'left'
               },
               {
                'name':'door',
                'dimension' : (0, globals.screenHeight/2 + 50, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 0, 0),
                'toRoom':10,
                'exitTo':'left'
               }


    ]
}
