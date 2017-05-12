#Impot ggame stuff
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0






class FindGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        asset = ImageAsset("NEWIMAGE.JPG")
        #for x in range(self.width//512 + 1):
            #for y in range(self.height//512 + 1):
                #Sprite(asset,(x*512, y*512))
"
myapp = FindGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
