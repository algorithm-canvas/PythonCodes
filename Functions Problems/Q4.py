# Create a function that returns both the area and circumference of a circle given its radius
import math

def cicle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return  area, circumference


a, c = cicle_stats(2)

print("Area: ", a, "Circumference: ", c)