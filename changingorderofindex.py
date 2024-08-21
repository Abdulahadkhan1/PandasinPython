import pandas as pd
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print("Original order of index")
print(s)
d = s.reindex(index = ['B', 'A', 'C','D','E'])
print("after acahnging index")
print(d)