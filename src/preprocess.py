"""Load + Preprocess Dataset. DataSet is already clean."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_data(path: str = "data/student-mat.csv"):
    df = pd.read_csv(path, sep=";")
    return df

def preprocess(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Preprocess the student performance dataset. 80% train, 20% test split."""
    df = df.copy()

    # transform categorical columns to numerical using Label Encoding
    le = LabelEncoder()
    for col in df.select_dtypes( include=["object"] ).columns:
        df[col] = le.fit_transform(df[col])


    df['pass'] = (df['G3'] >= 10).astype(int)

    # drop original target columns
# This is the list of 15 features from your image
    features_selected = [
        'failures', 
        'absences', 
        'goout', 
        'freetime', 
        'internet', 
        'schoolsup', 
        'paid', 
        'Medu', 
        'age', 
        'famsize', 
        'Mjob', 
        'guardian', 
        'health', 
        'traveltime', 
        'Pstatus'
    ]

    X = df[features_selected]
    Y = df['pass']


    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2,
        random_state=42 # for reproducibility. same split every time
    )

    return X_train, X_test, y_train, y_test



if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess(load_data())
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

