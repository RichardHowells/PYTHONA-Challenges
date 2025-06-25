
class Triangle:
    def __init__(self, s1, s2, s3):
        if s1 <= 0 or s2 <= 0 or s3 <=0:
            raise ValueError("Illegal side value")
        
        if s1 > s2 + s3 or s2 > s1 + s2 or s3 > s1 + s2:
            raise ValueError("These sides don't form a triangle")
        
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self._colour = 'Black'

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
    

t1 = Triangle(3, 4, 5)
print(t1.s1, t1.s2, t1.s3, t1.get_perimiter())

print(t1.s1, t1.s2, t1.s3, t1.perimiter)

t1.colour = "Red"
print(t1.colour)

t1.colour = "dog"



