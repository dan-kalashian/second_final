#numpy and pandas
#imports
import numpy as np
import pandas as pd

#created an array using numpy
x= np.array ([[1.,2.,3.],
            [10.,100.,100.]])

#printed array normally then as modified to have each value doubled
print(x)
print(x*2)

#read csv using pandas
flowers = pd.read_csv("iris_data.csv")
#printed data frame for chosen variables
print(flowers[["Species", "obs", "flower_part"]])
#using panda objects for data analysis
print(flowers.describe())
#print data frame for data where the length variable has a value greater than five
print(flowers[(flowers["Length"]>5)])

#create a dictionary with a few activities, how recently I did them, and if I thought is was enjoyable
Dans_Thoughts = {'Activity': ['book', 'tv', 'games', 'studying'],
        'Days Since Last time': [1, 0, 11, 0],
        'Enjoyable': ['Yes', 'Yes', 'Yes', 'No']}
#used pandas to make this dictionary a data frame
df = pd.DataFrame(Dans_Thoughts)
#wrote this data frame as a CSV file
df.to_csv('Dans_Thoughts.csv', index=False)
