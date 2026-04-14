import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset (comma separated now)
data = pd.read_csv("student-mat.csv")

# Clean column names
data.columns = data.columns.str.strip()

print("Columns:", data.columns)

# Drop unnecessary column
data = data.drop("student_id", axis=1)

# Convert categorical → numeric
data = pd.get_dummies(data)

# Features & Target
X = data.drop("overall_score", axis=1)
y = data["overall_score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save model + columns
pickle.dump((model, X.columns), open("model.pkl", "wb"))

print("✅ Model trained successfully!")