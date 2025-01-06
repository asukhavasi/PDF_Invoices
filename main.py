import pandas as pd
import glob

filepath = glob.glob("Data/*.xlsx")
print(filepath)

for file in filepath:
    df = pd.read_excel(file,sheet_name="Sheet 1")
    print(df)



