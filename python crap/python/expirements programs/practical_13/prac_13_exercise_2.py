import numpy
import numpy as np
a=np.array(["Ronit"], dtype = np.str)
b=np.array(["mehta"], dtype = np.str)
print("the first name:-",a)
print("the last name:-",b)
full_name = np.char.add(a, b)
print(full_name)
