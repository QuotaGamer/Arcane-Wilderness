from pyglet import app
from classes.cube import Rectangle
from classes.window import Window
from colorama import Fore
game = Window(640, 480, True, True)
keys:list=[]
global direction
direction=""
clickedat:list=[]
rect1 = Rectangle(50, 50, 50, 50, batch=game.batch)
rect2 = Rectangle(75, 75, 50, 80, batch=game.batch)
@game.event
def on_mouse_press(x, y, button, bs) -> None:
    if x > rect1.x:
        clickedat.append("Left")
    else:
        clickedat.append("Right")
    if y > rect1.y:
        clickedat.append("Up")
    else:
        clickedat.append("Down")
    print(f"{Fore.GREEN}[Cursor] {Fore.WHITE}Clicked at: {clickedat}")
@game.event
def on_mouse_release(*args) -> None:
    clickedat.clear()


@game.event
def on_draw() -> None:
    global direction #:skull:
    if "f" in keys:
        print(f"{Fore.GREEN}[Game]{Fore.WHITE} F pressed; this should be an attack.")
    print(f"{Fore.GREEN}[rect1]{Fore.WHITE} Current direction: {direction}")
    colliding:tuple=rect1.collides_with(rect2)
    if colliding==[]:
        print(keys)
        direction=rect1.movement(keys, 5)
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
    game.update()
@game.event
def on_key_press(key, bs) -> None:
    keys.append(chr(key))
@game.event
def on_key_release(key, bs) -> None:
    keys.remove(chr(key))

app.run()