from Constants import *

class Square:
    def __init__(self, value: int = -1, color: tuple = BLACK) -> None:
        self.value = value
        self.color = color
    
    def changeValue(self, newValue: int) -> None:
        if newValue == 0:
            self.value = newValue 
            self.color = GREEN
        elif newValue == -2:
            self.value = newValue
            self.color = WHITE
        else:
            self.value = newValue
            self.color = GREY