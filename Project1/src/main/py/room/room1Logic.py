'''
Created on Jun 1, 2015

@author: Marina K
'''

from globals import globals

#keep # of hits for each maze wall
hitCount={};

#initial left coordinate
leftMazeX=120;

'''
Logic pertaining to various events in room1
'''
def roomLogicFunction (object, roomObject) :
    global hitCount,leftMazeX;


#room description
roomData = {
    'name':"Intro",
    'backgroundColor': (169, 207, 235),
    'roomLogic':roomLogicFunction,
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
                'dimension' : (globals.screenWidth-50, globals.screenHeight - 150, globals.screenWidth, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':1,
                'exitTo':'right'
               }
     ]
   }

