#Impot ggame stuff
"""
Make Sprite which shows how many characters you've gotten correct of the word so far
When an image is displayed, it requires the user to type its characters
the characters must be typed in order that appear in the list of that word
if the incorrect character is typed, reset all progress on the current word
every time you type the correct character in the list, a green dot sprite will be created on the screen, 
one for each character
once the user types all the characters, the image is changed to the next image and demands that a new list is typed
When you type a letter, first checks if that is the correct letter in the list
See if you can do time so player has 60s to get as far as possible
find way to center text as word increases in size
time.time() the number of seconds since january 1970
    FindGame.listenKeyEvent("keydown", "q", qkey)
    FindGame.listenKeyEvent("keydown", "w", wkey)
    FindGame.listenKeyEvent("keydown", "e", ekey)
    FindGame.listenKeyEvent("keydown", "r", rkey)
    FindGame.listenKeyEvent("keydown", "t", tkey)
    FindGame.listenKeyEvent("keydown", "y", ykey)
    FindGame.listenKeyEvent("keydown", "u", ukey)
    FindGame.listenKeyEvent("keydown", "i", ikey)
    FindGame.listenKeyEvent("keydown", "o", okey)
    FindGame.listenKeyEvent("keydown", "p", pkey)
    FindGame.listenKeyEvent("keydown", "w", wkey)
    FindGame.listenKeyEvent("keydown", "a", akey)
    FindGame.listenKeyEvent("keydown", "s", skey)
    FindGame.listenKeyEvent("keydown", "d", dkey)
    FindGame.listenKeyEvent("keydown", "f", fkey)
    FindGame.listenKeyEvent("keydown", "g", gkey)
    FindGame.listenKeyEvent("keydown", "h", hkey)
    FindGame.listenKeyEvent("keydown", "j", jkey)
    FindGame.listenKeyEvent("keydown", "k", kkey)
    FindGame.listenKeyEvent("keydown", "l", lkey)
    FindGame.listenKeyEvent("keydown", "z", zkey)
    FindGame.listenKeyEvent("keydown", "x", xkey)
    FindGame.listenKeyEvent("keydown", "c", ckey)
    FindGame.listenKeyEvent("keydown", "v", vkey)
    FindGame.listenKeyEvent("keydown", "b", bkey)
    FindGame.listenKeyEvent("keydown", "n", nkey)
    FindGame.listenKeyEvent("keydown", "m", mkey)
    random.choice(['a','b', etc])
    for _ in range(5):
        create()
"""
import random, time
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
a= random.choice('abcdefghijklmnopqrstuvwxyz')
wordList = []
def createWord():
    global wordList
    wordList.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
    print(wordList)
def createWord2():
    global wordList
    wordList=[]
    
    for _ in range(10):
        createWord()
    wordList= ("".join(wordList))
    print(wordList)
b = list(a)
createWord2()
Quest=TextAsset(wordList, style='100px Arial')
class FindGame(App):
    def __init__(self, width, height):
        self.width=width
        self.height=height
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        asset = ImageAsset("images/starfield.jpg")
        self.index = 0
        #for x in range(self.width//512 + 1):
            #for y in range(self.height//512 + 1):
                #Sprite(asset,(x*512, y*512))
        global SCREEN_WIDTH,SCREEN_HEIGHT
        SCREEN_WIDTH = self.width
        SCREEN_HEIGHT = self.height
        for c in 'abcdefghijklmnopqrstuvwxyz':
            FindGame.listenKeyEvent("keydown", c, self.key)
    def makegreensprite(self):
        checker((200+(100*self.index),100))
        print('Makegreensprite')
        
    def makegreenspritegoaway(self):
        print('MakeGreenSpriteGoAway')
        pass
    def key(self,event):
        if event.key == wordList[self.index]:
            self.index += 1
            self.makegreensprite()
        else:
            self.index = 0
            self.makegreenspritegoaway()
            
    def step(self):
        pass
            
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
    asset = Quest
    width = 70
    height = 50
    def __init__(self, position):
        super().__init__(quest.asset, position)
        quest1 = b
        
quest((612,342))
#checker((100,100))
#checker((200+(50*myapp.index),100))

def done():
    print('Timer Expired!')

print(Timer)
timer = Timer(60,(150,150), done)
#myapp.run(timer.step)
myapp.run()