##Kurtis St. Thomas 6/25/2022
##This defines the Planet class

import pyglet


class Planet(pyglet.sprite.Sprite):
    def __init__(self, image, x=0,y=0, batch=None):
        super(Planet, self).__init__(
            image, x, y, batch=batch)
        self.x = x
        self.y = y
