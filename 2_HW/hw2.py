# Standard imports
import os

# Third-party imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from ucimlrepo import fetch_ucirepo 

# Local imports

# This updates plotting styles this is seaborns plotting styles
sns.set()
iris = fetch_ucirepo(id=53) 

X = iris.data.features  # This is already a DataFrame
Y = iris.data.targets   # This is also a DataFrame

df = pd.concat([X, Y], axis=1)  # Combines them side by side
df.rename(columns={'class': 'species'}, inplace=True)

# Check the first 5 rows
# print(df.head())
# print(df.isnull().sum())
# print(X)
# print(Y)

# Split testing data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

# Normalize the data
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)


# print(X_train_scaled)
# print(X_test_scaled)

# Predictions
# for k in range(1, 11):
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
# No accuracy change when I tried to change K from 1-10
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy for {10}: {accuracy}")
print(len(X_train), len(X_test))  # Make sure they're different sizes

print("DONE\n")

# I got sussed out and plotted it to see if there was clear seperation
# Because the accuracy BARLEY CHANGED
# sns.pairplot(df, hue="species")
# plt.show()