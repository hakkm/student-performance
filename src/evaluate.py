"""Evaluate the trained model on the test dataset and print performance metrics."""

from joblib import load
from preprocess import load_data, preprocess
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def evaluate():
    df = load_data()
    _, X_test, _, y_test = preprocess(df)

    model = load("models/student_performance.joblib")

    y_pred =  model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluate()
