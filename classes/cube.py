import pyglet

class Rectangle(pyglet.shapes.Rectangle):
    def __init__(self, x=int, y=int, width=int, height=int, color=(255, 255, 255, 255), batch=object):
        super().__init__(x, y, width, height, color, batch)
        self.last="None"
    def movement(self, keylist=list, speed=int):
        """MUST BE chr(key)"""
        if "w" in keylist:
            self.y+=speed
            self.last="Up"
            return "Up"
        if "a" in keylist:
            self.x-=speed
            self.last="Left"
            return "Left"
        if "s" in keylist:
            self.y-=speed
            self.last="Down"
            return "Down"
        if "d" in keylist:
            self.x+=speed
            self.last="Right"
            return "Right"
        return self.last
    def collides_with(self, other):
        x_overlap = max(0, min(self.x + self.width, other.x + other.width) - max(self.x, other.x))
        y_overlap = max(0, min(self.y + self.height, other.y + other.height) - max(self.y, other.y))

        collision_directions = []
        
        a = (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )
        if a:
            if x_overlap > y_overlap:
                if self.y < other.y: collision_directions.append("Down")
                if self.y > other.y: collision_directions.append("Up")
            else:
                if self.x < other.x: collision_directions.append("Left")
                if self.x > other.x: collision_directions.append("Right")

        return collision_directions