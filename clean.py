import pandas as pd

# Sample DataFrame

df = pd.read_csv("C:/Users/zaram/Desktop/python/htsdata (47).csv")


# Function to concatenate descriptions based on 'Other' in 'description'
def concat_descriptions(row):
    if row['Description'] == 'Other':
        indent_level = row['Indent']
        previous_rows = df[df['Indent'].between(1, indent_level - 1, inclusive='neither')][::-1]
        concatenated_desc = ' '.join(previous_rows['Description'])
        return concatenated_desc
    else:
        return row['Description']

# Apply the function to create a new column 'concatenated_description'
df['concatenated_description'] = df.apply(concat_descriptions, axis=1)

# Drop duplicates based on 'indent' to avoid repetition
df_result = df.drop_duplicates(subset='Indent')[['Indent', 'concatenated_description']].reset_index(drop=True)

# Display the result
#print(df_result)

df.to_csv("newdata.csv", index=False)