#Impot ggame stuff

import random, time
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
a= random.choice('abcdefghijklmnopqrstuvwxyz')
wordList = []
Quest=0
def createWord():
    global wordList
    wordList.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
    print(wordList)
def createWord2():
    global wordList, Quest
    wordList=[]
    
    for _ in range(10):
        createWord()
    wordList= ("".join(wordList))
    print(wordList)
    Quest=TextAsset(wordList, style='100px Arial')
    print(Quest)
b = list(a)
createWord2()

class FindGame(App):
    def __init__(self, width, height):
        self.width=width
        self.height=height
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        asset = ImageAsset("blue.png")
        self.index = 0
        self.point = 0
        self.pointList = []
        self.end=False
        
        self.timerList=[]
        self.timer=60
        self.currentTime = time.time()
        for x in range(self.width//600 + 1):
            for y in range(self.height//360 + 1):
                Sprite(asset,(x*600, y*360))
        global SCREEN_WIDTH,SCREEN_HEIGHT
        SCREEN_WIDTH = self.width
        SCREEN_HEIGHT = self.height
        for c in 'abcdefghijklmnopqrstuvwxyz':
            FindGame.listenKeyEvent("keydown", c, self.key)
    def makegreensprite(self):
        checker((200+(100*self.index),100))
        if self.index == 10:
            self.point += 10
            self.update()
            print(self.getSpritesbyClass(checker), len(self.getSpritesbyClass(checker)))
            for x in self.getSpritesbyClass(checker)[:]:
                x.destroy()
            for x in self.getSpritesbyClass(quest):
                x.destroy()
                print('fun')
            createWord2()
            quest((612,342))
            print(self.point)
            self.index = 0
            
        print('Makegreensprite')
        
    def makegreenspritegoaway(self):
        for x in self.getSpritesbyClass(checker):
            x.destroy()
        print('MakeGreenSpriteGoAway')
        pass
    def key(self,event):
        if self.end=False:
            if event.key == wordList[self.index]:
                self.index += 1
                self.makegreensprite()
        
        else:
            self.index = 0
            self.point -= 2
            self.update()
            self.makegreenspritegoaway()
            self.makegreenspritegoaway()
            self.makegreenspritegoaway()
            self.makegreenspritegoaway()
            self.makegreenspritegoaway()
            self.makegreenspritegoaway()
            self.makegreenspritegoaway()

            
    def step(self):
        if time.time()-self.currentTime>1:
            self.currentTime=time.time()
            timerAsset= TextAsset(self.timer, color=Color(0x9acd32, 1))
            self.timer-=1
            if len(self.timerList)>0:
                for x in self.timerList:
                    x.destroy()
            self.timerList=[]
            self.timerList.append(Sprite(timerAsset, (self.width/2, 20)))
        if self.timer<1:
            self.end=True
            
    def update(self):
        tadaAsset = TextAsset(self.point, style='100px Arial')
        if len(self.pointList)>0:
            for x in self.pointList:
                x.destroy()
        self.pointList=[]
        self.pointList.append(Sprite(tadaAsset, (self.width/2, 50)))
            
myapp = FindGame(0,0)
startTime = time.time()
class Timer(Sprite):
    def __init__(self, startvalue, position, expired):
        self.startvalue = startvalue
        self.starttime = time.time()
        startasset = TextAsset("{0}".format(startvalue), style='100px Arial')
        super.__init__(startasset,position)
        self.expired = expired
        "{0}".format(startvalue)
    
    def step(self):
        pass
        if time.timer() > self.starttime+1:
            if self.startvalue == 1:
                self.expire()
            else:
                Timer(self.startvalue-1,self.position,self.expired)
            self.destroy()
class checker(Sprite):
    asset = ImageAsset("green-dot-hi.png")
    width = 50
    height = 50
    def __init__(self, position):
        super().__init__(checker.asset, position)
        self.scale = .05
        
class quest(Sprite):
    global Quest
    print(Quest)
    asset = Quest
    width = 70
    height = 50
    def __init__(self, position):
        super().__init__(Quest, position)
        quest1 = b
        
#class questy(quest):
    
  
quest((612,342))
#checker((100,100))
#checker((200+(50*myapp.index),100))

def done():
    print('Timer Expired!')

print(Timer)
timer = Timer(60,(150,150), done)
#myapp.run(timer.step)
myapp.update()
myapp.run()