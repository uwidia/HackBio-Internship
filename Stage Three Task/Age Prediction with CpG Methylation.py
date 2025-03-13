import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("/content/CpGmeth2Age.csv")

df.head()

df.drop("Unnamed: 0", axis = 1, inplace = True)
#check for duplicate values
df.duplicated().sum()

#check for NaN or null values
df[(df.isnull().sum(axis=1) != 0)]

#Examine the age variable
df.Age.describe()

#Predict the age of the patients

N_features = []
mserror = []


for n_components in [90, 80, 70, 60, 50, 40, 30, 20, 10]:
  pca = PCA(n_components=n_components)
  X_pca = pca.fit_transform(df.drop('Age', axis = 1))

  y = df['Age']

  X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)


  model = LinearRegression()
  model.fit(X_train, y_train)


  y_pred = model.predict(X_test)
  mse = mean_squared_error(y_test, y_pred)
  print(f"Mean Squared Error for {n_components}: {mse}\n")
  N_features.append(n_components)
  mserror.append(mse)

print("As the number of features reduces, we can see a sharp increase in the accuracy of the model, shown by a reduction in the mean squared error values")

plt.plot(N_features, mserror)
plt.xlabel("Number of features")
plt.ylabel("Mean Squared Error")
plt.title("Number of features vs Mean Squared Error")

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.gca().invert_xaxis()

print("As the number of features reduces, the mse fluctuates. However, the overall trend is that the mse decreases as the number of features decreases, especially after the number of features reaches 40.")

