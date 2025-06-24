class Shape:
    def __init__(self, x, y):
        self._x = x
        self._y = y


class Triangle(Shape):
    def __init__(self, s1, s2, s3, x, y):
        super().__init__(x,y)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self._colour = 'Black'

    def get_area(self):
        # Area calculation not implemeted
        pass

    def get_perimiter(self):
        return self.s1 + self.s2 + self.s3
    
    def get_colour(self):
        return self._colour
    
    def set_colour(self, newColour):
        if newColour == 'Red' or newColour == "Blue" or newColour == "Green": 
           self._colour = newColour
        else:
            raise ValueError("Invalid colour")
    
    perimiter = property(get_perimiter)
    colour = property(get_colour, set_colour)

class Square(Shape):
    def __init__(self, height, width, x, y):
        super().__init__(x, y)
        self._height = height
        self._width = width
    
    def get_perimiter(self):
        return 2 * self._height + 2 * self._width
    
    perimiter = property(get_perimiter)
    

t1 = Triangle(3, 4, 5, 100, 110)
print(t1.s1, t1.s2, t1.s3, t1.get_perimiter())

print(t1.s1, t1.s2, t1.s3, t1.perimiter, t1._x, t1._y)

t1.colour = "Red"
print(t1.colour)

shapes = [ Triangle(2,2,3, 100, 110), Square(10,10, 110, 120)]
for shape in shapes:
    print(shape.perimiter)

# Moved to the very end as it raises an exception
t1.colour = "dog"



