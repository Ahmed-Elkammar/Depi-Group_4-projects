# Boston Housing Price Predictor

A machine learning web application to predict housing prices in Boston using a Decision Tree Regressor model, built with Streamlit.

## Project Structure
```text
boston_project/
├── housing.csv               # Dataset used for training
├── model.joblib              # Serialized trained Decision Tree model
├── metrics.json              # Model evaluation metrics and feature boundaries
├── train.py                  # Model training and hyperparameter tuning script
├── app.py                    # Streamlit web application
├── requirements.txt          # Python dependencies
└── notebook/
    ├── boston_housing.ipynb  # Exploratory Data Analysis & experiments
    └── visuals.py            # Visualization helpers
```

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Web Application
```bash
streamlit run app.py
```
Open your browser and navigate to the local URL provided in the terminal (usually `http://localhost:8501`).

### 3. Retrain the Model (Optional)
If you wish to modify parameters and retrain the model, run:
```bash
python train.py
```
