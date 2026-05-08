a = float(input("Enter temperature:"))
b = input("Enter units(K or F or C):").upper()

if b == "C":
    print(f"Temperature in Fahrenheit:{(a*9/5)+32:.2f}F")
    print(f"Temperature in Kelvin: {a + 273.15:.2f}K")
    
elif b == "F":
    print(f"Temperature in Celsius:{(a-32)*5/9:.2f}C")
    print(f"Temperature in Kelvin: {(a - 32) * 5/9 + 273.15:.2f}K")
    
elif b == "K":
    if a < 0:
       print("Kelvin cannot be negative.")
    
    else:
        print(f"Temperature in Celsius:{a-273.15:.2f}C")
        print(f"Temperature in Fahrenheit:{(a-273.15)*9/5+32:.2f}F")
    
    
else:
    print("Entered wrong units use only K, F, or C") 
    
   