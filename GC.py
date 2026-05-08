a = int(input("Give the marks in Maths :"))
b = int(input("Give the marks in Science :"))
c = int(input("Give the marks in English :"))

d = a+b+c
print(f"Total Marks: {d},")

A = (d/300)*100
print(f"Average Marks: {A},")

if A > 80:
    print(f"Grade:A")
    
elif A > 60:
    print(f"Grade:B")
    
elif A > 40:
    print(f"Grade:c")
    
else:
    print(f"Grade:D")        