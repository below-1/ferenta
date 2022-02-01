from sklearn.neural_network import MLPClassifier
import numpy as np

FILENAME = 'app/data.csv'

def build_classifier():
    f = open(FILENAME)
    data = np.loadtxt(f, delimiter=",")
    data = data[ data[:, 6] > 0 ]
    print(data.shape)
    X = data[:, 1:-1]
    y = data[:, -1]
    clf = MLPClassifier(alpha=1e-3, random_state=1)
    clf.fit(X, y)
    return clf
