def invert_dict(d):
    inverted_dict={}
    for key, value in d.items():
        inverted_dict[value]=key
    return inverted_dict

n=int(input("Enter the number of key value pairs in the dictionary:"))
d={}
for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value:")
    d[key]=value

print("Original dictionary")
print(d)
inverted_d=invert_dict(d)
print("Inveret dictionsry")
print(inverted_d)