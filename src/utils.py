import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_and_save_model():
    df = pd.read_csv('data/sample_data.csv')
    X = df[['age', 'income']]
    y = df['target']
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, 'src/model.pkl')

if __name__ == "__main__":
    train_and_save_model()
