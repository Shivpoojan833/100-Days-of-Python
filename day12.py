#STRING SLICING AND OPERATIONS ON STRING
name = "Shyam"
place= "Orai"
sirname = "Prasad"
# print("Hello, "+name+" "+sirname)
# print(name[0]) # 0 based indexing 
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])  #It throws an error because there is no 5th index

# for char in name:
#     print(char,end=" ")
    
# print(name[0:5]) #We can print string or parts of strings using indexing based slicing 
# print(name[:5])  #we can give nothing alongside the colons as the python takes default values as 0 and length of the string
# print(name[0:len(place)-2])
print(place[-5:])  #In python negative indexing also exists but it works like if str[-3:-1] then it is interpreted as len(str)-3:len(str)-1 so str[2:4]
# print(len(name))  #Used to retrieve length of any string
nm="Harry"
print(nm[-4:-2])  #It gives ar as output