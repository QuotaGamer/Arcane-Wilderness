import pyglet
from classes.cube import Rectangle
from classes.window import Window
from colorama import Fore

game=Window(640, 480, True, True)
keys:list=[]
rect1= Rectangle(50, 50, 50, 50, batch=game.batch)
rect2= Rectangle(75, 75, 50, 80, batch=game.batch)
clicking= False

@game.event
def on_mouse_press(x, y, button, bs):
    print(x, y, button)
    #clicking=True

@game.event
def on_draw() -> None:
    game.update()
    if "f" in keys:
        print(f"{Fore.GREEN}[Game]{Fore.WHITE} F pressed; this should be an attack.")
    #print(clicking)
    rect1.movement(keys, 5)
    colliding:tuple=rect1.collides_with(rect2)
    if colliding==False:
        rect1.movement(keys, 5)
        print(f"{Fore.GREEN}[rect1]{Fore.WHITE} No collision.")
    else:
        print(f"{Fore.GREEN}[rect1]{Fore.WHITE} Collision: {colliding}")
        if "Up" in colliding:
            rect1.y+=5
        if "Down" in colliding:
            rect1.y-=5
        if "Right" in colliding:
            rect1.x+=5
        if "Left" in colliding:
            rect1.x-=5
@game.event
def on_key_press(key, bs) -> None:
    keys.append(chr(key))
@game.event
def on_key_release(key, bs) -> None:
    keys.remove(chr(key))

pyglet.app.run()