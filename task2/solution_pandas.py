import pandas as pd

# Dictionary with 10 key value pairs. Now convert this Dictionary to Dataframe using Pandas 
data = { 'Name': ['John', 'Doe'],'Age': [28, 30],'Country': ['USA', 'Canada'], 'Occupation': ['Engineer', 'Manager'],'Salary': [75000, 85000], 'Company': ['Tech Corp', 'Innovate Inc'], 'Years_of_Experience': [5, 8], 'Degree': ['Master\'s in Engineering', 'PhD in Computer Science'], 'Marital_Status': ['Single', 'Married'], 'City': ['San Francisco', 'Toronto']}

data_frame = pd.DataFrame(data)
print(data_frame)


print("\n\n")


# drop the row with index 3 from the DataFrame df
data_set = {'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack'],
        'Age': [25, 30, 35, 40, 22, 29, 34, 28, 33, 27],
        'Country': ['USA', 'Canada', 'UK', 'Australia', 'Germany', 'France', 'India', 'China', 'Japan', 'Brazil'],
        'Score': [85, 90, 78, 88, 92, 80, 87, 91, 83, 89] }
df = pd.DataFrame(data_set)
print(df.drop(3))



# Rename the column "old_name" to "new_name"
print("\n",df.rename(columns={'ID':'Unique_ID'}))


# Changing the data type of the column "salary" from int to float:

data_frame['Salary'] = data_frame['Salary'].astype(float)
print(data_frame['Salary'].dtypes)
print(data_frame)
