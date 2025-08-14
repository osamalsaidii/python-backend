import math

class Shape:
    def __init__(self, name):
        self._name = name  
    
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def __str__(self):
        return f"{self._name} Shape"
    
    def __repr__(self):
        return f"{self.__class__.__name__}()"
    
  
    def __add__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() + other.area()

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.__radius = radius  
    

    @property
    def radius(self):
        return self.__radius
    
    def area(self):
        return math.pi * self.__radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.__radius
    
    def __str__(self):
        return f"{self._name} with radius {self.__radius}"
    
    def __repr__(self):
        return f"Circle(radius={self.__radius})"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.__width = width   
        self.__height = height 
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        return f"{self._name} with width {self.__width} and height {self.__height}"
    
    def __repr__(self):
        return f"Rectangle(width={self.__width}, height={self.__height})"




def print_shape_info(shape):
    print(f"Shape: {shape}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print()

def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 7)
    
    shapes = [circle, rectangle]
    
    for shape in shapes:
        print_shape_info(shape)
    

    total_area = circle + rectangle
    print(f"Total area of circle and rectangle: {total_area:.2f}")
    
    
    print(repr(circle))
    print(repr(rectangle))

if __name__ == "__main__":
    main()
