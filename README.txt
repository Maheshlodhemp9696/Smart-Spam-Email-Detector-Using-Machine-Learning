
📧 Smart Spam Email Detector Using Machine Learning
A machine learning-based web application that classifies emails as Spam or Not Spam using TF-IDF Vectorization and a Linear Support Vector Machine (SVM) classifier. The system provides a simple Django web interface where users can enter an email subject and body and get an instant prediction.
🚀 Features
📩 Email Subject and Body input
🤖 Machine Learning-based spam classification
🔤 TF-IDF text feature extraction
⚡ Linear SVM classification
🌐 Django-based web interface
✅ Spam / Not Spam prediction
📱 Responsive and user-friendly UI
📊 Model training using CSV dataset
🛠️ Technologies Used
Python
Django
Scikit-learn
Pandas
NumPy
TF-IDF Vectorizer
Support Vector Machine (SVM)
HTML
CSS
Git & GitHub
🧠 Machine Learning Workflow

Email Subject + Email Body
          ↓
     Text Preprocessing
          ↓
     TF-IDF Vectorization
          ↓
       Linear SVM
          ↓
   Spam / Not Spam

📸 Screenshots
🏠 Home Page
<img src="screenshots/home_page.png" width="800">
⚠️ Spam Detection
<img src="screenshots/spam.png" width="800">
✅ Not Spam Detection
<img src="screenshots/not_spam.png" width="800">

📂 Project Structure
=======
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


Email Subject + Email Body
          ↓
     Text Preprocessing
          ↓
     TF-IDF Vectorization
          ↓
       Linear SVM
          ↓
   Spam / Not Spam


## 📂 Project Structure

>>>>>>> 1111adab8e8746aae82460b584b5de1388a40891

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
<<<<<<< HEAD
├── screenshots/
│   ├── home.png
│   ├── spam-result.png
│   └── normal-result.png
│
=======
>>>>>>> 1111adab8e8746aae82460b584b5de1388a40891
├── manage.py
├── requirements.txt
└── README.md

<<<<<<< HEAD
📊 Dataset
The dataset contains the following important columns:
Column	Description
`Subject`	Email subject
`Body`	Email body/content
`Label`	Email classification
Label
=======

## 📊 Dataset

The dataset contains the following important columns:

| Column    | Description          |
| --------- | -------------------- |
| `Subject` | Email subject        |
| `Body`    | Email body/content   |
| `Label`   | Email classification |

### Label

0 → Not Spam
1 → Spam


The `Subject` and `Body` are combined into a single text field before applying TF-IDF vectorization.
⚙️ Installation
1. Clone the repository

git clone https://github.com/Maheshlodhemp9696/Smart-Spam-Email-Detector-Using-Machine-Learning.git
2. Open the project folder

cd Smart-Spam-Email-Detector-Using-Machine-Learning

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment
Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

5. Install dependencies

pip install -r requirements.txt

🤖 Train the Machine Learning Model
If you want to train the model using your own dataset:

python detector/train_model.py "path/to/your/dataset.csv"

The dataset should contain:
=======

The `Subject` and `Body` are combined into a single text field before applying TF-IDF vectorization.

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/Maheshlodhemp9696/Smart-Spam-Email-Detector-Using-Machine-Learning.git


### 2. Open the project folder

cd Smart-Spam-Email-Detector-Using-Machine-Learning


### 3. Create a virtual environment

python -m venv venv


### 4. Activate the virtual environment

**Windows:**


venv\Scripts\activate

**Linux / macOS:**


source venv/bin/activate


### 5. Install dependencies

pip install -r requirements.txt


## 🤖 Train the Machine Learning Model

If you want to train the model using your own dataset:

python detector/train_model.py "path/to/your/dataset.csv"


The dataset should contain:


Subject
Body
Label


After successful training, the following files will be generated:
=======

After successful training, the following files will be generated:

detector/model.pkl
detector/tfidf.pkl

▶️ Run the Django Application
Start the Django development server:

python manage.py runserver

Open your browser and visit:

http://127.0.0.1:8000/

🖥️ How It Works
Enter the Email Subject.
Enter the Email Body.
Click Check Email.
The subject and body are combined.
TF-IDF converts the text into numerical features.
The trained Linear SVM model classifies the email.
The result is displayed as:
⚠️ Spam Email
✅ Not Spam
🔍 Example
Spam Email
Subject:

Congratulations! You won a lottery

Body:
=======

## ▶️ Run the Django Application

Start the Django development server:


python manage.py runserver

Open your browser and visit:

http://127.0.0.1:8000/

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

Congratulations! You won a lottery

**Body:**

You have been selected as the lucky winner.
Click the link to claim your prize now.

Prediction:
⚠️ Spam Email
Normal Email
Subject:
Project Meeting Tomorrow

Body:
=======

**Prediction:**

⚠️ Spam Email


### Normal Email

**Subject:**
Project Meeting Tomorrow

**Body:**

Hi, our project meeting is scheduled for tomorrow at 10 AM.
Please join on time.

Prediction:

✅ Not Spam

🔐 Important Note
The application uses the same fitted TF-IDF vectorizer for new emails that was used during model training.
For new email prediction:
=======

**Prediction:**

✅ Not Spam

## 🔐 Important Note

The application uses the **same fitted TF-IDF vectorizer** for new emails that was used during model training.

For new email prediction:


user_data_tfidf = tfid.transform(user_data)
prediction = model.predict(user_data_tfidf)

`fit_transform()` should only be used while training the TF-IDF vectorizer.
📌 Future Enhancements
📧 Gmail integration
🗄️ Store prediction history in MySQL
👤 User authentication
📈 Admin dashboard
📊 Spam detection analytics
🔔 Email notifications
☁️ Cloud deployment
🔄 Automatic model retraining
👨‍💻 Author
Mahesh Lodhe
GitHub:
https://github.com/Maheshlodhemp9696
⭐ Support
If you find this project useful, consider giving the repository a ⭐ on GitHub.
---
📜 License
This project is created for educational and development purposes.
=======

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


### 📜 License

This project is created for educational and development purposes.
>>>>>>> 1111adab8e8746aae82460b584b5de1388a40891
