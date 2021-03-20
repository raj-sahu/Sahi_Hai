import warnings
import joblib
import features_extraction
import sys
import numpy as np

from features_extraction import MODEL_PATH


def predict(test_url):
    features_test = features_extraction.main(test_url)
    features_test = np.array(features_test).reshape((1, -1))

    clf = joblib.load(MODEL_PATH)

    pred = clf.predict(features_test)
    print(test_url)
    print(pred)
    return int(pred[0])


def main():
    url = sys.argv[1]
    # url = "https://pricehistory.in/?url=https%3A%2F%2Fai.google%2Feducation%2F"

    prediction = predict(url)
    if prediction == 1:
        print("SAFE")
    else:
        print("PHISHING")


if __name__ == "__main__":
    main()
