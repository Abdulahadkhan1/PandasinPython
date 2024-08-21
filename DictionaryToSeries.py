import pandas as pd
car = {
    'Model' : ['s','c','a'],
    'speed':[290,300,310],
    'Safety':['100%','99%','100%']
}
print("original dictionary")
print(car)
new_series = pd.Series(car)
print(new_series)