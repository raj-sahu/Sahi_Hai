from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
import numpy as np
import joblib
import os
from dotenv import load_dotenv

label = []
data = []

load_dotenv()
MODEL_PATH_RF = os.getenv("MODEL_PATH_RF")
with open('./data/web_data.arff') as fh:
    for line in fh:
        line = line.strip()
        temp = line.split(',')
        label.append(temp[-1])
        data.append(temp[0:-1])

X = np.array(data)
y = np.array(label)

X = X[:, [0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12,
          13, 14, 15, 16, 17, 22, 23, 24, 25, 27, 29]]
X = np.array(X).astype(np.float64)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = RandomForestClassifier(random_state=42, verbose=1)
clf.fit(X_train, y_train)
importance = clf.feature_importances_

print(importance)
print(clf.score(X_test, y_test))

joblib.dump(clf, MODEL_PATH_RF, compress=9)
