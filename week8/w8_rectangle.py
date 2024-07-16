from w8_shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        self._shape_type = 'Rectangle'

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('Width must be positive')
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError('Height must be positive')
        self.__height = value

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return super().__str__() + f', dimensions: {self.width} x {self.height}'

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)  # Rectangle constructor takes same width and height
        self._shape_type = 'Square'
    
    @property
    def side(self):
        return self.width
    
    @side.setter
    def side(self, value):
        self.width = value
        self.height = value

if __name__ == '__main__':
    r = Rectangle('R', 5, 10)
    print(r)    # print will calll method __str__ of Rectangle class to print

    s = Square('ABCD', 10)
    print(s)    # print will calll method __str__ of Rectangle class to print
