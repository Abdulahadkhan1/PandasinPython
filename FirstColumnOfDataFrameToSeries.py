import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("original Data Frame")
print(df)
series_col = df.iloc[:, 0]
print("Column 1 to series is :")
print(series_col)
