import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
df = pd.read_csv("Dataset Phising Website.csv")
df = df.drop(columns=["index"])  # drop index column if exists

X = df.drop(columns=["Result"])
y = df["Result"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Models
lr = LogisticRegression(max_iter=1000)
dt = DecisionTreeClassifier()

lr.fit(X_train, y_train)
dt.fit(X_train, y_train)

# Save models & scaler
joblib.dump(scaler, "scaler.pkl")
joblib.dump(lr, "logistic_model.pkl")
joblib.dump(dt, "decision_tree_model.pkl")

print("✅ Models trained and saved successfully")


