# STRING METHODS
# String are immutable means we can't change them inplace
# All string methods doesn't change the original string but create a new copy for the operation
name="Shivpoojan"
print(len(name))   #This method is used to print the length of the string
print(name.upper())  #This method is used to convert full string to uppercase letters
print(name.lower())  #This method is used to convert full string to lowercase letters
string1 = "Hurray!!!!!"
print(string1.rstrip("!")) #This method removes any trailing characters of symbols from the string
print(name.replace("Shivpoojan","Ayush")) # This method replace the all occurences of any string with any other provided string
string2 = "!!!! Hello everybody how are you ?"
print(string2.split(" "))  # This method returns list of parts of strings that are separated by any kind of separator like whitespace
blog = "good morning everybody this is my blog"
print(blog.capitalize())  # This method is used to capitalize the first character of a string
print(blog.center(50)) #This aligns the string in center acc to the given parameters
