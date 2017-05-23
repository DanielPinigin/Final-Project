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

class quest(Sprite):
    asset = ImageAsset("images/coollogo_com-23243960.png")
    width = 70
    height = 50
class FindGame(App):
    FindGame.listenKeyEvent("keydown", "q", key)
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
    def __init__(self, width, height):
        self.width=width
        self.height=height
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        asset = ImageAsset("images/starfield.jpg")
        for x in range(self.width//512 + 1):
            for y in range(self.height//512 + 1):
                Sprite(asset,(x*512, y*512))
myapp = FindGame(SCREEN_WIDTH, SCREEN_HEIGHT)
quest ((100,100))
myapp.run()