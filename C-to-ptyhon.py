# n=int(input())
# i=1
# while i<=n:
#     print(i,end="")
#     i += 1


# a=input()
# Nlist=a.split()
# new_Nlist=list(map(int,Nlist))
# new_Nset=set(new_Nlist)


# b=input()
# Mlist=b.split()
# new_Mlist=list(map(int,Mlist))
# new_Mset=set(new_Mlist)


# c=new_Nset.intersection(new_Mset)
# d=sorted(list(new_Nset.difference(c).union(new_Mset.difference(c))))

# for i in d:
#     print(i) 


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# result=[[i,j,k]
    
# for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k)!=n)
#                 ]
# print(result)
            
# n = int(input())
# arr = list(map(int, input().split()))
    
# arr.sort(reverse=True)
    
# for i in range(len(arr)):
#     if(arr[i]>arr[i+1]):
#         break
    
# print(arr[i+1])

# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     list1=list([name][score])
    
# print(list[0])
    
# from gtts import gTTS
# import os
# text ="Hello world"
# language ="en"
# speech = gTTS(text=text, lang=language, slow=False)
# speech.save("output.mp3")    
  
# from moviepy.editor import TextClip, compositeVideoClip

# text = TextClip(
#                "Hello Anand", 
#                fontsize=70, 
#                size(1280,720),
#                color='while'
#             )
# text = text.set_duration(5)

# video = compositeVideoClip([text])
# video.write_videofile("output2.mp4",fps=24)

from moviepy.editor import TextClip, CompositeVideoClip

text = TextClip(
    "Helo Anand",
    fontsize=70,
    size=(1280, 720),   # ✅ equal sign added
    color='white'
)

text = text.set_duration(5)

video = CompositeVideoClip([text])
video.write_videofile("output2.mp4", fps=24)