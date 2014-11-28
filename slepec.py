import random
from snake import *

# Barva glave in repa
COLOR_HEAD = "#00FF00"
COLOR_TAIL = "#FF1493"

class Slepec(Snake):
    def __init__(self, field, x, y, dx, dy):
        # Poklicemo konstruktor nadrazreda
        Snake.__init__(self,
            field = field,
            color_head = COLOR_HEAD,
            color_tail = COLOR_TAIL,
            x = x, y = y, dx = dx, dy = dy)
        # V konstruktor lahko dodate se kaksne atribute

    def turn(self):
        """Igrica poklice metodo turn vsakic, preden premakne kaco. Kaca naj se tu odloci, ali se
           bo obrnila v levo, v desno, ali pa bo nadaljevala pot v isti smeri.

           * v levo se obrne s self.turn_left()
           * v desno se obrne s self.turn_right()
           * koordinate glave so self.coords[0]
           * smer, v katero potuje je (self.dx, self.dy)
           * spisek koordinat vseh misk je self.field.mice.keys()
           * spisek vseh kac je self.field.snakes
        """


        closestMice = self.closest_mice(self.coords[0], self.field.mice.keys())
        smer = (self.dx, self.dy)

        if smer[0] == -1:
            # kaca gre levo
            if self.coords[0][1] - closestMice[1] < 0:
                self.turn_left()
            else:
                self.turn_right()
        elif smer[0] == 1:
            # kaca gre desno
            if self.coords[0][1] - closestMice[1] < 0:
                self.turn_left()
            else:
                self.turn_right()
        else:
            # kaca gre gor
            if self.coords[0][0] - closestMice[0] > 0:
                self.turn_left()
            else:
                self.turn_right()

                

        
           
        if random.randint(0,10) < 5:
            if random.randint(0,1) == 1:
                self.turn_left()
            else:
                self.turn_right()

    def closest_mice(self, current_location, mices):
        closest = float("inf")
        closest_mice = mices
        for mice in mices:
            d = abs(current_location[0] - mice[0]) + abs(current_location[1] - mice[1])
            if d < closest:
                closest = d
                closest_mice = mice
        return closest_mice








        
