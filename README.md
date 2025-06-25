# 🛡️ Malware Detection using Ensemble Learning on Memory Dump Analysis

This project investigates and implements a malware detection framework using memory dump analysis combined with deep feature extraction and ensemble learning models. The objective is to improve classification accuracy and robustness in detecting malicious behaviors from memory artifacts.

## 🚀 Project Overview

Modern malware often evades traditional static detection methods. This project leverages memory forensics and machine learning to build a detection pipeline capable of identifying malicious processes using features extracted from memory dumps. It incorporates:

- Deep autoencoder-based feature extraction
- Stacked ensemble learning (multiple base classifiers + meta-classifier)
- Temporal data splitting for realistic evaluation
- Interpretability using SHAP values
- Key performance metrics: Accuracy, F1-score, ROC-AUC, FPR, FNR

## 📁 Project Structure

- data/ # Raw and preprocessed datasets
- notebooks/ # EDA, feature engineering, and modeling notebooks
- models/ # Saved model files and evaluation reports
- src/ # Core Python scripts for training, evaluation, etc.
- requirements.txt # Python dependencies
- README.md # Project documentation

## 🛠️ Development Environment

- **Language:** Python 3.11
- **IDE/Tools:** JupyterLab, VS Code
- **Libraries:**
  - `pandas`, `numpy` for data handling
  - `scikit-learn`, `xgboost`, `catboost` for ML models
  - `tensorflow` / `keras` for deep autoencoder
  - `shap` for model explainability
  - `matplotlib`, `seaborn` for visualizations
- **Environment:** Conda-based virtual environment

## 📊 Dataset and Features

- **Dataset Used**: Public memory dump dataset – **MemMal-D2024**
- **Feature Source**: Extracted using the **Volatility framework**, capturing behavioral memory features such as working set size, thread count, and I/O activity.
- **Preprocessing Steps**:
  - **Missing Value Handling**: NaN imputation and filtering of corrupted entries
  - **Normalization**: Applied to continuous features to reduce variance scale issues
  - **Dimensionality Reduction**: Performed using **deep autoencoder** to extract latent features
- **Sequence Modeling**:
  - The project incorporates temporal behavior modeling using a Hidden Markov Model (HMM).

## 🧠 Model Architecture

1. **Autoencoder**: Compresses high-dimensional memory features into latent representations.
2. **Base Classifiers**: Includes Random Forest, Logistic Regression, SVC, XGBoost
3. **Meta-Classifier**: CatBoost or Logistic Regression used in stacking to combine predictions from base models.

## 📈 Evaluation Metrics

To ensure the system's effectiveness and safety in malware detection:

- **Accuracy**, **Precision**, **Recall**, **F1-score**
- **ROC-AUC**
- **False Positive Rate (FPR)** – to minimize false alerts
- **False Negative Rate (FNR)** – to reduce undetected malware risks
- **SHAP and Coefficients magnitude** – to interpret feature contributions to predictions

## 🔄 Workflow Summary

1. Data collection from memory dump datasets
2. Preprocessing and cleaning
3. Feature extraction via deep autoencoder
4. Training stacked ensemble models
5. Evaluation under temporal validation
6. Model interpretability via SHAP

## 🤝 Collaboration and Version Control

- Version control via Git
- Repository structured for modular experimentation
- Contributions tracked using branches and pull requests

## 📌 Citation

If this project or its ideas contributed to your research, please consider citing:

```bibtex
@article{MANIRIHO2024103864,
  title = {MeMalDet: A Memory analysis-based Malware Detection Framework using deep autoencoders and stacked ensemble under temporal evaluations},
  journal = {Computers & Security},
  pages = {103864},
  year = {2024},
  doi = {https://doi.org/10.1016/j.cose.2024.103864},
  author = {Pascal Maniriho and Abdun Naser Mahmood and Mohammad Jabed Morshed Chowdhury}
}
```
