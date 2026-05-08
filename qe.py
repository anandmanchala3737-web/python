a = int(input("Give a value :"))
b = int(input("Give b value :"))
c = int(input("Give c value :"))

D = b**2-4*a*c

r1 = (-b+D**(0.5))/(2*a)
r2 = (-b-D**(0.5))/(2*a)

print(f"Roots ={(r1,r2)}")