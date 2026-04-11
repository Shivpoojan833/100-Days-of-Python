#STRING SLICING AND OPERATIONS ON STRING
name = "Shyam"
place= "Orai"
sirname = "Prasad"
print("Hello, "+name+" "+sirname)
print(name[0]) # 0 based indexing 
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])  #It throws an error because there is no 5th index

for char in name:
    print(char,end=" ")