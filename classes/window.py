import pyglet

class Window(pyglet.window.Window):
    def __init__(self, winwidth=int, winheight=int, vsync=True, fpsdisplay=True):
        super().__init__(winwidth, winheight, vsync=vsync)
        self.fpsdisplay = fpsdisplay
        if self.fpsdisplay == True: self.fpsd = pyglet.window.FPSDisplay(self)
        self.batch = pyglet.shapes.Batch()
    def update(self):
        self.clear()
        self.batch.draw()
        self.fpsd.draw()