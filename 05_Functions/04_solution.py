import math

def circlecalci(r):
    return 2*math.pi*r, math.pi*(r**2)

print(circlecalci(7))

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(3)

print("Area: ", a, "Circumference: ", c)