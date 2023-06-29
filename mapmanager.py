import pickle
class Mapmanager():
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.color = [(0.2, 0.2, 0.35, 0.5), (0.2, 0.2, 0.2, 0.5),
                      (0.2, 0.6, 0.2, 0.5), (0.2, 0.8, 0.35, 0.5)]
        self.startNew()
        base.accept("control-s", self.save)
        base.accept("control-e", self.export)
    def startNew(self):
        self.land = render.attachNewNode("Land")
    def findBlock(self, pos):
        block = self.land.findAllMatches("=at=" + str(pos))
        if block:
            return False
        else:
            return True
    def findTheHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.findBlock((x, y, z)):
            z += 1
        return (x, y, z)
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color[position[2]] if position[2]<4 else self.color[3])
        self.block.setTag("at", str(position))
        self.block.reparentTo(self.land)
    def save(self):
        blocks = self.land.getChildren()
        with open("saved_land.dat", "wb") as f:
            pickle.dump(len(blocks), f)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, f)
    def export(self):
        self.clear()
        with open("saved_land.dat", "rb") as f:
            length = pickle.load(f)
            for i in range(length):
                pos = pickle.load(f)
                self.addBlock(pos)
    def del_block(self, pos):
        blocks = self.land.findAllMatches("=at=" + str(pos))
        for block in blocks:
            block.removeNode()
            block.removePath()
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def load_land(self, file):
        self.clear()
        with open(file, "r") as f:
            y = 0
            for string in f:
                x = 0
                strings = string.split(" ")
                for z in strings:
                    for z0 in range(int(z)+1):
                        self.addBlock((x, y, z0))
                    x += 1
                y+=1