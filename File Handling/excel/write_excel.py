import pandas as pd
# import openpyxl

data = {"Name": ["John","Alice","Bob"], "Age":[30,25,35]}
df = pd.DataFrame(data)

df.to_excel("output.xlsx", index = False)