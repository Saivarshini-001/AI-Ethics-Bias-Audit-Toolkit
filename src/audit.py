import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt

def run_audit():
    model = joblib.load('src/model.pkl')
    df = pd.read_csv('data/sample_data.csv')
    X = df[['age', 'income']]
    
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    # Save SHAP summary
    shap.summary_plot(shap_values, X, show=False)
    plt.savefig('reports/shap_explanation_plot.png')

    # Bias check
    gender_group = df.groupby('gender')['target'].mean()
    bias_summary = f"Prediction Rates by Gender:\n{gender_group}"
    with open('reports/model_bias_summary.txt', 'w') as f:
        f.write(bias_summary)

    print("Audit Complete!")

if __name__ == "__main__":
    run_audit()
