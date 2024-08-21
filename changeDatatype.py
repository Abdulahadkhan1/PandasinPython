import pandas as pd
s1 = pd.Series(['100','200','python','300.12','400'])
print("Original Data series")
print(s1)
print("Change the said Datatype to numeric:")
s2 = pd.to_numeric(s1, errors = 'coerce')
print(s2)