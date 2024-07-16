from w8_shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        self._shape_type = 'Circle' 
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('Radius must be positive')
        self.__radius = value
    
    # override area() method to calculate area of a circle
    def area(self):
        return 3.14 * self.radius ** 2
    
    # override __str__ method to return string representation of the object
    def __str__(self):
        return super().__str__() + f', radius: {self.radius}'
    
if __name__ == '__main__':
    c = Circle('O', 5)
    print(c)    # print will calll method __str__ of Circle class to print
    