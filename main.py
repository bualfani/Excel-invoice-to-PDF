import pandas as pd
import glob

filepaths =glob.glob('invoices/*xlsx')

for files in filepaths:
    df = pd.read_excel(files, sheet_name="Sheet 1")
    print(df)