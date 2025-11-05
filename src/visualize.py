import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from joblib import load
from preprocess import load_data, preprocess
import graphviz
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

def visualize_tree():
    df = load_data();
    X_train, X_test, y_train, y_test = preprocess(df)
    model = load("models/student_performance.joblib")
    
    dot_data = tree.export_graphviz(
        model,
        out_file=None,
        feature_names=X_train.columns,
        class_names=["Fail", "Pass"],
        filled=True, rounded=True
    )
    graph = graphviz.Source(dot_data)
    graph.render("models/student_tree")

    # Feature importance plot
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(importances)), importances[indices])
    plt.xticks(range(len(importances)), X_train.columns[indices], rotation=90)
    plt.title("Feature Importance")
    plt.tight_layout()
    plt.show()

def treeDepth_vs_Accuracy():
    df = load_data();
    X_train, X_test, y_train, y_test = preprocess(df)

    depths = range(1, 21)
    accuracies = []

    for depth in depths:
        model = DecisionTreeClassifier(max_depth=depth)
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
        accuracies.append(accuracy)

    plt.figure(figsize=(10, 6))
    plt.plot(depths, accuracies, marker='o')
    plt.title("Tree Depth vs. Accuracy")
    plt.xlabel("Tree Depth")
    plt.ylabel("Accuracy")
    plt.xticks(depths)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    visualize_tree()
    treeDepth_vs_Accuracy()
