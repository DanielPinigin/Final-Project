#Impot ggame stuff
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0



print("I <3 Computer Programming!!!")


class FindGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        asset = ImageAsset("lel.jpg")
        for x in range(self.width//600 + 1):
            for y in range(self.height//600 + 1):
                Sprite(asset,(x*600, y*600))

myapp = FindGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
