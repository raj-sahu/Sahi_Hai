from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
import joblib
import os
from dotenv import load_dotenv
label = []
data = []

load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH")
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

y = LabelEncoder().fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = MLPClassifier(hidden_layer_sizes=(100, 50, 30, 10, 5),
                    max_iter=1000, activation='relu', solver='adam', random_state=42, verbose=True)

clf.fit(X_train, y_train)

clf.score(X_test, y_test)

y_pred = clf.predict(X_test)
acc = clf.score(X_test, y_test)
print("Accuracy is:", acc)
# cm = confusion_matrix(y_pred, y_test)

joblib.dump(clf, MODEL_PATH, compress=9)
