#Impot ggame stuff
"""
Find Sprite Images of letters
Find bright background color
When you type a letter, first checks if that is the correct letter in the list

"""
import random
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

class FindGame(App):
    def __init__(self, width, height):
        
        super().__init__(width, height)
        self.width=width
        self.height=height
        black = Color(0, 1)
        noline = LineStyle(0, black)
        asset = ImageAsset("images/starfield.jpg")
        for x in range(self.width//512 + 1):
            for y in range(self.height//512 + 1):
                Sprite(asset,(x*512, y*512))
        global SCREEN_WIDTH,SCREEN_HEIGHT
        SCREEN_WIDTH = self.width
        SCREEN_HEIGHT = self.height
myapp = FindGame(0,0)
class quest(Sprite):
    asset = ImageAsset("images/coollogo_com-23243960.png")
    width = 70
    height = 50
    def __init__(self, position):
        super().__init__(quest.asset, position)
        self.x = random.randint(0,SCREEN_WIDTH)
        self.y = random.randint(0,SCREEN_HEIGHT)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.vx = 3.5
        self.vy = 0.9
        self.circularCollisionModel()
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


myapp.run()