'''
Created on Jun 13, 2015

@author: Marina K
'''

from globals import globals
import pygame

SpiderImage = [
    pygame.image.load('images/room12/spider1.png'),
    
]
    
currentSpiderImage = 0;
currentSpiderImageSpeed = 0;

spiderCoordinates=[
    {'x':50, 'y':20},
    {'x':globals.screenWidth-150, 'y':10},
    {'x':50, 'y':globals.screenHeight - 150},
    {'x':globals.screenWidth-150, 'y':globals.screenHeight - 50}
];

spider1Direction="right";
spider2Direction="left";
spider3Direction="right";
spider4Direction="left";
message="Welcome, strangest. Scared of little spiders?";

died=False;
diedCycles=0;

spiderClicks=[0, 0, 0, 0];
spiderKilled=[False, False, False, False];

'''
Init stuff
'''
def init ():
    
    global currentSpiderImage, currentSpiderImageSpeed, spiderCoordinates;
    global spider1Direction, spider2Direction, spider3Direction, spider4Direction;
    global message, died, diedCycles, spiderClicks, spiderKilled;
    
    currentSpiderImage = 0;
    currentSpiderImageSpeed = 0;
    
    spiderCoordinates=[
        {'x':50, 'y':20},
        {'x':globals.screenWidth-150, 'y':10},
        {'x':50, 'y':globals.screenHeight - 150},
        {'x':globals.screenWidth-150, 'y':globals.screenHeight - 50}
    ];
    
    spider1Direction="right";
    spider2Direction="left";
    spider3Direction="right";
    spider4Direction="left";
    message="Welcome, strangest. Scared of little spiders?";
    
    died=False;
    diedCycles=0;
    
    spiderClicks=[0, 0, 0, 0];
    spiderKilled=[False, False, False, False];

init ();

'''
check if any spider is clicked
'''        
def spiderClicked (x, y):        

    for i in range (0, 4):
        rect = pygame.Rect (spiderCoordinates [i]['x'], spiderCoordinates [i]['y'], 150, 150);
        if (rect.collidepoint (x, y)):
            return i;
        
    return -1;    
    

'''
Mark spider killed
'''
def markSpiderKilled (spiderNum):
    global spiderKilled, spiderCoordinates;
    
    spiderKilled [spiderNum]=True;
    spiderCoordinates [spiderNum]['x'] = -100;
    spiderCoordinates [spiderNum]['y'] = -100;
    

'''
check if collided with any spider
'''
def collidedWithSpiders ():
    
    x = globals.currentXPos;
    y =  globals.currentYPos;
    
    #check square
    for i in range (x, x + 50):
        for j in range (y, y + 50):
            if (spiderClicked (i, j) > -1):
                return True;
    
    
'''
Check if spider is killed
'''
def isSpiderKilled (spiderNum):
    
    global spiderKilled;
    
    return spiderKilled [spiderNum];

def allSpidersKilled ():
    for i in range (0, 4):
        if (not isSpiderKilled (i)):
            return False;
               
    return True;

'''
Check if any spider is killed
'''    
def checkIfAnySpiderIsKilled (): 
    
    global spiderClicks, message;
    
    for i in range (0, 4):
        if (spiderClicks [i] > 15 and not isSpiderKilled (i)):
            markSpiderKilled (i);
            message="You killed spider #" + str (i + 1) + ". It hurt ...";   
    
'''
Logic pertaining to various events in room11
'''
def roomLogicFunction (object, roomObject) :

    #draw Spider
    global SpiderImage, currentSpiderImageSpeed, currentSpiderImage;
    global message;
    global died;
    global diedCycles;
    global spiderClicks;
    global spiderCoordinates;
    global roomData;
    
    if (allSpidersKilled ()):
        roomData ['objects'][0]['dimension'] = (globals.screenWidth - 50, globals.screenHeight/2 - 100, 50, 150);
        message="All killed. Proceed to the door.";
        
    
    if (died):
        diedCycles += 1;
        
        if (diedCycles > 800 and not allSpidersKilled ()):
            globals.currentRoom=0;
            init ();


    #draw spiders
    for sp in range (0, 4):
        if (not isSpiderKilled (sp)):
            globals.screen.blit(SpiderImage [currentSpiderImage],(spiderCoordinates [sp]['x'], spiderCoordinates [sp]['y']));

    
    currentSpiderImageSpeed += 1;

    if (currentSpiderImageSpeed > 1):
        currentSpiderImageSpeed = 0;

        #each spider has its own moving function so 4 calls
        if (not isSpiderKilled (0)):
            moveSpider1 ();
        if (not isSpiderKilled (1)):
            moveSpider2 ();
        if (not isSpiderKilled (2)):
            moveSpider3 ();
        if (not isSpiderKilled (3)):
            moveSpider4 ();
        
    #check clicks    
    try:
        if (object.type and object.pos):

            #mouse click position
            pos = object.pos;
            x = pos[0];
            y = pos [1];
            
            clickedOnSpider=spiderClicked (x, y);
            
            if (clickedOnSpider > -1):
                if (clickedOnSpider == 0):
                    message="It tickles !";
                elif (clickedOnSpider == 1):
                    message="Looky here, we got ourselves a knight";
                elif (clickedOnSpider == 2):
                    message="I'm calling the police !!";
                elif (clickedOnSpider == 3):
                    message="Do not touch this";
                
                spiderClicks [clickedOnSpider] += 1;
                checkIfAnySpiderIsKilled ();
            

    except:
        pass;
    
    if (collidedWithSpiders ()):
        message="You just died. Kill the remaining spiders to stay alive.";
        died=True;
    #draw message    
    roomData ['objects'][1]['text']=message;

        
