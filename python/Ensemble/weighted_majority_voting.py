from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import accuracy_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

import re
import pandas as pd
import numpy as np

class MajorityVoting():
    def __init__(self, classifiers, weights=None):
        self.classifiers = classifiers
        if isinstance(weights, list) and len(weights) != len(self.classifiers):
            raise ValueError("len(classifiers) does not match len(weights)")
        else:
            self.weights = weights

    def __str__(self):
        return f"{self.__class__.__name__}(weights={self.weights})"

    def predict_labels(self, X_test):
        prediction_array = []
        for clf in self.classifiers:
            y_predicted = clf.predict(X_test)
            prediction_array.append(y_predicted)
        self.predictions = np.array(prediction_array)
        return self.predictions


    def vote(self, X_test):
        base_predictions = self.predict_labels(X_test)
        ensemble_predictions = []
        num_samples = base_predictions.shape[1]
        for i in range(num_samples):
            votes = base_predictions[:, i]
            ens_pred = np.argmax(np.bincount(votes, weights=self.weights))
            ensemble_predictions.append(ens_pred)
        return np.array(ensemble_predictions)




def main():
    iris = load_iris()
    X, y = iris.data[50:], iris.target[50:]

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.15,
                                                        shuffle=True,
                                                        random_state=42)

    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    # Define models
    clf1 = LogisticRegression(C=0.02, max_iter=50)
    clf2 = DecisionTreeClassifier(max_depth=10)
    clf3 = KNeighborsClassifier(n_neighbors=1)
    clf4 = LogisticRegression(penalty="l2", C=0.06)
    clf5 = LogisticRegression(penalty="l2", C=0.01)

    classifiers = [clf1, clf2, clf3, clf4, clf5]

    eligible_classifiers = []

    performance_metrics = []

    for clf in classifiers:
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        y_true = y_test
        f1 = round(f1_score(y_true, y_pred), 2)
        if f1 > 0.50:
            eligible_classifiers.append(clf)
            performance_metrics.append(f1)
        else:
            print(f"{clf} score is {f1}. not eligible\n")

    # classifier_names = [ re.sub('(?<!^)(?=[A-Z])', ' ', name) for name in classifier_names]


    voter1= MajorityVoting(eligible_classifiers)
    y_pred = voter1.vote(X_test)
    f1 = round(f1_score(y_true,y_pred), 2)
    classifier_names = eligible_classifiers + [voter1]
    performance_metrics.append(f1)

    voter2= MajorityVoting(eligible_classifiers, weights=[0.2, 0.2, 0.9, 0.2])
    y_pred = voter2.vote(X_test)
    f1 = round(f1_score(y_true,y_pred), 2)
    classifier_names.append(voter2)
    performance_metrics.append(f1)

    result = pd.DataFrame({
        "model": classifier_names,
        "f1": performance_metrics
        })

    print(result)

if __name__ == '__main__':
    main()
