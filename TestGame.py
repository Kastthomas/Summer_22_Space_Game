##Kurtis St. Thomas 6/25/2022
##This file controls the window and events


import Ship
import Planet
import pyglet

#sets resource path
#window = pyglet.window.Window(fullscreen=True)
win = pyglet.window.Window(width=720, height=720)
pyglet.resource.path.append('C:\\Users\\17034\\Pictures\\PygletGame')
pyglet.resource.reindex()

#centers image on the screen
def center_anchor(img):
    img.amchor_x = img.width // 2
    img.amchor_y = img.height // 2

planet_image = pyglet.resource.image('Mars_Sprite.png')
center_anchor(planet_image)


center_x = int(win.width/2)
center_y = int(win.width/2)
planet = Planet.Planet(planet_image, center_x, center_y, None)

ship_image = pyglet.resource.image('Spaceship_Sprite.png')
center_anchor(ship_image)

ship_start_offset = 300
ship = Ship.Ship(ship_image, x=center_x + ship_start_offset,
                 y=center_y, dx=0, dy=150, rotv=-90)

@win.event
def on_draw():
    win.clear()
    planet.draw()
    ship.draw()


pyglet.app.run()
