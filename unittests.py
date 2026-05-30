import os
import yaml
import pandas as pd
import numpy as np

def test_download_data(download_func):
    """Grader for Task 0: Data Download"""
    print("Running Task 0 Autograder (Data Download)...")
    try:
        # We can't easily mock the sklearn call without complexity, 
        # but we can test if the function produces the expected output file.
        # For the sake of the autograder, we'll just check if it returns/produces data.
        import os
        if os.path.exists("data/raw/dataset.csv"):
            os.remove("data/raw/dataset.csv")
            
        download_func()
        
        assert os.path.exists("data/raw/dataset.csv"), "File data/raw/dataset.csv was not created"
        df = pd.read_csv("data/raw/dataset.csv")
        assert 'target' in df.columns, "Target column missing in downloaded data"
        assert len(df) > 500, "Dataset seems too small for Breast Cancer dataset"
        
        print("[SUCCESS] Task 0: Data download logic is correct!\n")
    except Exception as e:
        print(f"[FAIL] Task 0: {e}\n")

def test_prepare_script(prepare_func):
    """Grader for Task 1: Data Preparation"""
    print("Running Task 1 Autograder (Data Preparation)...")
    try:
        # Create dummy data
        df = pd.DataFrame({
            'feature1': np.random.rand(100),
            'feature2': np.random.rand(100),
            'target': np.random.randint(0, 2, 100)
        })
        
        train, test = prepare_func(df, split_ratio=0.2, seed=42)
        
        assert len(train) == 80, f"Expected train size 80, got {len(train)}"
        assert len(test) == 20, f"Expected test size 20, got {len(test)}"
        assert 'target' in train.columns, "Target column missing in train set"
        
        print("[SUCCESS] Task 1: Data preparation logic is correct!\n")
    except Exception as e:
        print(f"[FAIL] Task 1: {e}\n")

def test_train_script(train_func):
    """Grader for Task 2: Model Training"""
    print("Running Task 2 Autograder (Model Training)...")
    try:
        X_train = np.random.rand(100, 5)
        y_train = np.random.randint(0, 2, 100)
        
        model = train_func(X_train, y_train, n_estimators=10, max_depth=5)
        
        from sklearn.base import is_classifier
        assert is_classifier(model), "Returned object is not a classifier"
        
        print("[SUCCESS] Task 2: Model training logic is correct!\n")
    except Exception as e:
        print(f"[FAIL] Task 2: {e}\n")

def test_dvc_config():
    """Grader for DVC Configuration"""
    print("Running DVC Config Autograder...")
    if not os.path.exists('dvc.yaml'):
        print("[FAIL] dvc.yaml not found. Did you run 'dvc stage add'?")
        return
    
    with open('dvc.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    stages = config.get('stages', {})
    if 'prepare' not in stages:
        print("[FAIL] 'prepare' stage missing in dvc.yaml")
        return
    
    if 'train' not in stages:
        print("[FAIL] 'train' stage missing in dvc.yaml")
        return

    print("[SUCCESS] DVC configuration looks good!\n")

def test_github_actions_workflow():
    """Grader for GitHub Actions Workflow"""
    print("Running GitHub Actions Autograder...")
    workflow_path = '.github/workflows/ml_ci.yml'
    if not os.path.exists(workflow_path):
        print(f"[FAIL] {workflow_path} not found.")
        return
    
    with open(workflow_path, 'r') as f:
        content = f.read()
    
    checks = {
        'flake8': "Linting (flake8) missing.",
        'pytest': "Unit testing (pytest) missing.",
        'cache:': "Dependency caching missing.",
        'dvc pull': "Data verification (dvc pull) missing.",
        '$GITHUB_STEP_SUMMARY': "Automated reporting missing."
    }
    
    failed = False
    for check, msg in checks.items():
        if check not in content:
            print(f"[FAIL] {msg}")
            failed = True
            
    if not failed:
        print("[SUCCESS] GitHub Actions workflow looks correctly configured for enterprise CI!\n")
