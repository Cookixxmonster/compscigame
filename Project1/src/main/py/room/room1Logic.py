'''
Created on Jun 1, 2015

@author: Marina K
'''

from globals import globals
import pygame

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
    'speed': 8,
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
                'dimension' : (700, 0, 140, 25),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':1,
                'exitTo':'down'
               },
               {
                'name':'bed',
                'dimension' : (350, 300, 280, 400),
                'shape':'rect',
                'backgroundColor':(123, 121, 148),
                },
               {
                'name':'pillow1',
                'dimension' : (370, 600, 100, 90),
                'shape':'rect',
                'backgroundColor':(240,210,170),
                },
                {
                'name':'pillow2',
                'dimension' : (510, 600, 100, 90),
                'shape':'rect',
                'backgroundColor':(240,210,170),
                },
    
               {
                'name':'blanket',
                'dimension' : (350, 300, 280, 250),
                'shape':'rect',
                'backgroundColor':(181, 128, 217),
                },
               {
                'name':'table',
                'dimension' : (50, 25, 150, 125),
                'shape':'rect',
                'backgroundColor':(130, 92, 10),
                },
               {
                'name':'paper',
                'dimension' : (87.5, 56.25, 75, 62.5),
                'shape':'rect',
                'backgroundColor':(255,255,255),
                },
               {
                'name':'chair',
                'dimension' : (85, 160, 75, 50),
                'shape':'rect',
                'backgroundColor':(130, 92, 10),
                },
               {
                'name':'chair',
                'dimension' : (85, 160, 75, 50),
                'shape':'rect',
                'backgroundColor':(130, 92, 10),
                },
               {
                'name':'sickstickman',
                'data' : pygame.image.load('images/stick.png'),
                'dimension' : (430, 450, 0, 0),
                'shape':'image'
                }
               
               
     ]
   }

