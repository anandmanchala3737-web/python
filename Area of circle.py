import math

r = float(input("Give the radius :"))

def area(r):
    print(f"{math.pi * r**2}")

c = area(r)

print(c)