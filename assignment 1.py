#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


# In[3]:


iris = datasets.load_iris()
X = iris.data  # Features
Y = iris.target  # Labels


# In[4]:


X_filtered = X[Y != 2]
Y_filtered = Y[Y != 2]


# In[5]:


num_cases = len(X_filtered)


# In[6]:


print("First 10 cases of X:")
print(X_filtered[:10])
print("Corresponding labels (Y):")
print(Y_filtered[:10])


# In[7]:


attributes = iris.feature_names


# In[8]:


mean_values = np.mean(X_filtered, axis=0)
std_values = np.std(X_filtered, axis=0)
for i, attribute in enumerate(attributes):
    print(f"{attribute}:")
    print(f"  Mean: {mean_values[i]}, Standard Deviation: {std_values[i]}")


# In[9]:


X_train, X_test, y_train, y_test = train_test_split(X_filtered, Y_filtered, test_size=0.3, random_state=42)


# In[10]:


svc = SVC(kernel='linear')
svc.fit(X_train, y_train)


# In[11]:


sample_data = np.array([[5.1, 3.5, 1.4, 0.2],  # Should be predicted as setosa (label 0)
                        [6.0, 3.0, 4.5, 1.5],  # Should be predicted as versicolor (label 1)
                        [4.8, 3.2, 1.6, 0.1]]) # Should be predicted as setosa (label 0)

sample_predictions = svc.predict(sample_data)
print("Predictions for sample data:")
print(sample_predictions)


# In[12]:


y_pred = svc.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy on test set: {accuracy}")


# In[13]:


if accuracy >= 0.95:
    print("SVC classifier achieved 95% or better accuracy!")
else:
    print("SVC classifier did not achieve 95% accuracy.")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names[:2]))


# In[ ]:




#OutPut
"""First 10 cases of X:
[[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]
 [4.6 3.1 1.5 0.2]
 [5.  3.6 1.4 0.2]
 [5.4 3.9 1.7 0.4]
 [4.6 3.4 1.4 0.3]
 [5.  3.4 1.5 0.2]
 [4.4 2.9 1.4 0.2]
 [4.9 3.1 1.5 0.1]]
Corresponding labels (Y):
[0 0 0 0 0 0 0 0 0 0]


sepal length (cm):
  Mean: 5.471000000000003, Standard Deviation: 0.6384817930058776
sepal width (cm):
  Mean: 3.099, Standard Deviation: 0.4763391648814948
petal length (cm):
  Mean: 2.861, Standard Deviation: 1.4422825659349836
petal width (cm):
  Mean: 0.7859999999999999, Standard Deviation: 0.5623201934841042
  
  SVC(kernel='linear')
  
  Predictions for sample data:
[0 1 0]


Accuracy on test set: 1.0

SVC classifier achieved 95% or better accuracy!

Classification Report:
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        17
  versicolor       1.00      1.00      1.00        13

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30"""