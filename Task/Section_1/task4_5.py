import math

PI = math.pi

def area(shape, *args):
    if shape == "circle":
        return PI * args[0]**2
    elif shape == "square":
        return args[0]**2
    elif shape == "triangle":
        return 0.5 * args[0] * args[1]

def perimeter(shape, *args):
    if shape == "circle":
        return 2 * PI * args[0]
    elif shape == "square":
        return 4 * args[0]
    elif shape == "triangle":
        return sum(args)