# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars.iloc[0:3])

# Print out fourth, fifth and sixth observation
print(cars.iloc[3:6])