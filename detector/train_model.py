import sys
from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

BASE_DIR = Path(__file__).resolve().parent.parent

# Usage:
# python detector/train_model.py "C:\path\to\SVM_Gmail_data (1).csv"
if len(sys.argv) < 2:
    print("Usage: python detector/train_model.py <csv_path>")
    sys.exit(1)

csv_path = Path(sys.argv[1])

df = pd.read_csv(csv_path)

required = {"Subject", "Body", "Label"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")

df["text"] = (
    df["Subject"].fillna("").astype(str)
    + " "
    + df["Body"].fillna("").astype(str)
)

X = df["text"]
Y = df["Label"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.20, random_state=42, stratify=Y
)

tfid = TfidfVectorizer()
X_train_tfidf = tfid.fit_transform(X_train)
X_test_tfidf = tfid.transform(X_test)

model = SVC(kernel="linear")
model.fit(X_train_tfidf, Y_train)

Y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(Y_test, Y_pred)

joblib.dump(model, BASE_DIR / "detector" / "model.pkl")
joblib.dump(tfid, BASE_DIR / "detector" / "tfidf.pkl")

print(f"Model trained successfully.")
print(f"Accuracy: {accuracy:.4f}")
print("Saved: detector/model.pkl")
print("Saved: detector/tfidf.pkl")
