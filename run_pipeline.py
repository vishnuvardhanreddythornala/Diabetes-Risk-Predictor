from src.data_preprocessing import load_data, preprocess_data
from src.model_training import train_models
from src.model_evaluation import evaluate_model
from src.model_evaluation import evaluate_model  # Added for confusion matrix
import joblib
import os
import warnings
import pandas as pd
warnings.filterwarnings("ignore", category=FutureWarning)

# Step 1: Load and preprocess
df = load_data("data/diabetes.csv")
X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

# Step 2: Training ALL models
trained_models = train_models(X_train, y_train)

# Step 3: Evaluating ALL models and saving confusion matrices PER MODEL
results = {}
for name, model in trained_models.items():
    metrics = evaluate_model(model, X_test, y_test, model_name=name)   # This saves confusion matrix PNG!
    results[name] = metrics

results_df = pd.DataFrame(results).T  # For CSV saving/report

# Step 4: Get BEST model
best_name = results_df["Accuracy"].idxmax()
best_model = trained_models[best_name]
best_metrics = results[best_name]

print(f"\nBest Model: {best_name}")
print("Performance Metrics:", best_metrics)

# Step 5: Save best model and scaler
os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/best_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

# Saves evaluation results to CSV
results_df.to_csv("models/model_comparison_results.csv")