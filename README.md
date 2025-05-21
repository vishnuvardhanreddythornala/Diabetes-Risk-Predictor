# 🩺 Diabetes Risk Predictio
  A complete end-to-end Python ML pipeline to predict diabetes using the Pima Indians dataset, featuring preprocessing, model comparison, and error analysis. Includes a user-friendly Streamlit web app for 
  instant predictions.
---

## 🚀 Features

- Supervised classification using:
  - Logistic Regression
  - Random Forest
  - XGBoost
- Evaluation Metrics:
  - Accuracy, Precision, Recall, F1-Score
  - ROC Curve, Confusion Matrix
- Explainability with SHAP (SHapley Additive exPlanations)
- Modular and scalable codebase
- Interactive prediction via Streamlit dashboard

---

## 📁 Project Structure

\`\`\`
diabetes-risk-prediction/
│
├── app/
│   └── streamlit_app.py         # Streamlit app for interactive prediction
├── models/                      # Trained model artifacts (optional)
├── data/                        # Input datasets (not included)
├── run_pipeline.py              # Entry point for model training and evaluation
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
\`\`\`

---

## ⚙️ Installation

1. **Clone the repository**

\`\`\`bash
git clone https://github.com/yourusername/diabetes-risk-prediction.git
cd diabetes-risk-prediction
\`\`\`

2. **Create and activate a virtual environment**

\`\`\`bash
python -m venv venv
# Activate on Linux/Mac
source venv/bin/activate
# Activate on Windows
venv\Scripts\activate
\`\`\`

3. **Install dependencies**

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## 🧪 Usage

### ▶️ Run Model Pipeline

To train and evaluate models:

\`\`\`bash
python run_pipeline.py
\`\`\`

### 🌐 Launch Streamlit App

To start the interactive app in your browser:

\`\`\`bash
streamlit run app/streamlit_app.py
\`\`\`

---

## 📊 Model Evaluation

The pipeline uses multiple machine learning algorithms to classify diabetes risk and evaluates their performance using:

- Accuracy
- Precision, Recall, F1-Score
- Confusion Matrix
- ROC-AUC Curve

Evaluation outputs (plots, reports) are generated automatically.

---

## 🧠 Model Explainability with SHAP

SHAP (SHapley Additive exPlanations) is integrated to explain the impact of each feature on the prediction. This improves trust and interpretability in the model’s decisions.

---

## 📉 Example Input Features

The models use the following health indicators (assumed):

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

*Make sure your dataset includes these features or adapt the pipeline accordingly.*

---

## 🎨 Streamlit Interface

The \`streamlit_app.py\` file provides:

- User-friendly input for clinical features
- Instant diabetes risk prediction
- SHAP summary plots for feature importance

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (\`git checkout -b feature-name\`)
3. Commit your changes (\`git commit -am 'Add new feature'\`)
4. Push to the branch (\`git push origin feature-name\`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- [Scikit-learn](https://scikit-learn.org/)
- [XGBoost](https://xgboost.ai/)
- [Streamlit](https://streamlit.io/)
- [SHAP](https://github.com/slundberg/shap)
- Based on the PIMA Diabetes dataset

---

Built with ❤️ to make healthcare predictive and proactive.
