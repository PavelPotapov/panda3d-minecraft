class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.pos = pos
        self.hero0 = loader.loadModel("block")
        self.hero0.setPos(pos)
        self.hero0.setScale(0.3)
        self.hero0.reparentTo(render)
        base.camera.reparentTo(self.hero0)
        base.disableMouse()
    def move(self):
        base.accept("w", self.forward)
        base.accept("a", self.leftward)
        base.accept("d", self.rightward)
        base.accept("q", self.build)
        base.accept("e", self.delete)
        base.accept("s", self.backward)
        base.accept("space", self.pod)
        base.accept("control-space", self.pod_del)
        base.accept("arrow_down", self.down_show)
        base.accept("arrow_up", self.up_show)
        base.accept("arrow_left", self.left)
        base.accept("arrow_right", self.right)
        base.accept("w" + "-repeat", self.forward)
        base.accept("a" + "-repeat", self.leftward)
        base.accept("d" + "-repeat", self.rightward)
        base.accept("q" + "-repeat", self.build)
        base.accept("s" + "-repeat", self.backward)
        base.accept("space" + "-repeat", self.pod)
        base.accept("control-space" + "-repeat", self.pod_del)
        base.accept("arrow_down" + "-repeat", self.down_show)
        base.accept("arrow_up" + "-repeat", self.up_show)
        base.accept("arrow_left" + "-repeat", self.left)
        base.accept("arrow_right" + "-repeat", self.right)
    def forward(self):
        pos = self.look_at(self.hero0.getH())
        #self.land.findBlock(pos)
        if self.land.findBlock(pos):
            pos = self.land.findTheHighestEmpty(pos)
            self.hero0.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.findBlock(pos):
                self.hero0.setPos(pos)
    def backward(self):
        pos = self.look_at((self.hero0.getH()+180) % 360)
        self.land.findBlock(pos)
        if self.land.findBlock(pos):
            pos = self.land.findTheHighestEmpty(pos)
            self.hero0.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.findBlock(pos):
                self.hero0.setPos(pos)
    def rightward(self):
        pos = self.look_at((self.hero0.getH() - 90) % 360)
        self.land.findBlock(pos)
        if self.land.findBlock(pos):
            pos = self.land.findTheHighestEmpty(pos)
            self.hero0.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.findBlock(pos):
                self.hero0.setPos(pos)
    def leftward(self):
        pos = self.look_at((self.hero0.getH() + 90) % 360)
        self.land.findBlock(pos)
        if self.land.findBlock(pos):
            pos = self.land.findTheHighestEmpty(pos)
            self.hero0.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.findBlock(pos):
                self.hero0.setPos(pos)
    def right(self):
        rot = self.hero0.getH()
        self.hero0.setH((rot - 1) % 360)
    def left(self):
        rot = self.hero0.getH()
        self.hero0.setH((rot + 1) % 360)
    def pod(self):
        pos = self.hero0.getPos()
        pos = pos[0], pos[1], pos[2]+1
        x, y, z = pos
        pos = self.land.findTheHighestEmpty(pos)
        self.land.addBlock(pos)
        self.hero0.setPos(x, y, z)
    def pod_del(self):
        pos = self.hero0.getPos()
        pos = pos[0], pos[1], pos[2] - 1
        x, y, z = pos
        pos = self.land.findTheHighestEmpty(pos)
        self.land.del_block(pos)
        self.hero0.setPos(x, y, z)
    def build(self):
        pos = self.look_at(self.hero0.getH() % 360)
        self.land.addBlock(pos)
    def delete(self):
        pos = self.look_at(self.hero0.getH() % 360)
        self.land.del_block(pos)
    def look_at(self, angle):
        x, y, z = self.hero0.getPos()
        x = round(x)
        y = round(y)
        z = round(z)
        dx, dy = self.check_dir(angle)
        return x+dx, y+dy, z
    def down_show(self):
        rot = self.hero0.getP()
        self.hero0.setP((rot - 1) % 360)
    def up_show(self):
        rot = self.hero0.getP()
        self.hero0.setP((rot + 1) % 360)
    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, 1)
        elif angle <= 65:
            return (-1, 1)
        elif angle <= 110:
            return (-1, 0)
        elif angle <= 155:
            return (-1, -1)
        elif angle <= 200:
            return (0, -1)
        elif angle <= 245:
            return (1, -1)
        elif angle <= 290:
            return (1, 0)
        elif angle <= 335:
            return (1, 1)
        else:
            return (0, 1)