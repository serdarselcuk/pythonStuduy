# Import numpy
#%%
# import numpy as np

# # Assign the filename: file
# file = 'digits_header.txt'

# # Load the data: data
# data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])

# #%%
# # Print data
# print(data)


#%% 
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
y = np.random.random(10)

#%% 
plt.plot(x, y)
plt.xlabel("sayilar")

#%%
