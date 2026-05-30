import pandas as pd
from sklearn.datasets import load_breast_cancer
import os

def download_data():
    """
    Downloads the Breast Cancer dataset from sklearn and saves it as a CSV.
    """
    print("Downloading Breast Cancer dataset...")
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    
    os.makedirs("data/raw", exist_ok=True)
    output_path = "data/raw/dataset.csv"
    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")

if __name__ == "__main__":
    download_data()
