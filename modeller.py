import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt

with open("C:/Users/raeda/NBA-predictor/Processed_Data.pkl", "rb") as f:
    df = pickle.load(f)

inputs = df[["W", "L", "OW", "OL"]]
results = df["W/L"]

accuracy = []

for i in range(1000):

    X_train, X_test, Y_train, Y_test = train_test_split(inputs, results, test_size= 0.1)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy.append(accuracy_score(Y_test, Y_pred))

series = pd.Series(accuracy)
summary = series.describe(percentiles=[.25, .5, .75])
print(summary)

fig = plt.figure()
plt.boxplot(accuracy)
plt.show()

#print("Accuracy:", accuracy_score(Y_test, Y_pred))
#print("Intercept:", model.intercept_)
#feature_names = X_train.columns
#coefficients_dict = {feature_names[i]: model.coef_[0][i] for i in range(len(feature_names))}
#print("Feature Coefficients:", coefficients_dict)
#conf_matrix = confusion_matrix(Y_test, Y_pred)
#print("Confusion Matrix:\n", conf_matrix)