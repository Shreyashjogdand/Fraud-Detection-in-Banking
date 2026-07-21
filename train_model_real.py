

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix


CSV_FILE = "paysim/paysim.csv"

print("Loading dataset...")
df = pd.read_csv(CSV_FILE)
print("Rows loaded:", len(df))


df = df[df["type"].isin(["TRANSFER", "CASH_OUT"])].copy()
print("Rows after filtering:", len(df))


df = df.rename(columns={
    "step": "count",
    "oldbalanceOrg": "oldbalanceOrig",   # PaySim spells it 'Org'
})


df = df[df["oldbalanceOrig"] > 0].copy()
drain_ratio = df["newbalanceOrig"] / df["oldbalanceOrig"]
df["isFraud"] = (drain_ratio <= 0.10).astype(int)
print("Engineered fraud rate: %.2f%%" % (100 * df["isFraud"].mean()))


features = ["count", "type", "amount",
            "oldbalanceOrig", "newbalanceOrig",
            "oldbalanceDest", "newbalanceDest"]
X = df[features]
y = df["isFraud"]

numeric_features = ["count", "amount", "oldbalanceOrig",
                    "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]
categorical_features = ["type"]

preprocessor = ColumnTransformer(transformers=[
    ("num", Pipeline([("scaler", MinMaxScaler())]), numeric_features),
    ("cat", Pipeline([("encoder", OneHotEncoder(handle_unknown="ignore"))]), categorical_features),
])

model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=100, random_state=42,
        class_weight="balanced", n_jobs=-1)),
])


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

print("Training model...")
model_pipeline.fit(X_train, y_train)

y_pred = model_pipeline.predict(X_test)
print("\nConfusion matrix [[TN FP][FN TP]]:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification report:")
print(classification_report(y_test, y_pred, digits=4))

joblib.dump(model_pipeline, "banking_app_rf.pkl")
print("\nbanking_app_rf.pkl created successfully!")