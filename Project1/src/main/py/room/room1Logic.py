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

    #print ("Room1 logic called for room:", roomObject);

    #if object's hit, store its id
    if (isinstance (object, dict)):
        if (object['name'] == 'mazeWall'):
            hitCount [object['id']] = True;

    #if all 3 maze walls were hit, move the left one back
    if (1 in hitCount and 2 in hitCount and 3 in hitCount):
        leftMazeX -= 1;

    #make sure if's not flying off the screen
    if (leftMazeX < 20):
        leftMazeX = 20;

    #find object #4 and change its whole dimensions, since it's immutable
    roomObject['objects'][4]['dimension'] = (leftMazeX, 110, 20, globals.screenHeight - 230);


#room description
roomData = {
    'name':"Find second room",
    'backgroundColor': (169, 207, 235),
    'startX':550,
    'startY':550,
    'roomLogic':roomLogicFunction,
    'objects':[
               #define borders
               {
                'name':'leftwall',
                'dimension' : (0, 0, 2, globals.screenHeight),
                'shape':'rect',
                'backgroundColor':(255, 0, 0)
               },
               {
                'name':'rightwall',
                'dimension' : (globals.screenWidth -2, 0, 2, globals.screenHeight),
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
                'id':1,
                'name':'mazeWall',
                'dimension' : (leftMazeX, 110, 20, globals.screenHeight - 230),
                'shape':'rect',
                'backgroundColor':(1, 1, 1)
               },
               {
                'id':2,
                'name':'mazeWall',
                'dimension' : (240, 500, globals.screenWidth-300, 20),
                'shape':'rect',
                'backgroundColor':(100, 100, 100)
               },
               {
                'id':3,
                'name':'mazeWall',
                'dimension' : (240, 200, globals.screenWidth-300, 20),
                'shape':'rect',
                'backgroundColor':(100, 100, 100)
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight/2 - 100, globals.screenWidth, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':1,
                'exitTo':'right'
               }
     ]
   }

