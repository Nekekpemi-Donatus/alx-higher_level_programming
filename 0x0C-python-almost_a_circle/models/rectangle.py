#!/usr/bin/python3
"""module rectangle.py
creates a rectangle that inherits from the base class
"""


from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle
    Attributes:
    Private instance attributes:
       __width -> width
       __height -> height
       __x -> x
       __y -> y

    method:
    public method:
      -area(self)
      -display(self)
      -update(self, *args)
      -to_dictionary(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle attributes.
        Args:
          - __width: width
          - __height: height
          - __x: x
          - __y: y
          - id: id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attributes."""

        return self.__width

    @property
    def height(self):
        """Retrieves the height attributes"""

        return self.__height

    @property
    def x(self):
        """Retrieves the x attributes"""

        return self.__x

    @property
    def y(self):
        """Retrieves the y attributes"""

        return self.__y

    @width.setter
    def width(self, value):
        """Set the width to value"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height attribute"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the x attributes"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the y attributes"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function that finds the area of the rectangle"""
        area = self.__height * self.__width
        return area

    def display(self):
        """Function prints in stdout the Rectangle
           instance with the character #"""

        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a string representation of a Rectangle instance"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
                             - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Function that assigns an argument to each attribute:"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """Function that returns a dictionary representation of a rectangle"""

        rect_dict = {'id': self.id, 'width': self.__width,
                     'height': self.__height, 'x': self.__x, 'y': self.__y}
        return rect_dict
