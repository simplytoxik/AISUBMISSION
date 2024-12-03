AI Diagnosis and Visualization Tools
Overview
This repository contains two Python-based projects:

AI Diagnosis Model (final_model.py): A machine learning model that predicts medical diagnoses based on patient data.
Data Visualization Tool (graphs.py): A suite of data visualizations to understand patient trends and statistics.
Both projects are designed to work with a dataset named riyal_data.csv.

Features
AI Diagnosis Model
Data Preprocessing:
Splits blood pressure data into systolic and diastolic components.
Encodes categorical variables (e.g., gender, diagnosis, address) using LabelEncoder.
Standardizes numerical features for better model performance.
Machine Learning:
Utilizes a RandomForestClassifier for prediction.
Supports new predictions with user-provided data.
User Interaction:
Gathers user details interactively via the command line.
Validates input for accuracy and completeness.
Performance Evaluation:
Provides accuracy score and a detailed classification report.
Data Visualization Tool
Generates various visualizations to explore patient demographics and health data:
Age Distribution: Histogram showing the distribution of patients' ages.
Diagnosis Count by Gender: Bar chart with gender differentiation.
Blood Pressure Distribution: Boxplot for systolic and diastolic blood pressures.
Height vs. Weight: Scatterplot with points sized by age.
Diagnosis Count: Count plot of diagnoses.
Requirements
Ensure you have the following Python packages installed:

For final_model.py:
numpy
pandas
scikit-learn
For graphs.py:
matplotlib
seaborn
pandas
Install all dependencies using:

bash
Copy code
pip install -r requirements.txt
Setup
Clone this repository:
bash
Copy code
git clone <repository-url>
cd <repository-name>
Ensure you have Python 3.8+ installed.
Create and activate a virtual environment:
bash
Copy code
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux
Install dependencies:
bash
Copy code
pip install -r requirements.txt
File Descriptions
final_model.py
This script builds a machine learning model for predicting patient diagnoses. It:

Loads and preprocesses data from riyal_data.csv.
Trains a RandomForestClassifier on the dataset.
Interactively collects patient details and predicts their diagnosis.
Run the script:

bash
Copy code
python final_model.py
graphs.py
This script generates insightful visualizations from the dataset. It:

Loads patient data from riyal_data.csv.
Creates and displays various charts and plots.
Run the script:

bash
Copy code
python graphs.py
Dataset
riyal_data.csv
The dataset should have the following columns:

Age: Patient's age (numeric).
Gender: Gender of the patient (Male or Female).
Height: Height in centimeters (numeric).
Weight: Weight in kilograms (numeric).
Blood_Pressure: Blood pressure in the format systolic/diastolic (e.g., 120/80).
Diagnosis: Patient's diagnosis (categorical).
Address: Location or address (categorical).
Ensure the dataset is in the same directory as the scripts.

Example Usage
final_model.py
Load the dataset and train the model.
Enter patient details interactively:
plaintext
Copy code
Enter your name: John
Age (1-120): 45
Gender (Male/Female): Male
Height (in cm, e.g., 170): 175
Weight (in kg, e.g., 65): 70
Systolic Blood Pressure (e.g., 120): 125
Diastolic Blood Pressure (e.g., 80): 85
Receive a predicted diagnosis:
plaintext
Copy code
Predicted Diagnosis: Hypertension
graphs.py
Run the script to display visualizations:

Age distribution.
Diagnosis counts by gender.
Blood pressure distributions.
Scatterplots of height vs. weight.
Example output:

Troubleshooting
Common Errors
ModuleNotFoundError: Ensure all required libraries are installed:

bash
Copy code
pip install -r requirements.txt
FileNotFoundError: 'riyal_data.csv' not found: Place the dataset in the same directory as the scripts.

Broken scipy or matplotlib installation: Reinstall the package:

bash
Copy code
pip uninstall scipy matplotlib
pip install scipy matplotlib
Contribution
Feel free to open issues or submit pull requests for improvements or bug fixes.

License
This project is open-source and available under the MIT License.
