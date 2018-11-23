# Importing the libraries

import pandas as pd

# Importing the Dataset
dataset = pd.read_csv('Train_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values
print("X:",X)
print("Y:",Y)

#Data Preprocessing - Taking care of Missing Data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

# Encoding categorical Data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y = labelencoder_X.fit_transform(Y)


# Splitting the dataset into training and testing(considered 20% of the data as Test data here)
from sklearn.cross_validation import train_test_split
X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.2,random_state = 0)
print(X_Train,X_Test,Y_Train,Y_Test)

# featureScaling
from sklearn.preprocessing import StandardScaler
sc_x= StandardScaler()
X_Train= sc_x.fit_transform(X_Train)
X_Test= sc_x.transform(X_Test)

print(X_Train,X_Test)
