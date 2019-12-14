# Definition of radius
r = 192500

# Import radians function of math package
from math import radians as rad

# Travel distance of Moon over 12 degrees. Store in dist.
phi = 12
dist = rad(r*phi)

# Print out dist
print(dist)