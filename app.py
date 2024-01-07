from pyglet import app, image
from classes.cube import Rectangle
from classes.window import Window
from colorama import Fore
pic=image.load_animation("assets/boykisser.gif")
game = Window(640, 480, True, True)
keys:list=[]
debugcollision=False
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
    pic.anchor_x = rect1.x
    pic.anchor_y = rect1.y
    colliding:tuple=rect1.collides_with(rect2)
    direction=rect1.movement(keys, 5)
    if colliding==[]:
        if debugcollision: print(f"{Fore.GREEN}[rect1]{Fore.WHITE} No collision.")
        pass
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
    if "f" in keys:
        print(f"{Fore.GREEN}[Game]{Fore.WHITE} F pressed; this should be an attack.")
        keys.remove("f")
    print(f"{Fore.GREEN}[rect1]{Fore.WHITE} Current direction: {direction}")
    game.update()
@game.event
def on_key_press(key, bs) -> None:
    keys.append(chr(key))
@game.event
def on_key_release(key, bs) -> None:
    if chr(key) == "f":
        pass
    else:
        keys.remove(chr(key))

app.run()