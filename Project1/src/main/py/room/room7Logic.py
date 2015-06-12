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
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Hallway2.jpg',
    'roomLogic':roomLogicFunction,
    'speed':5,
    'objects':[
               {
                'name':'door',
                'dimension' : (globals.screenWidth - 80, globals.screenHeight/3-80 , 350, 450),
                'shape':'door',
                'backgroundColor':(255, 0, 0),
                'toRoom':7,
                'exitTo':'right'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-225, globals.screenHeight/2 - 130, 40, 60),
                'shape':'door',
                'backgroundColor':(0, 255, 0),
                'toRoom':8,
                'exitTo':'right'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-670, globals.screenHeight/2 - 120 , 45, 60),
                'shape':'door',
                'backgroundColor':(0, 0, 255),
                'toRoom':9,
                'exitTo':'left'
               },
               {
                'name':'door',
                'dimension' : (0, globals.screenHeight/2 - 200, 50, 400),
                'shape':'door',
                'backgroundColor':(0, 0, 0),
                'toRoom':10,
                'exitTo':'left'
               }


    ]
}
