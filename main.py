from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.land = Mapmanager()
        self.land.load_land("land1.txt")
        self.hero = Hero((10, 10, 1), self.land)
        self.hero.move()
        self.taskMgr.add(self.update, "update")
        
    def update(self, task):
        if self.mouseWatcherNode.hasMouse():
            x = self.mouseWatcherNode.getMouseX()
            if x >= -1 and x <= -0.5:
                self.hero.left()
            elif x > -0.5 and x <= 0.5:
                pass
            else:
                self.hero.right()
            y = self.mouseWatcherNode.getMouseY()
            if y >= -1 and y <= -0.5:
                self.hero.down_show()
            elif y > -0.5 and y <= 0.5:
                pass
            else:
                self.hero.up_show()
        return task.cont

game = Game()
game.run()