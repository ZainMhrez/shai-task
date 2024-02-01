import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1- Basic Data Exploration
print('1- Basic Data Exploration:')

# Load dataset
df = pd.read_csv('Salaries.csv')
# number of rows and columns
print('number of rows and columns: ',df.shape,'\n')

# data types of each column
print('data types of each column: ')
print(df.dtypes)

# check for missing values in each column
missing_values = df.isnull().sum()
print("Number of missing values: ")
print(missing_values)

print('================================================================')

# 2- Descriptive Statistics
print('2- Descriptive Statistics:')


# mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.
mean_salary = df['TotalPay'].mean()
median_salary = df['TotalPay'].median()
mode_salary = df['TotalPay'].mode()
min_salary = df['TotalPay'].min()
max_salary = df['TotalPay'].max()
range_salary = max_salary - min_salary
std_dev_salary = df['TotalPay'].std()

print('Mean: ',mean_salary)
print('Median: ',median_salary)
print('Min: ',min_salary)
print('Max: ',max_salary)
print('Mode: ',mode_salary)
print('Range: ',range_salary)
print('Standard Deviation: ',std_dev_salary)

print('================================================================')

# 3- Data Cleaning
print('3- Data Cleaning:')

# Handle missing data.

# Notes and Status columns We will delete it because it doesn't have any values
new_df = df.drop(columns=['Notes','Status'])
print('New Columns: ')
print(new_df.columns.tolist())

# For each column in ['BasePay','OvertimePay','OtherPay','Benefits'], we will replace missing values with the column's mean
# Each column has numeric values and pay amount so I think it's a good way to handle missing values
for col in new_df[['BasePay','OvertimePay','OtherPay','Benefits']]:
  new_df[col].fillna(value = new_df[col].mean(), inplace = True)

print(new_df.head())


print('================================================================')

# 4- Basic Data Visualization
print('4- Basic Data Visualization:')

# Plot histogram for the distribution of salaries
plt.figure(figsize=(8, 6))
plt.hist(new_df['TotalPay'], bins=10, color='red', edgecolor='black')
plt.title('Distribution of Salaries')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plot pie chart for the proportion of employees in different departments
plt.figure(figsize=(8, 8))
plt.pie(new_df['JobTitle'].value_counts(), labels=new_df['JobTitle'].unique(), autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Proportion of Employees in Different Departments')
plt.show()

