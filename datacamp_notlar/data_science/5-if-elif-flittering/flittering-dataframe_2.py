# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
print(cars[cars['drives_right']])
#sel = cars[dr]

# Print sel
#print(sel)