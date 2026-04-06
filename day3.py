#pip is used to import external modules in the python program
#The syntax is something like this ----> import pandas as pd OR import numpy as np
import numpy as np
x=[1,2,3,45,56]
y=[5,6,7,8,9]
result=  np.absolute(max(x,y))
print(result)