a=1458746357235789
b=True #boolean type variable
c=None  #Nonetype variable
d=complex(2,3)
print(a)
fname="Aman"
lname = "Tiwari"
print(fname)
#print(a+fname) #This print() statement throws error ncz for concatinating two data types they have to be same not different.
print(fname+" "+lname)
print(d)
print("The type of fname is ",type(fname)) #type() function is used to check the data type of a variable and we pass variable inside the paranthesis
print("The type of a is ",type(a))
print("The type of b is ",type(b))
print("The type of c is ",type(c))
print("The type of d is ",type(d))

#Sequenced Data
list1 = [1,2,3,["apple","kiwi","Lichi"],4]
print(list1) #We can include data elements of different data types and we can change the list items at any time (mutable)

tuple1=("lion","tiger","sparrow","giraffe")
print(tuple1)  #Tuple are like list but they are immutable hence they cannot be changed at later in the code

# Mapped Data
dict1 = {1:"One",2:"Two",3:"Three",4:"Four"}
print(dict1)  #This is also called the key value pairs of the python as every item is combined with a key.
#Every thing in python is an object like dictionary, boolean, integer, list etc., . Because python is an onject oriented programming language.
