'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals
import pygame;
from pygame.event import Event

currentDancersImage = 0;
currentDancersImageDelta = 0;


dancersImages = [
    pygame.image.load('images/Dancing people/tmp-0.png'),
    pygame.image.load('images/Dancing people/tmp-1.png'),
    pygame.image.load('images/Dancing people/tmp-2.png'),
    pygame.image.load('images/Dancing people/tmp-3.png'),
    pygame.image.load('images/Dancing people/tmp-4.png'),
    pygame.image.load('images/Dancing people/tmp-5.png'),
    pygame.image.load('images/Dancing people/tmp-6.png'),
    pygame.image.load('images/Dancing people/tmp-7.png'),
    pygame.image.load('images/Dancing people/tmp-8.png'),
    pygame.image.load('images/Dancing people/tmp-9.png'),
    pygame.image.load('images/Dancing people/tmp-10.png'),
    pygame.image.load('images/Dancing people/tmp-11.png'),
    pygame.image.load('images/Dancing people/tmp-12.png'),
    pygame.image.load('images/Dancing people/tmp-13.png'),
    pygame.image.load('images/Dancing people/tmp-14.png'),
    pygame.image.load('images/Dancing people/tmp-15.png'),
    pygame.image.load('images/Dancing people/tmp-16.png'),
    pygame.image.load('images/Dancing people/tmp-17.png'),
    pygame.image.load('images/Dancing people/tmp-18.png'),
    pygame.image.load('images/Dancing people/tmp-19.png'),
    pygame.image.load('images/Dancing people/tmp-20.png'),
    pygame.image.load('images/Dancing people/tmp-21.png'),
    pygame.image.load('images/Dancing people/tmp-22.png'),
    pygame.image.load('images/Dancing people/tmp-23.png'),
    pygame.image.load('images/Dancing people/tmp-24.png'),
    pygame.image.load('images/Dancing people/tmp-25.png'),
    pygame.image.load('images/Dancing people/tmp-26.png'),
    pygame.image.load('images/Dancing people/tmp-27.png'),
    pygame.image.load('images/Dancing people/tmp-28.png'),
    pygame.image.load('images/Dancing people/tmp-29.png'),
    pygame.image.load('images/Dancing people/tmp-30.png'),
    pygame.image.load('images/Dancing people/tmp-31.png'),
    pygame.image.load('images/Dancing people/tmp-32.png'),
    pygame.image.load('images/Dancing people/tmp-33.png'),
    pygame.image.load('images/Dancing people/tmp-34.png'),
    pygame.image.load('images/Dancing people/tmp-35.png'),
    pygame.image.load('images/Dancing people/tmp-36.png'),
    pygame.image.load('images/Dancing people/tmp-37.png')
]


'''
This method changes coordinates to make door visible
when the key has been clicked
'''
def openDoor ():
    global roomData;
    roomData ['objects'][6]['dimension']= (0, globals.screenHeight/2 - 100, 50, 150);
    roomData ['objects'][5]['text']= "Very good. You may proceed now";

    #hide the key
    roomData ['objects'][4]['dimension']= (-525, 400, 50, 50);


'''
Logic pertaining to various events in room11
'''
def roomLogicFunction (object, roomObject) :

    #draw dancers
    global dancersImages, currentDancersImageDelta, currentDancersImage;

    globals.screen.blit(dancersImages [currentDancersImage],(0,-50));

    globals.screen.blit(dancersImages [currentDancersImage],(450,150));
    currentDancersImageDelta += 1;


    if (currentDancersImageDelta > 3):
        currentDancersImageDelta = 0;
        currentDancersImage += 1;
        if (currentDancersImage > 36):
            currentDancersImage = 0;


    #check if mouse clicked
    try:
        if (object.type and object.pos):

            #mouse click position
            #'dimension' : (525, 400, 50, 50),
            pos = object.pos;
            x = pos[0];
            y = pos [1];

            if (x > 525 and x < 525 + 50 and y > 400 and y < 400 + 50):
                openDoor ();
    except:
        pass;

#room description
roomData = {
    'name':"",
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Lust.jpg',
    'speed': 8,
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
                'name':'key image',
                'dimension' : (580, 390, 50, 50),
                'shape':'image',
                'data':pygame.image.load('images/room11/key.png')
               },
               {
                'name':'information label',
                'text' : 'Welcome to Lust Room, find a key to exit it. Or die trying. Ha ha.',
                'size':15,
                'dimension' : (20, 15, 0, 0),
                'shape':'label',
                'color': (255,255,255),
                'backgroundColor':(0, 0, 0)
               },
               {
                'name':'door',
                'dimension' : (-100, globals.screenHeight/2 - 100, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':11,
                'exitTo':'left'
               }
    ]
}
