from matplotlib import pyplot as plt

# Get the extremes for number of chips
firsteqx = [6.5, 0]
firsteqy = [0, 13]

# Get the extremes for values
seceqx = [4.4,0]
seceqy = [0,-22]

# Plot the lines
plt.plot(firsteqx,firsteqy, color='blue')
plt.plot(seceqx, seceqy, color="orange")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()