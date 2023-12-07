# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('/content/drive/MyDrive/Crop_Pridiction/crop_production.csv')

# Display the first few rows of the DataFrame
df.head()

# Display the total number of elements (rows * columns) in the DataFrame
df.size

# Get the number of rows and columns in the DataFrame
nr, nc = df.shape
print(nr, nc)

# Display the column names in the DataFrame
df.columns

# Display the data types of each column in the DataFrame
df.dtypes

# Display the number of missing values in each column of the DataFrame
df.isnull().sum()

# Drop rows with missing values from the DataFrame
df.dropna(inplace=True)

# Display unique values for each column in the DataFrame
for i in df.columns:
    print(i, " ", df[i].unique())

# Group data by 'State_Name' and calculate the sum of 'Production' for each state
state_budget = df.groupby('State_Name')['Production'].sum()
state_budget = state_budget.sort_values(ascending=False)

# Create a bar plot of production by state
plt.xlabel('Production')
sns.barplot(x=state_budget.values, y=state_budget.index)

# Group data by 'Crop' and calculate the sum of 'Production' for each crop
crops_budget = df.groupby('Crop')['Production'].sum()
crops_budget = crops_budget.sort_values(ascending=False)

# Create a pie chart of the top 5 crops by production
palette_color = sns.color_palette('bright')
plt.pie(crops_budget[:5].values, labels=crops_budget[:5].index, colors=palette_color, autopct='%.0f%%')
plt.show()

# Create a line plot of production over the years
sns.lineplot(x=df['Crop_Year'], y=df['Production'])

# Group data by 'Crop' and calculate the sum of 'Production' for each crop
top_crops = df.groupby('Crop')['Production'].sum().reset_index()
top_crops_sorted = top_crops.sort_values(by='Production', ascending=False)
top_10_crops = top_crops_sorted[0:10]

# Display the top 10 crops by production
top_10_crops

# Group data by 'State_Name' and 'Crop', then filter for the top 10 crops
grouped_df = df.groupby(['State_Name', 'Crop'])['Production'].sum().reset_index()
top_10_crops = grouped_df[grouped_df['Crop'].isin(top_10_crops['Crop'])]

# Create a stacked bar plot of crop production by state for the top 10 crops
pivot_df = top_10_crops.pivot(index='State_Name', columns='Crop', values='Production')
pivot_df.plot(kind='bar', stacked=True, figsize=(7, 5))
plt.xlabel('State')
plt.ylabel('Production')
plt.title('Crop Production by State')
plt.legend()
plt.show()

# Group data by 'Season' and calculate the sum of 'Production' for each season
season_budget = df.groupby('Season')['Production'].sum()
season_budget = season_budget.sort_values(ascending=False)

# Create a bar plot of production by season
sns.barplot(y=season_budget.values, x=season_budget.index)
