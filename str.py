# import cv2
# import string
# import os
# d={}
# c={}

# for i in range(225):
#     d[chr(i)]=i
#     c[i]=chr(i)




# x=cv2.imread("1.jpg")

# i=x.shape[0]
# j=x.shape[1]

# key= input("Enter key to edit: ")
# text= input("Enter text to show:")

# k1=0
# tln=len(text)
# z=0
# n=0
# m=0

# l=len(text)

# for i in range(1):
#     x[n,m,z]=d[text[i]]^d[key[k1]]
#     n=n+1
#     m=m+1
#     m=(m+1)%3
#     k1=(k1+1)%len(key)
    
#     cv2.imwrite("Encrypted_img.jpg",x)
    
#     os.startfile("Encrypted_img.jpg")

import cv2
import os

# Create dictionaries
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Read image
img = cv2.imread(r"C:\Users\admin\Documents\python project")

rows, cols, channels = img.shape


key = input("Enter key: ")
text = input("Enter text to hide: ")

key_len = len(key)
text_len = len(text)

if text_len > rows * cols:
    print("Text too long for this image!")
    exit()

n = m = z = 0
k = 0

for i in range(text_len):
    img[n, m, z] = d[text[i]] ^ d[key[k]]

    m += 1
    if m == cols:
        m = 0
        n += 1

    k = (k + 1) % key_len

# Save encrypted image
cv2.imwrite("Encrypted_img.jpg", img)
os.startfile("Encrypted_img.jpg")

print("Text hidden successfully!")
