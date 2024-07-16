class Employee:
    def __init__(self, id, name, rate):
        self.id = id
        self.name = name
        self.rate = rate
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if id <= 0:
            raise ValueError("Employee ID must be positive")
        self.__id = id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Employee name cannot be empty")
        self.__name = name

    @property
    def rate(self):
        return self.__rate
    
    @rate.setter
    def rate(self, rate):
        if rate < 0:
            raise ValueError("Employee rate must be non-negative")
        self.__rate = rate
