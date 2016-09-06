# Assignment 9
# Swimming Fish and Worms using Classes
# Junmanee Cadenhead


from graphics import *
from random import randint

class MakeFish:
    
    '''Constructor'''
    def __init__(self, x, y, color, speed):
        '''make body'''
        self.body = Oval(Point(x-20,y-10), Point(x+20,y+10))
        self.body.setFill(color)
        self.body.setOutline(color)
        self.worms = Text(Point(-100, -65), "~")
        self.worms.setSize(36)
        self.worms.setTextColor('pink')

        '''make tail & eye depending on assigned speed'''
        if speed > 0:
            self.fin = Oval(Point(x-8, y-16), Point(x-14, y+16))
            self.eye = Circle(Point(x+8, y+4), 2)
            
        elif speed < 0:
            self.fin = Oval(Point(x+8, y-16), Point(x+14, y+16))
            self.eye = Circle(Point(x-8, y+4), 2)

            
        self.fin.setFill(color)
        self.fin.setOutline(color)
        self.eye.setFill("white")


        self.speed = speed

    '''Methods'''
    def getCenter(self):
        center = self.body.getCenter()
        return center
    

    def draw(self,win):
        self.body.draw(win)
        self.fin.draw(win)
        self.eye.draw(win)
        self.worms.draw(win)


    def move(self, dx, dy):
        self.body.move(dx,dy)
        self.fin.move(dx,dy)
        self.eye.move(dx,dy)
        self.worms.move(dx,dy)

        
    def getSpeed(self):
        return self.speed
 

        
#------------------------------------------------------------------------------          
'''Random Number Generator that takes out 0'''
def RandNotZero(n):
    rand = 0
    while rand == 0:
        rand = randint(-n,n)
    return rand


'''wrap around: finds the center point of the fish and determins whether it is.
If it is beyond the window, the fish is moved back.'''
def wrap(win, fish):
    speed = fish.getSpeed()
    cx = fish.getCenter().getX()
    
    if cx > 105:
        fish.move(-200,0)
    elif cx < -105:
        fish.move(200,0)
    else:
        fish.move(speed, 0)

    

def main():
    '''User input and creating the window'''
    ndisks = eval(input("How many fish? "))
    print("#fish=",ndisks)
    
    win = GraphWin( 'Swim Disks Class', 500, 500 )
    win.setBackground( 'SlateGray1' )
    w = 100
    win.setCoords( -w, -w, w, w)

    sand = Rectangle(Point(-105, -60), Point(105, -105))
    sand.setFill('lemon chiffon')
    sand.draw(win)

    
    Lfish = []
    for c in range(ndisks): 
        x = randint(-100,100)
        y = randint(-50,100)
        r,g,b = randint(0,255),randint(0,255),randint(0,255)
        color = color_rgb(r,g,b)
        
        speed = RandNotZero(10)
        fish = MakeFish(x, y, color, speed)
        
        fish.draw(win)
        Lfish.append(fish)

    while True:
        if win.checkMouse():
            break
        for d in Lfish:
            wrap(win, d)

    win.close()

               
main()

