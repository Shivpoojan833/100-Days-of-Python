# IN THIS WE ARE LAERNING STRINGS AND ITS FUNCTIONALITIES MORE DEEPLY
msg = "Hello my name is ABCD"
print(msg[0])  #Strings are like the array of characters that have the index positions that starts with 0 so a string with length 5 has indexing from 0 to 4
# print(msg[22])  In this print statement we are accessing 22th index of the string msg but it is not present in the string because python counts blankspace also as a character so this gives an error 
for ch in msg:
    print(ch,end=" ")  #This is a demonstration of how the characters are placed in a string and how can we print them in a sequence
    
# We also make multiline strings using '''string'''  OR  """string""" , we can span the string into multiple lines and we can use different annotations like " inside the string using different string denotions.

str1 = '''This is a 
multiline string and it can be written within triple double quotes'''
print(str1)

str2 = '''Hello "I am a Python Programmer'''
print(str2)