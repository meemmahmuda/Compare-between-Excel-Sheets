# import pandas as pd

# df1 = pd.read_excel("dbbl.xlsx", sheet_name="Sheet1")
# df2 = pd.read_excel("dncc.xlsx", sheet_name="Sheet1")

# matched = df1[df1['Txn ID'].isin(df2['Tranno'])]
# unmatched = df1[~df1['Txn ID'].isin(df2['Tranno'])]

# matched.to_excel("matched.xlsx", index=False)
# unmatched.to_excel("unmatched.xlsx", index=False)


import pandas as pd


df1 = pd.read_excel("dbbl.xlsx", sheet_name="Sheet1")
df2 = pd.read_excel("dncc.xlsx", sheet_name="Sheet1")


merged = pd.merge(df1, df2, left_on='Txn ID', right_on='Tranno', how='outer', indicator=True)


merged.to_excel("comparison.xlsx", index=False)


matched = merged[merged['_merge'] == 'both']
unmatched = merged[merged['_merge'] != 'both']

matched.to_excel("matched_both.xlsx", index=False)
unmatched.to_excel("unmatched_both.xlsx", index=False)

print("Done! Files created: comparison.xlsx, matched_both.xlsx, unmatched_both.xlsx")


# import pandas as pd

# # Load Excel files
# df1 = pd.read_excel("dbbl.xlsx", sheet_name="Sheet1")
# df2 = pd.read_excel("dncc.xlsx", sheet_name="Sheet1")

# # Convert columns to string
# df1['Txn ID'] = df1['Txn ID'].astype(str)
# df2['Tranno'] = df2['Tranno'].astype(str)

# # Merge on the converted columns
# merged = pd.merge(df1, df2, left_on='Txn ID', right_on='Tranno', how='outer', indicator=True)

# # Save full comparison
# merged.to_excel("comparison.xlsx", index=False)

# # Separate matched and unmatched
# matched = merged[merged['_merge'] == 'both']
# unmatched = merged[merged['_merge'] != 'both']

# matched.to_excel("matched_both.xlsx", index=False)
# unmatched.to_excel("unmatched_both.xlsx", index=False)

# print("✅ Done! Files created: comparison.xlsx, matched_both.xlsx, unmatched_both.xlsx")
