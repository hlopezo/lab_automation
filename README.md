# Lab Automation: MLOPS End-to-End Pipeline

This repository contains the materials for Session 3 of the MLOPS course.

## 🎓 Teacher's Presentation Guide (Demo Checklist)

To present this lab effectively tomorrow morning, follow this flow:

### 1. The "Why" (3-minute Intro)
*   **The Problem**: Manual scripts are "black boxes." If data changes or we change a parameter, we lose track.
*   **The Solution**: We are building a **Reproducible Machine Learning Pipeline**.
    *   **DVC**: Versioning for data and pipeline orchestration (The "Makefile" for ML).
    *   **MLflow**: The "flight recorder" for experiments.
    *   **GitHub Actions**: Continuous Training (CT) on every push.

### 2. Live Demo Steps
1.  **Environment Setup**:
    ```bash
    bash setup_lab.sh
    source .venv/bin/activate
    ```
2.  **DVC Pipeline**:
    *   Show `dvc.yaml`. Explain the DAG: `download` -> `prepare` -> `train`.
    *   Run `dvc repro`.
    *   **The "Magic" Moment**: Change `n_estimators` in `params.yaml` and run `dvc repro` again. Show how DVC skips the `download` and `prepare` stages because only the model parameters changed.
3.  **MLflow UI**:
    *   Run `mlflow ui` and show the parameters/metrics logged for the different runs.
4.  **Autograding**:
    *   Show a "GRADED CELL" in Notebook 1.
    *   Run the evaluation cell to show how students get immediate `[SUCCESS]` feedback.

### 3. Using the Solved Versions
*   If you get stuck during the live coding, the `_Solved.ipynb` files contain the full implementation.
*   You can use them to show the "Final Result" immediately if time is short.

---

## 📂 Project Structure
- `01_DVC_MLflow_Pipeline.ipynb`: Main lab on reproducibility and tracking.
- `02_GitHub_Actions_CI.ipynb`: Lab on CI/CD automation.
- `src/`: Production-ready scripts (`download_data.py`, `prepare.py`, `train.py`).
- `unittests.py`: The Autograder (logic for instant feedback).
- `setup_lab.sh`: Automated environment initializer.

## 🚀 Getting Started

1. **Run the setup script:**
   ```bash
   bash setup_lab.sh
   ```

2. **Activate the environment:**
   ```bash
   source .venv/bin/activate
   ```

3. **Open the notebooks:**
   Open the `.ipynb` files in Jupyter or VS Code to begin.

## ✅ Automatic Grading
The notebooks contain **GRADED CELL** sections. To verify implementation, run the evaluation cells provided in the notebooks. They use `unittests.py` to check the code against the expected behavior.
