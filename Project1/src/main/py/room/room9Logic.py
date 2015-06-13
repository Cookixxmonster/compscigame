'''
Created on Jun 6, 2015

@author: Marina K
'''
import pygame;
import random;
from globals import globals

#generate random string
digits="1234";
randomString=''.join (random.choice(digits) for _ in range(4))
clickedMirrors="";

'''
Logic pertaining to various events in room9
'''
def roomLogicFunction (object, roomObject) :
    #check if mouse clicked
    
    global clickedMirrors, roomData;
    
    try:
        if (object.type and object.pos):

            #mouse click position
            #'dimension' : (525, 400, 50, 50),
            pos = object.pos;
            x = pos[0];
            y = pos [1];
            
            clickedMirror = isMirrorClicked (x, y);
            if (clickedMirror):
                clickedMirrors += clickedMirror;
                
            #when 4 numberes entered, compare
            #it to the random string generated before
            if (len (clickedMirrors) == 4):
                
                info = "";
                correctResult = randomString == clickedMirrors;
                if (correctResult):
                    info = "PROCEED TO EXIT";
                    roomData ['objects'][4]['dimension']=(globals.screenWidth - 50, 100, 50, 150);
                else:
                    info = "WRONG GUESS";
                    
                clickedMirrors = "";    
                
                roomData ['objects'][12]['text']=info;
            else:
                #clear info when number entered
                roomData ['objects'][12]['text']=''; 
 

            roomData ['objects'][9]['text']= "YOU'VE ENTERED:" + clickedMirrors;

    except:
        pass;

'''
Return number of the clicked mirror
Or False if it's not clicked
'''
def isMirrorClicked (x, y):
    global roomData;
    
    for i in range (0, 4):
        dimension = roomData ['objects'][5 + i]['dimension'];
        rect = pygame.Rect (dimension [0], dimension [1], dimension [2], dimension [3]);
        if (rect.collidepoint (x, y)):
            return str (i + 1);
        
    return False;    
        

#room description
roomData = {
    'name':"",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Pride.jpg',
    'startX':400,
    'startY':550,
    'startMovement':'stand',
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
                'dimension' : (-50, globals.screenHeight/2 - 100, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':11,
                'exitTo':'right'
               },
               #mirrors, invisible objects
               {
                'name':'mirror1',
                'dimension' : (10, 340, 90, 300),
                'shape':'mirror',
                'backgroundColor':(0, 0, 0)
               },
               {
                'name':'mirror2',
                'dimension' : (105, 285, 100, 300),
                'shape':'mirror',
                'backgroundColor':(0, 0, 0)
               },
               {
                'name':'mirror3',
                'dimension' : (615, 285, 100, 300),
                'shape':'mirror',
                'backgroundColor':(0, 0, 0)
               },               
               {
                'name':'mirror4',
                'dimension' : (715, 315, 100, 300),
                'shape':'mirror',
                'backgroundColor':(0, 0, 0)
               },
               #labels
               {
                'name':'information label',
                'text' : "YOU'VE ENTERED:",
                'size':48,
                'dimension' : (165, 100, 0, 0),
                'shape':'label',
                'color': (0, 255, 0),
                'backgroundColor':(0, 0, 0)
               },
               {
                'name':'randomString',
                'text' : randomString,
                'size':16,
                'dimension' : (700, 680, 0, 0),
                'shape':'label',
                'color': (255,255,255),
                'backgroundColor':(0, 0, 0)
               },
               {
                'name':'info',
                'text' : 'Click on the mirrors to enter the number which will open the doors',
                'size':24,
                'dimension' : (20, 20, 0, 0),
                'shape':'label',
                'color': (255,255,255),
                'backgroundColor':(0, 0, 0)
               },
               {
                'name':'result',
                'text' : '',
                'size':36,
                'dimension' : (300, 150, 0, 0),
                'shape':'label',
                'color': (255,0 , 0),
                'backgroundColor':(0, 0, 0)
               },

            ]
}
