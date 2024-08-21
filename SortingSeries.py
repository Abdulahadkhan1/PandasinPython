import pandas as pd
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original series")
sorted_sreies = pd.Series(s1).sort_values()
print("sorted series")
print(sorted_sreies)