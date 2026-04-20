# train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Create some dummy data (Age, Monthly Spend -> Churn: 0 or 1)
data = {
    'Age': [25, 45, 35, 50, 23, 60],
    'Monthly_Spend': [50.0, 120.0, 60.0, 150.0, 30.0, 200.0],
    'Churn': [0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df[['Age', 'Monthly_Spend']]
y = df['Churn']

# 2. Train the model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# 3. Save the model as an artifact
joblib.dump(model, 'model.pkl')
print("Model trained and saved as model.pkl")