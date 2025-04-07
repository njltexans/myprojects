# @property  is a decorator used to define a method as a property (it can be accessed like an attribute)
#       - A benefit is that it allows for the method to be accessed without using parentheses and you can add additional logic when read, write, or delete operations are performed
#      - Gives you getter, setter, and deleter functionality


class rectangle:

    def __init__(self, length, width):
        self._length = length  #Meant to be used internally and built upon using @property
        self._width = width

    @property
    def width(self):
        return f"{self._width} is the width of the rectangle."

    @property
    def length(self):
        return f"{self._length} is the length of the rectangle."
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            raise ValueError("Width must be greater than 0.")
        
    @length.setter
    def length(self, new_length):
        if new_length > 0:
            self._length = new_length
        else:
            raise ValueError("Length must be greater than 0.")
        
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.")
    
    @length.deleter
    def length(self):
        del self._length
        print("Length has been deleted.")



rectangle = rectangle(10, 5)

del rectangle.length #deletes length attribute

