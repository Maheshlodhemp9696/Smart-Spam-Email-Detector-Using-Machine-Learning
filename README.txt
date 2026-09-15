# 📧 Smart Spam Email Detector Using Machine Learning

A machine learning-based web application that classifies emails as **Spam** or **Not Spam** using **TF-IDF Vectorization** and a **Linear Support Vector Machine (SVM)** classifier. The system provides a simple Django web interface where users can enter an email subject and body and get an instant prediction.

## 🚀 Features

* 📩 Email Subject and Body input
* 🤖 Machine Learning-based spam classification
* 🔤 TF-IDF text feature extraction
* ⚡ Linear SVM classification
* 🌐 Django-based web interface
* ✅ Spam / Not Spam prediction
* 📱 Responsive and user-friendly UI
* 📊 Model training using CSV dataset

## 🛠️ Technologies Used

* **Python**
* **Django**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **TF-IDF Vectorizer**
* **Support Vector Machine (SVM)**
* **HTML**
* **CSS**
* **Git & GitHub**

## 🧠 Machine Learning Workflow

```text
Email Subject + Email Body
          ↓
     Text Preprocessing
          ↓
     TF-IDF Vectorization
          ↓
       Linear SVM
          ↓
   Spam / Not Spam
```

## 📂 Project Structure

```text
Smart-Spam-Email-Detector-Using-Machine-Learning/
│
├── detector/
│   ├── templates/
│   │   └── index.html
│   │
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   ├── train_model.py
│   ├── model.pkl
│   └── tfidf.pkl
│
├── email_spam_detector/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## 📊 Dataset

The dataset contains the following important columns:

| Column    | Description          |
| --------- | -------------------- |
| `Subject` | Email subject        |
| `Body`    | Email body/content   |
| `Label`   | Email classification |

### Label

```text
0 → Not Spam
1 → Spam
```

The `Subject` and `Body` are combined into a single text field before applying TF-IDF vectorization.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Maheshlodhemp9696/Smart-Spam-Email-Detector-Using-Machine-Learning.git
```

### 2. Open the project folder

```bash
cd Smart-Spam-Email-Detector-Using-Machine-Learning
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🤖 Train the Machine Learning Model

If you want to train the model using your own dataset:

```bash
python detector/train_model.py "path/to/your/dataset.csv"
```

The dataset should contain:

```text
Subject
Body
Label
```

After successful training, the following files will be generated:

```text
detector/model.pkl
detector/tfidf.pkl
```

## ▶️ Run the Django Application

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🖥️ How It Works

1. Enter the **Email Subject**.
2. Enter the **Email Body**.
3. Click **Check Email**.
4. The subject and body are combined.
5. TF-IDF converts the text into numerical features.
6. The trained Linear SVM model classifies the email.
7. The result is displayed as:

   * ⚠️ **Spam Email**
   * ✅ **Not Spam**

## 🔍 Example

### Spam Email

**Subject:**

```text
Congratulations! You won a lottery
```

**Body:**

```text
You have been selected as the lucky winner.
Click the link to claim your prize now.
```

**Prediction:**

```text
⚠️ Spam Email
```

### Normal Email

**Subject:**

```text
Project Meeting Tomorrow
```

**Body:**

```text
Hi, our project meeting is scheduled for tomorrow at 10 AM.
Please join on time.
```

**Prediction:**

```text
✅ Not Spam
```

## 🔐 Important Note

The application uses the **same fitted TF-IDF vectorizer** for new emails that was used during model training.

For new email prediction:

```python
user_data_tfidf = tfid.transform(user_data)
prediction = model.predict(user_data_tfidf)
```

`fit_transform()` should only be used while training the TF-IDF vectorizer.

## 📌 Future Enhancements

* 📧 Gmail integration
* 🗄️ Store prediction history in MySQL
* 👤 User authentication
* 📈 Admin dashboard
* 📊 Spam detection analytics
* 🔔 Email notifications
* ☁️ Cloud deployment
* 🔄 Automatic model retraining

## 👨‍💻 Author

**Mahesh Lodhe**

GitHub:
https://github.com/Maheshlodhemp9696

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📜 License

This project is created for educational and development purposes.
