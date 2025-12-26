# series as generalized numpy

import pandas as pd
data = pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'])

print(data[: 'd'])

#series as specialized dictionary
population_dist  = {'california' : 654674864,
                    'texas' : 45267,
                    'new york' : 21256,
                    'florida' : 876890,
                    'canada': 786978
}
population = pd.Series(population_dist)
print(population)

# constructing series objects

new = pd.Series([2,4,6])
print(new)

# loading heat disease dataset

data = pd.read_csv("heart_disease.csv")
data = data.head()


# pandas dataframe object

print(data)
area = data['Age'] # converting dataframe into series
print(area)

states = pd.DataFrame({'Age':data['Age'],
                       'Gender':data['Gender']}  
                        )
print(states)
print(states.columns)

# data frame as specialized dictionary
