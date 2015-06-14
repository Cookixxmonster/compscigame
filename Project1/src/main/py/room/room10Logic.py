'''
Created on Jun 12, 2015

@author: Marina K
'''

import pygame;
import random;

from globals import globals


bubbleImage=pygame.image.load('images/room3/Textbubble.png');
gotItCount=0;

'''
Randomly select tails or heads
'''
def isSelectedTails () :
    return random.random () > 0.5;

'''
Logic pertaining to various events in room10
'''
def roomLogicFunction (object, roomObject) :
    
    global gotItCount, roomData;
    
    #if it's keyboard event
    if (hasattr (object, 'key')):
        print ('Room 10', object.unicode, '  ', object.key);
        
        #check if it's backspace
        
        if (object.key == pygame.K_1 or object.key == pygame.K_2):
            
            selectedTails=isSelectedTails ();
            gotIt = False;
            
            if (object.key == pygame.K_1 and selectedTails):
                gotIt = True;
                roomData['objects'][9]['text']='You got it!';     
            elif (object.key == pygame.K_2 and not selectedTails):
                gotIt = True;
                roomData['objects'][9]['text']='You got it!';
            else:
                roomData['objects'][9]['text']='You got it wrong!';     

            if (gotIt):
                gotItCount += 1;
                
            if (gotItCount > 15):    
                roomData['objects'][0]['dimension']=(globals.screenWidth-50, globals.screenHeight/2 - 100, 50, 150);     
                roomData['objects'][9]['text']='Proceed to Exit';     
                
                
            print (gotIt, " ", selectedTails);

#room description
roomData = {
    'name':"Greed",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Greed.jpg',
    'speed': 8,
    'startX':400,
    'startY':500,
    'startMovement':'stand',
    'roomLogic':roomLogicFunction,
    'objects':[

               {
                'name':'door',
                'dimension' : (-50, globals.screenHeight/2 - 100, 50, 150),
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
               },
               {
                'name':'bubble',
                'data' : bubbleImage,
                'dimension' : (190, 75, 0, 0),
                'shape':'image'
                },
                {
                'name':'information label',
                'text' : "HEADS OR TAILS?",
                'size':22,
                'dimension' : (200, 100, 0, 0),
                'shape':'label',
                'color': (0, 0, 0),
                'backgroundColor':(0, 0, 0)
               },
                {
                'name':'headsLabel',
                'text' : '1 = HEADS',
                'size':38,
                'dimension' : (455, 385, 0, 0),
                'shape':'label',
                'color': (255, 0, 0),
                'backgroundColor':(0, 0, 0)
               },
                {
                'name':'headsLabel',
                'text' : '2 = TAILS',
                'size':38,
                'dimension' : (455, 428, 0, 0),
                'shape':'label',
                'color': (0, 255, 0),
                'backgroundColor':(0, 0, 0)
               },            
                {
                'name':'result',
                'text' : "",
                'size':38,
                'dimension' : (355, 478, 0, 0),
                'shape':'label',
                'color': (0, 255, 0),
                'backgroundColor':(0, 0, 0)
               }            
            ]
}
