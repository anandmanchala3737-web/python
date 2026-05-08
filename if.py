weather = input("what is the weather :")
t = "3:30pm"

if weather == "sunny":
    if t == "3:30pm":
     print("you can play cricket")
    else:
        print("you can not play")
        
elif weather == "rainy":
    print("play with car toy")
    
elif weather == "hot":
    if t == "2:30pm":        
       print("play with robot toy")        
    else:
        print("stay home")    
else:
    print("good night")