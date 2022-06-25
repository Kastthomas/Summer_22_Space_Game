##Kurtis St. Thomas 6/25/2022
##This file controls the window and events


import Ship
import Planet
import pyglet
from pyglet.window import key

#sets resource path
#window = pyglet.window.Window(fullscreen=True)
win = pyglet.window.Window(width=720, height=720)
pyglet.resource.path.append('C:\\Users\\17034\\Pictures\\PygletGame')
pyglet.resource.reindex()

#centers image on the screen
def center_anchor(img):
    img.amchor_x = img.width // 2
    img.amchor_y = img.height // 2
    
#implements a planet
planet_image = pyglet.resource.image('Mars_Sprite.png')
center_anchor(planet_image)


center_x = int(win.width/2)
center_y = int(win.width/2)
planet = Planet.Planet(planet_image, center_x, center_y, None)

#implements the ship
ship_image = pyglet.resource.image('Spaceship_Sprite.png')
center_anchor(ship_image)

ship_start_offset = 200
ship = Ship.Ship(ship_image, x=center_x + ship_start_offset,
                 y=center_y, dx=0, dy=150, rotv=-90)

#draws the planet and ship
@win.event
def on_draw():
    win.clear()
    planet.draw()
    ship.draw()


@win.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
                 ship.rot_left = True
    if symbol == key.RIGHT:
                 ship.rot_right = True                
    if symbol == key.UP:
                 ship.engines = True
@win.event                 
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT:
             ship.rot_left = False
    if symbol == key.RIGHT:
             ship.rot_right = False                
    if symbol == key.UP:
             ship.engines = False
        
def update(dt):
    ship.update(dt)


pyglet.clock.schedule_interval(update, 1/60.0)



pyglet.app.run()