def moveSpider1 ():
    global spider1Direction, spiderCoordinates;
    
    spider1X=spiderCoordinates [0]['x']; 
    spider1Y=spiderCoordinates [0]['y']; 
    
    if (spider1Direction == 'right'):
        if (spider1X<350 and spider1Y < 300):
            spider1X += 5;    
            spider1Y += 4;
        else:
            spider1Direction="left";
    elif (spider1Direction == 'left'):
        if (spider1X>50 and spider1Y > 100):
            spider1X -= 4;    
            spider1Y -= 5;
        else:
            spider1Direction="right";
            
    spiderCoordinates [0]['x'] = spider1X; 
    spiderCoordinates [0]['y'] = spider1Y; 
            
    
def moveSpider2 ():
    global spider2Direction, spiderCoordinates;
    
    spider2X=spiderCoordinates [1]['x']; 
    spider2Y=spiderCoordinates [1]['y']; 
    
    if (spider2Direction == 'left'):
        if (spider2X>400 and spider2Y < 250):
            spider2X -= 3;    
            spider2Y += 2;
        else:
            spider2Direction="right";
    elif (spider2Direction == 'right'):
        if (spider2X<750 and spider2Y > 100):
            spider2X += 3;    
            spider2Y -= 2;
        else:
            spider2Direction="left";
            
    spiderCoordinates [1]['x'] = spider2X; 
    spiderCoordinates [1]['y'] = spider2Y; 
            
    
def moveSpider3 ():
    global spider3Direction, spiderCoordinates;
    
    spider3X=spiderCoordinates [2]['x']; 
    spider3Y=spiderCoordinates [2]['y'];
     
    if (spider3Direction == 'right'):
        if (spider3X<400 and spider3Y > 350):
            spider3X += 3;    
            spider3Y -= 2;
        else:
            spider3Direction = "left";
    elif (spider3Direction == 'left'):
        if (spider3X > 100 and spider3Y < 500):
            spider3X -= 2;    
            spider3Y += 3;
        else:
            spider3Direction = "right";

    spiderCoordinates [2]['x'] = spider3X; 
    spiderCoordinates [2]['y'] = spider3Y; 
        
def moveSpider4 ():
    global spider4Direction, spiderCoordinates;
    
    spider4X=spiderCoordinates [3]['x']; 
    spider4Y=spiderCoordinates [3]['y'];
    
    if (spider4Direction == 'left'):
        if (spider4X>400):
            spider4X -= 3;    
            spider4Y -= 2;
        else:
            spider4Direction = "right";
    elif (spider4Direction == 'right'):
        if (spider4X<700):
            spider4X += 2;    
            spider4Y += 3;
        else:
            spider4Direction = "left";
            
    spiderCoordinates [3]['x'] = spider4X; 
    spiderCoordinates [3]['y'] = spider4Y; 
            
            
#room description
roomData = {
    'name':"Fight Room",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Evil Room.png',
    'speed': 8,
    'roomLogic':roomLogicFunction,
    'startX':400,
    'startY':500,
    'startMovement':'none',
    'objects':[
              {
                'name':'door',
                'dimension' : (globals.screenWidth + 50, globals.screenHeight/2 - 100, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':12,
                'exitTo':'right'
               },
               {
                'name':'information label',
                'text' : message,
                'size':25,
                'dimension' : (20, 15, 0, 0),
                'shape':'label',
                'color': (255,255,255),
                'backgroundColor':(0, 0, 0)
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
