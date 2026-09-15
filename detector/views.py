from pathlib import Path
import joblib
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "detector" / "model.pkl"
TFIDF_PATH = BASE_DIR / "detector" / "tfidf.pkl"

# The model files are created by train_model.py.
model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None
tfid = joblib.load(TFIDF_PATH) if TFIDF_PATH.exists() else None

def home(request):
    prediction = None
    error = None
    subject = ""
    body = ""

    if request.method == "POST":
        subject = request.POST.get("subject", "").strip()
        body = request.POST.get("body", "").strip()

        if not subject or not body:
            error = "Please enter both email subject and body."
        elif model is None or tfid is None:
            error = "Model files are missing. Run train_model.py first."
        else:
            user_data = [subject + " " + body]
            user_data_tfidf = tfid.transform(user_data)
            prediction = int(model.predict(user_data_tfidf)[0])

    return render(request, "index.html", {
        "prediction": prediction,
        "error": error,
        "subject": subject,
        "body": body,
    })
