print("Welcome to simple calculator...")

num1 = float(input("Give a number :"))
num2 = float(input("Give a number :"))

A = input("Enter a operator :")

if A == "+":
    print(f"Addition = {num1 + num2}")
    
elif A == "-":
    print(f"subtraction = {num1 - num2}")
       
elif A == "*":
    print(f"multiplication = {num1 * num2}")
    
elif A == "/":
    if num2 == "0":
        print('we can division') 
    else:
           
        print(f"division = {num1 / num2}")

elif A == "^":
    print(f'power = {num1 ** num2}') 

elif A == "%":
    print(f"percantage = {num1 / num2 * 100}")

else:
    print("Entered worng operater ")

print("Thank you for using...")     