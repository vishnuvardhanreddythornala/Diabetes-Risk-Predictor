# 🩺 Diabetes Risk Predictor

A machine learning pipeline to predict whether a patient is at risk of diabetes using clinical data such as glucose levels, insulin, BMI, age, and other health indicators.

---
## 📑 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Limitations and Future Work](#limitations-and-future-work)
- [License](#license)
- [Contact](#contact)

## 📖 About the Project  
Diabetes is a global health issue affecting millions. Early risk detection can lead to timely medical intervention.  
This project uses machine learning techniques to predict whether an individual is at risk of diabetes, based on attributes like glucose levels, insulin, BMI, and age.  
It employs classification models and is integrated with a Streamlit-based user interface for real-time prediction and interpretation.

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

## 🛠️ Tech Stack  
- Python  
- Pandas  
- Scikit-Learn  
- XGBoost  
- SHAP  
- Streamlit  

---

## ⚙️ Installation  
```bash
# Clone the repository  
git clone https://github.com/vishnuvardhanreddythornala/Diabetes-Risk-Predictor.git

# Navigate to the project directory  
cd Diabetes-Risk-Predictor

# Create and activate virtual environment (optional)  
python -m venv venv  
source venv/bin/activate        # On Windows use: venv\Scripts\activate

# Install dependencies  
pip install -r requirements.txt 
```

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

## 📁 Project Structure

```
diabetes-risk-prediction/
│
├── app/
│   └── streamlit_app.py         # Streamlit app for interactive prediction
├── models/                      # Trained model artifacts (optional)
├── data/                        # Input datasets (not included)
├── run_pipeline.py              # Entry point for model training and evaluation
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

⚡ Limitations and Future Work
Limitations:
Accuracy limited by the dataset size and quality

Currently supports batch inference; lacks real-time API deployment

Does not integrate electronic health records

Future Work:
Deploy as a cloud web app or API endpoint

Improve UI/UX with visual guides for medical terms

Add historical tracking for user health progression

📜 License
This project is licensed under the MIT License.


## 🙌 Acknowledgements

- [Scikit-learn](https://scikit-learn.org/)
- [XGBoost](https://xgboost.ai/)
- [Streamlit](https://streamlit.io/)
- [SHAP](https://github.com/slundberg/shap)
- Based on the PIMA Diabetes dataset

---

*Built with ❤️ to make healthcare predictive and proactive.*

📞 Contact
Name: Thornala Vishnu Vardhan Reddy
GitHub: @vishnuvardhanreddythornala
Email: vishnuvardhanreddythornala@gmail.com

