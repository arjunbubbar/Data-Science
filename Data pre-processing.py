import pandas as pd

from sklearn.impute import SimpleImputer

data = pd.read_csv ("/Users/arjunbubbar/Desktop/Jetlearn/Data Science/Datasets/Data.csv")

data.info ()

# check for missing values in the dataset (true indicates missing), sum adds up every number of values in the column

print (data.isna ().sum ())

# removing missing values
 
# data.dropna (inplace = True)

# print (data.isna (). sum())

# manually replacing missing values, you specify which column you want to replace

data.loc [data ['Age'].isna (), 'Age'] = data ['Age'].median ()

print (data)

# automated process to replace data, imputing values, sk learn library

impute = SimpleImputer (missing_values = pd.NA, strategy = 'median')

data [['Age', 'Salary']] = impute.fit_transform (data [['Age', 'Salary']])

print (data)

# features independent X (many so capital x), target dependent y (one)

X = data [['Age', 'Salary', 'Country']]

y = data ['Purchased']

# encoding categorical values - changing categorical values into numbers - for ML only works with numbers

# encoding features, presented in numbers 

encf = pd.get_dummies (X, columns=['Country'], dtype = int)

print (encf)

# encoding target











