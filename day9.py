#TYPE CONVERSION
#THERE ARE TWO TYPES OF DATA TYPE CONVERSION IN PYTHON THE FIRST ONE IS EXPLICIT TYPE CONVERSION AND THE OTHER ONE IS IMPLICIT TYPE CONVERSION.
# EXPLICIT CONVERSION
str = "234"
num = 34
print(int(str)+num)  #Here we are converting the string type into the integer type manually by using int() function and we can use another functions for different data types such as float(), str(), dict() etc.
# IMPLICIT CONVERSION
a=5.78
b=13
print(a+b) #Here python automatically converts the result of a+b into float type as float is greater in heirarchy in comparison to integer.