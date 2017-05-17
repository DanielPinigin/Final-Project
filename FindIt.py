#Impot ggame stuff
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

class Spaceship(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Spaceship.asset, position)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()
        
class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.vx = 0.5
        self.vy = 0.9
        self.circularCollisionModel()
        FindGame.listenKeyEvent("keydown", "w", self.Speed)
    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.x+self.vx > self.width//512+1
            set self.x = 0
    def Speed(self, event):
        self.vx += 5
    
class FindGame(App):
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
            Spaceship((.5*(self.width//512+1)*512,.5*(self.height//512+1)*512-90))
            Sun((100,100))
    def step(self):
        for asset in self.getSpritesbyClass(Sun):
            asset.step()
myapp = FindGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
