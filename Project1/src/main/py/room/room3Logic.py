'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals
import pygame;


currentBananaImage = 0;
currentBananaImageSpeed = 0;
bananaApproached = False; 

bubbleImage=pygame.image.load('images/room3/Textbubble.png');
bananaPosition = (450,350);
bananaBubblePosition = (550,300);
bananaBananaMessages=["Would you like some grits?"];
bananaBananaCurrentMessage = 0;

BananaImages = [
    pygame.image.load('images/Banana/tmp-0.png'),
    pygame.image.load('images/Banana/tmp-1.png'),
    pygame.image.load('images/Banana/tmp-2.png'),
    pygame.image.load('images/Banana/tmp-3.png'),
    pygame.image.load('images/Banana/tmp-4.png'),
    pygame.image.load('images/Banana/tmp-5.png'),
    pygame.image.load('images/Banana/tmp-6.png'),
    pygame.image.load('images/Banana/tmp-7.png')

]

'''
Return True if walking person is close to the banana
'''
def isPersonCloseToBanana ():
    
    global bananaPosition;
    
    x = globals.currentXPos;
    y =  globals.currentYPos;
    
    #that's where the babana is
    rect = pygame.Rect (bananaPosition [0], bananaPosition [1], 350, 350);
    
    #check each point in the square when the walking man is
    for i in range (x, x + 100):
        for j in range (y, y + 100):
            if (rect.collidepoint (i, j)):
                return True;
    


'''
Logic pertaining to various events in room3
'''
def roomLogicFunction (object, roomObject) :

    global currentBananaImageSpeed, currentBananaImage;
    global bananaApproached, bubbleImage, bananaPosition;
    global bananaBananaMessages, bananaBananaCurrentMessage;
    global roomData;

    globals.screen.blit(BananaImages [currentBananaImage], bananaPosition);

    currentBananaImageSpeed += 1;


    #draw Banana, currentBananaImageSpeed controls how fast it goes
    if (not bananaApproached):
        if (currentBananaImageSpeed > 4):
            currentBananaImageSpeed = 0;
    
            currentBananaImage += 1;
            if (currentBananaImage > len (BananaImages) - 1):
                currentBananaImage = 0;

    if (not bananaApproached and isPersonCloseToBanana ()):
        bananaApproached = True;      
        globals.direction="stand";  

    #check if bubble needs to be drawn
    if (bananaApproached):
        
        #draw bubble
        globals.screen.blit (bubbleImage, bananaBubblePosition);
        
        #draw current question
        globals.drawLabel(bananaBubblePosition [0] + 15, bananaBubblePosition [1] + 15, bananaBananaMessages [bananaBananaCurrentMessage])

#room description
roomData = {
    'name':"Happy World",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/a-happy-place-sunrise.png',
    'speed': 8,
    'roomLogic':roomLogicFunction,
    'objects':[
               {
                'name':'door',
                'dimension' : (0, globals.screenHeight-150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':1,
                'exitTo':'left'
               },
               {
                'name':'door',
                'dimension' : (globals.screenWidth-50, globals.screenHeight - 150, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':3,
                'exitTo':'right'
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
