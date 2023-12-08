##NUMPY and pandas
import numpy as np
import pandas as pd
x= np.array ([[1.,2.,3.],
            [10.,100.,100.]])
print(x)
print(x*2)

flowers = pd.read_csv("iris_data.csv")
print(flowers[["Species", "obs", "flower_part"]])
print(flowers.describe())
print(flowers[(flowers["Length"]>5)])

Dans_Thoughts = {'Activity': ['book', 'tv', 'games', 'studying'],
        'Days Since Last time': [1, 0, 11, 0],
        'Enjoyable': ['Yes', 'Yes', 'Yes', 'No']}
df = pd.DataFrame(Dans_Thoughts)

df.to_csv('Dans_Thoughts.csv', index=False)
