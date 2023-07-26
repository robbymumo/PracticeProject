# Calculate area of polygons
import math


class Calculator:
    def __init__(self):
        pass

    def calculate(self, shape):
        shape = shape.lower()
        if shape == 'square':
            side = int(input('Enter the dimensions of the side: > '))
            return side * side
        elif shape == 'rectangle':
            length = int(input('Enter the length - '))
            width = int(input('Enter the width - '))
            return length * width
        elif shape == 'triangle':
            base = int(input('Enter the base - '))
            height = int(input('Enter the height - '))
            return 0.5 * base * height
        elif shape == 'circle':
            radius = int(input('Enter the radius: > '))
            return math.pi * radius ** 2
        else:
            print('Unsupported Polygon')


calculator = Calculator()
shape = input('Choose the shape: Circle, square, triangle, rectangle: >')
area = calculator.calculate(shape)
print(f'The area of {shape} is {area} cm^2')
