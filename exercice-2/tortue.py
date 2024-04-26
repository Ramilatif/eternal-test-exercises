

class Tortue:
    x=0
    y=0
    direction = 1

    def __init__(self,x,y):
    
        self.x = x 
        self.y = y 
        self.direction = 1 


    def walk(self,d:int):
        match self.direction:
            case 1:
                self.y -= d
            case 2:
                self.x += d
            case 3:
                self.y += d
            case 4:
                self.x -= d
                 
    def look_up(self):
        self.direction = 1

    def look_right(self):
        self.direction = 2

    def look_down(self):
        self.direction = 3
    
    def look_left(self):
        self.direction = 4

    def teleport(self,x,y):
        self.x = x
        self.y = y

   