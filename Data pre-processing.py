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

# data.loc [data ['Age'].isna (), 'Age'] = data ['Age'].median ()

# print (data)

# automated process to replace data, imputing values, sk learn library, fit transform transforms values

impute = SimpleImputer (missing_values = pd.NA, strategy = 'mean')

data [['Age', 'Salary']] = impute.fit_transform (data [['Age', 'Salary']])

print (data)

# features independent X (many so capital x), target dependent y (one)

X = data [['Age', 'Salary', 'Country']]

y = data ['Purchased']

# encoding categorical values - changing categorical values into numbers - for ML only works with numbers

# encoding features, presented in numbers 

encf = pd.get_dummies (X, columns = ['Country'], dtype = int)

print (encf)


# transformers property takes list with tuple, tuple will have first thing as string encoder, second thing is object of type of encoder, 
# third is index of column to be encoded, remainder passthrough means no changes to the remaining columns

# get dummies considers current data and transforms, if category is missing then number of resulting columns will be less,
# one hot encoder fit transform learns about the category and transforms the data
# and when it is used again on a different dataset it still has the learning which it can apply on the new dataset using only the transform function  

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer (transformers = [('encoder',OneHotEncoder (),[2])], remainder = 'passthrough')

Z = ct.fit_transform (X)

print (Z)

c = data [data ['Country'] == 'France']

encodecountry = pd.get_dummies (c, columns = ['Country'], dtype = int)

print (encodecountry)

transformencode = ct.transform (c)

print (transformencode)

# encoding target - label encoding, same process does not work for target like we use for features, 
# converts yes and no to 1 and 0, no is 0 yes is 1, since alphabetical, label encoder can be used for features

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder ()

p = le.fit_transform (y)

print (p)

# scaling brings data closer to eachother, because they can be biased to big values, can impact performance of model, smaller scale better
# mean value 0 sd 1, therefore positive and negative values
# min max scaling eliminates negative values, and represents data between 0 and 1

from sklearn.preprocessing import StandardScaler

ss = StandardScaler ()

print (ss.fit_transform (X [['Salary']]))

from sklearn.preprocessing import MinMaxScaler

mms = MinMaxScaler ()

print (mms.fit_transform (X [['Salary']]))

























