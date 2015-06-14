'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals
import pygame

'''
Logic pertaining to various events in room5
'''
def roomLogicFunction (object, roomObject) :
    return 0;
angerApproached = False; 

bubbleImage=pygame.image.load('images/room3/Textbubble.png');
angerPosition = (450,350);
angerBubblePosition = (400,300);
angerMessages=["Would you like some grits?"];
angerCurrentMessage = 0;


def isPersonCloseToanger ():
    
    global angerPosition;
    
    x = globals.currentXPos;
    y =  globals.currentYPos;
    
    #that's where the anger is
    rect = pygame.Rect (angerPosition [0], angerPosition [1], 350, 350);
    
    #check each point in the square when the walking man is
    for i in range (x, x + 100):
        for j in range (y, y + 100):
            if (rect.collidepoint (i, j)):
                return True;


'''
Logic pertaining to various events in room4
'''
def roomLogicFunction (object, roomObject) :
    
    
                
    global angerApproached, bubbleImage, angerPosition;
    global angerMessages, angerCurrentMessage;
    global roomData;
    
    
    if (not angerApproached and isPersonCloseToanger ()):
        angerApproached = True;      
        globals.direction="stand";
        
    #check if bubble needs to be drawn
    if (angerApproached):
            
        #draw bubble
        globals.screen.blit (bubbleImage, angerBubblePosition);
            
        #draw current question
        globals.drawLabel(angerBubblePosition [0] + 15, angerBubblePosition [1] + 15, angerMessages [angerCurrentMessage])


#room description
roomData = {
    'name':"Anger World",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/angry background.png',
    'speed': 8,
    'roomLogic':roomLogicFunction,
    'objects':[
               {
                'name':'door',
                'dimension' : (0, globals.screenHeight-150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':3,
                'exitTo':'left'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight - 150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':5,
                'exitTo':'right'
               },
               {
                'name':'anger',
                'data' : pygame.image.load('images/anger1.png'),
                'dimension' : (450, globals.screenHeight-310, 0, 0),
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
