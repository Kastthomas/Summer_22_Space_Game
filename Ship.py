##Kurtis St. Thomas 6/25/2022
##This defines the Ship class


import pyglet

class Ship(pyglet.sprite.Sprite):
    def __init__(self, image, x=0,y=0, dx=0, dy=0, rotv=0, batch=None):
        super(Ship, self).__init__(
            image, x, y, batch=batch)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rotation = rotv
        self.rot_spd = 100.0
        self.thrust = 200.0
        self.rot_left = False
        self.rot_right = False
        self.engines = False

    #updates ships rotation
    def update(self, dt):
        if self.rot_left:
                self.rotation -= self.rot_spd * dt
        if self.rot_right:
                self.rotation += self.rot_spd * dt
