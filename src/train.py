from preprocess import load_data, preprocess

from sklearn.tree import DecisionTreeClassifier
from joblib import dump



def train():
    df = load_data();
    X_train, X_test, y_train, y_test = preprocess(df)

    model = DecisionTreeClassifier(
            criterion='entropy', # gini impurity
            max_depth=6,
            random_state=42 # for reproducibility
            )
    model.fit(X_train, y_train)


    dump(model, "models/student_performance.joblib")

    print("Model trained and saved to models/student_performance.joblib")


if __name__ == "__main__":
    train()
    evaluate()
    visualize_tree()
