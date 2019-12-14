# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
#print(cars)
# Extract drives_right column as Series: dr
dr = cars['drives_right']
#print(dr)

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)
