'''
Created on Jun 3, 2015

@author: Marina K
'''

from globals import globals




trivia=[
        {
         'question':'What does KFC stand for?',
         'answer':'Kentucky Fried Chicken',
         'input':''
         },
        {
         'question':'What chain is the Big Mac sold at?',
         'answer':'Mcdonalds',
         'input':''
         },
         {
         'question':'What is the Tim Hortons jingle??',
         'answer':'Always Fresh, Always Tim Hortons',
         'input':''
         },
         {
         'question':'What chain does 737-1111 belong to?',
         'answer':'Pizza Pizza',
         'input':''
         },
         {
         'question':'Which restaurant has lips as their mascot?',
         'answer':'Dairy Queen',
         'input':''
         }
];

currentTrivia=0;
currentInput=''

#need to answer 3 questions to exit
passingScore = 3;

'''
Logic pertaining to various events in room8
'''
def roomLogicFunction (object, roomObject) :
    
    global currentInput,currentTrivia, trivia, passingScore;
    
    if (hasattr (object, 'key')):
        print ('Room 8', object.unicode, '  ', object.key);
        
        #check if it's backspace
        if (object.key == 8):
            currentInput = currentInput [0:len (currentInput) - 1]
        #or Enter    
        elif (object.key == 13):
            
            #store current answer
            trivia [currentTrivia]['input']=currentInput;
            
            if (currentTrivia + 1 >= len (trivia)):
                
                #check if answers were right
                rightAnswers = 0;
                for i in trivia:
                    if (i ['answer'].strip () == i ['input'].strip ()):
                        rightAnswers += 1;
                    print ("IIIIIIIIII", i ['answer'], i ['input']);    
                        
                print ("Right:", rightAnswers);        
                #if passed, show door        
                if (rightAnswers >= passingScore):        
                    roomData ['objects'][4]['dimension']=(globals.screenWidth - 50, 100, 50, 150);
                else:
                    #if did not pass, start all over    
                    currentTrivia = 0;
                    trivia [currentTrivia]['input']=currentInput;
                    currentInput = '';
                    roomData ['objects'][5]['text']= trivia [currentTrivia]['question'];
                
            else:    
                currentTrivia += 1;
                currentInput = '';
                roomData ['objects'][5]['text']= trivia [currentTrivia]['question'];
        else:
            currentInput += object.unicode;
    
        roomData ['objects'][6]['text']= currentInput;

#room description
roomData = {
    'name':"Gluttony",
    'speed':6,
    'backgroundColor': (0, 155, 225),
    'backgroundImage' : 'images/Gluttony.jpg',
    'speed': 8,
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
               #door is hidden upon entering
               {
                'name':'door',
                'dimension' : (-50, globals.screenHeight/2 - 100, 50, 150),
                'shape':'rect',
                'backgroundColor':(0, 255, 100),
                'toRoom':11,
                'exitTo':'right'
               },
               {
                'name':'triviaQuestion',
                'text' : trivia [currentTrivia]['question'],
                'size':25,
                'dimension' : (100, 50, 300, 0),
                'shape':'label',
                'color': (255,0 , 0),
                'backgroundColor':(0, 0, 0)
               },
               {
                'name':'triviaInput',
                'text' : currentInput,
                'size':30,
                'dimension' : (100, 150, 0, 0),
                'shape':'label',
                'color': (255, 255 , 255),
                'backgroundColor':(0, 0, 0)
               }
    ]
}
