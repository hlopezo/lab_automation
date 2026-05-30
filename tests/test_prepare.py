import pandas as pd
import numpy as np

# We mock a simple prepare logic to demonstrate pytest
def prepare_data(df, test_size=0.2):
    # Dummy split logic
    split_idx = int(len(df) * (1 - test_size))
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]
    return train, test

def test_prepare_data_split_ratio():
    # Arrange
    df = pd.DataFrame({'feature1': range(100), 'target': range(100)})
    
    # Act
    train, test = prepare_data(df, test_size=0.2)
    
    # Assert
    assert len(train) == 80
    assert len(test) == 20
