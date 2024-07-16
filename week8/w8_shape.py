from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name            # call setter method to set name attribte
        self._shape_type = 'Shape'  # protected attribute
    @property
    def name(self):
        return self.__name          # private attribute
    
    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError('Name cannot be empty')
        self.__name = name
    
    # area() is abstract method because we don't know how to calculate area of a general shape
    @abstractmethod
    def area(self): 
        pass
    
    # override __str__ method to return string representation of the object
    def __str__(self):
        return f'{self._shape_type} {self.__name}, area: {self.area()}'