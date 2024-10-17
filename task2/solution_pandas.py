import pandas as pd

# Dictionary with 10 key value pairs. Now convert this Dictionary to Dataframe using Pandas 
data = { 'Name': ['John', 'Doe'],'Age': [28, 30],'Country': ['USA', 'Canada'], 'Occupation': ['Engineer', 'Manager'],'Salary': [75000, 85000], 'Company': ['Tech Corp', 'Innovate Inc'], 'Years_of_Experience': [5, 8], 'Degree': ['Master\'s in Engineering', 'PhD in Computer Science'], 'Marital_Status': ['Single', 'Married'], 'City': ['San Francisco', 'Toronto']}

print(pd.DataFrame(data))
