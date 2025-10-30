## 'r' MODE OR read mode to read an existing file ##

with open(r'C:\Users\USER\Documents\Python\Week1\file_handling\myfile.txt','r') as myfile: # r means read mode
 
 text=myfile.read() # it assign the file a variable and allows you to read it.
 print(text)
 

 ## Default file mode ##

with open(r'C:\Users\USER\Documents\Python\Week1\file_handling\myfile.txt') as myfile: # defualt also means 'r' or read mode
 
  text_b=myfile.read() 
  print(text_b)
 
## 'w' MODE or write mode to creates file or write in an existing file (previous data will overwrite)


user_data={
    "Name":"Areeba Shamsi",
    "Age" :22,
    "Country":"Pakistan"
 }
user2_data={
    "Name":"Summiya Shamsi",
    "Age" :17,
    "Country":"Pakistan"
 }
with open(r'C:\Users\USER\Documents\Python\Week1\file_handling\user_info.txt','w') as user_info: # 'w' means write mode to create a file or to rewrite in an existing file
 # we have to give a proper path where we want ur file to be create
  info=user_info.write(str(user_data)) # write() only takes string argumnet as the file is plan text thats why we convert the type
 
 ## 'a' MODE or append mode ( use to add text in an existing file , it will not overwrite the previous text)

user2_data={
    "Name":"Summiya Shamsi",
    "Age" :17,
    "Country":"Pakistan"
 }
with open('user_info.txt','a') as user_info: # add the newer value and will remain the previous data too
  info=user_info.write(str(user2_data)+'/n')
 
## 'rb' MODE or read binary mode ,reads file like an image or audio etc
with open(r'C:\Users\USER\Documents\Python\Week1\file_handling\bird.jpg','rb') as i: 
  myimage=i.read()
print(type(myimage)) #it will give output of the type of image which is binary i.e (<class 'bytes'>)
print(myimage) #it will provide the rgb values of each pixel.

## 'wb' MODE or write binary mode ##

#  use for copying a binary image file into a new binary file , it will ead an existing binary file of an image and copy it and create a new file

with open(r'C:\Users\USER\Documents\Python\Week1\file_handling\binary_bird.jpg','wb') as f:
  f.write(myimage) # an existing image variable that has its binary form.