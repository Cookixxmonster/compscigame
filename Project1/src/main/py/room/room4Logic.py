'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals
import pygame

sadnessApproached = False; 

bubbleImage=pygame.image.load('images/room3/Textbubble.png');
sadnessPosition = (450,350);
sadnessBubblePosition = (400,300);
sadnessMessages=["Riddle Goes Here"];
sadnessCurrentMessage = 0;


def isPersonCloseToSadness ():
    
    global sadnessPosition;
    
    x = globals.currentXPos;
    y =  globals.currentYPos;
    
    #that's where the sadness is
    rect = pygame.Rect (sadnessPosition [0], sadnessPosition [1], 350, 350);
    
    #check each point in the square when the walking man is
    for i in range (x, x + 100):
        for j in range (y, y + 100):
            if (rect.collidepoint (i, j)):
                return True;


'''
Logic pertaining to various events in room4
'''
def roomLogicFunction (object, roomObject) :
    
    
                
    global sadnessApproached, bubbleImage, sadnessPosition;
    global sadnessMessages, sadnessCurrentMessage;
    global roomData;
    
    
    if (not sadnessApproached and isPersonCloseToSadness ()):
        sadnessApproached = True;      
        globals.direction="stand";
        
    #check if bubble needs to be drawn
    if (sadnessApproached):
            
        #draw bubble
        globals.screen.blit (bubbleImage, sadnessBubblePosition);
            
        #draw current question
        globals.drawLabel(sadnessBubblePosition [0] + 15, sadnessBubblePosition [1] + 15, sadnessMessages [sadnessCurrentMessage])





#room description
roomData = {
    'name':"Sad World",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/sad image.png',
    'speed': 8,
    'roomLogic':roomLogicFunction,
    'objects':[
             {
                'name':'door',
                'dimension' : (0, globals.screenHeight-150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':2,
                'exitTo':'left'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight - 150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':4,
                'exitTo':'right'
               },
               {
                'name':'sadness',
                'data' : pygame.image.load('images/Sadness.png'),
                'dimension' : (450,350, 0, 0),
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
