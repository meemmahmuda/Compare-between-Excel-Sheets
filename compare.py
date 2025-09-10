# import pandas as pd

# df1 = pd.read_excel("dbbl.xlsx", sheet_name="Sheet1")
# df2 = pd.read_excel("dncc.xlsx", sheet_name="Sheet1")


# merged = pd.merge(df1, df2, left_on='Txn ID', right_on='Tranno', how='outer', indicator=True)



# matched = merged[merged['_merge'] == 'both']
# unmatched = merged[merged['_merge'] != 'both']


# unmatched.to_excel("unmatched_both.xlsx", index=False)

# print("Done! Files created: matched_both.xlsx, unmatched_both.xlsx")


import pandas as pd
from tkinter import Tk, filedialog, simpledialog
import os

root = Tk()
root.withdraw()

def load_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        return pd.read_csv(file_path)
    elif ext == ".xlsx":
        return pd.read_excel(file_path, sheet_name=0)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

file1 = filedialog.askopenfilename(
    title="Select first file",
    filetypes=[("Excel or CSV files", "*.xlsx *.csv")]
)

file2 = filedialog.askopenfilename(
    title="Select second file",
    filetypes=[("Excel or CSV files", "*.xlsx *.csv")]
)

df1 = load_file(file1)
df2 = load_file(file2)

df1_columns_lower = {col.lower(): col for col in df1.columns}
df2_columns_lower = {col.lower(): col for col in df2.columns}

col1_input = simpledialog.askstring("Input", "Enter column name from first file to compare:").strip().lower()
col2_input = simpledialog.askstring("Input", "Enter column name from second file to compare:").strip().lower()

col1 = df1_columns_lower.get(col1_input)
col2 = df2_columns_lower.get(col2_input)

if not col1 or not col2:
    raise ValueError("Column not found in one of the files. Check spelling.")

merged = pd.merge(df1, df2, left_on=col1, right_on=col2, how='outer', indicator=True)

unmatched = merged[merged['_merge'] != 'both']

unmatched_file = filedialog.asksaveasfilename(
    title="Save unmatched file as",
    defaultextension=".xlsx",
    filetypes=[("Excel files", "*.xlsx")]
)
if unmatched_file:
    unmatched.to_excel(unmatched_file, index=False)
    print(f"Done! Unmatched data saved to {unmatched_file}")
