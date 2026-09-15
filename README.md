## 📸 Screenshots

### 🏠 Home Page

![Home Page](./screenshots/home_page.png)

### ⚠️ Spam Detection

![Spam Detection](./screenshots/spam.png)

### ✅ Not Spam Detection

![Not Spam Detection](./screenshots/not_spam.png)


📧 Smart Spam Email Detector Using Machine Learning

A machine learning-based Django web application that automatically classifies emails as Spam or Not Spam using TF-IDF Vectorization and a Linear Support Vector Machine (SVM) classifier.

📖 Project Description

Smart Spam Email Detector Using Machine Learning is a Django-based web application developed to identify whether an email is Spam or Not Spam.

The application accepts an Email Subject and Email Body from the user. These two inputs are combined into a single text and processed using TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization. The extracted numerical features are then passed to a Linear Support Vector Machine (SVM) machine learning model for classification.

The trained model predicts whether the email is spam or a legitimate email and displays the result instantly through a simple and responsive Django web interface.

This project demonstrates the practical integration of:

🤖 Machine Learning

📝 Natural Language Processing (NLP)

🔤 TF-IDF Text Vectorization

⚡ Linear Support Vector Machine (SVM)

🌐 Django Web Development

🐍 Python

📊 CSV-based Dataset

The project is designed as a practical machine learning application that can be extended with features such as Gmail integration, user authentication, prediction history, analytics, and cloud deployment.

🎯 Project Objective

The main objective of this project is to build an automated email classification system that can:

Accept an email subject and body as input.

Process the email text.

Convert text into numerical features using TF-IDF.

Use a trained Linear SVM model for classification.

Predict whether the email is Spam or Not Spam.

Display the prediction through a Django web interface.

🚀 Features

📩 Email Subject and Body input

🤖 Machine Learning-based spam classification

🔤 TF-IDF text feature extraction

⚡ Linear SVM classification

🌐 Django-based web interface

✅ Spam / Not Spam prediction

📱 Responsive and user-friendly UI

📊 Model training using CSV dataset

🔄 Reusable trained model and TF-IDF vectorizer

⚡ Instant prediction for new emails

🛠️ Technologies Used

Technology

Purpose

Python

Main programming language

Django

Web application framework

Scikit-learn

Machine learning implementation

Pandas

Dataset handling and preprocessing

NumPy

Numerical operations

TF-IDF Vectorizer

Text feature extraction

Linear SVM

Email classification

HTML

Web page structure

CSS

Web page styling

Git & GitHub

Version control and project hosting

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

🔹 Step-by-Step Workflow

1. Email Input

The user enters the email subject and email body through the Django web interface.

2. Text Combination

The subject and body are combined into a single text field.

3. TF-IDF Vectorization

The combined text is converted into numerical features using the same fitted TF-IDF vectorizer used during model training.

4. Linear SVM Classification

The TF-IDF features are passed to the trained Linear SVM model.

5. Prediction

The model predicts:

0 → Not Spam
1 → Spam

6. Result Display

The prediction is displayed to the user through the Django interface.

📊 Dataset

The application uses a CSV dataset containing email information and classification labels.

Dataset Columns

Column

Description

Subject

Email subject

Body

Email body/content

Label

Email classification

Label Meaning

0 → Not Spam
1 → Spam

The Subject and Body columns are combined into a single text field before applying TF-IDF vectorization.

Example:

Subject: Congratulations! You won a lottery

Body: You have been selected as the lucky winner.

The combined text is then processed by the TF-IDF vectorizer.

⚙️ Installation

1. Clone the Repository

git clone https://github.com/Maheshlodhemp9696/Smart-Spam-Email-Detector-Using-Machine-Learning.git

2. Open the Project Folder

cd Smart-Spam-Email-Detector-Using-Machine-Learning

3. Create a Virtual Environment

python -m venv venv

4. Activate the Virtual Environment

Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

5. Install Dependencies

pip install -r requirements.txt

🤖 Train the Machine Learning Model

If you want to train the model using your own dataset, run:

python detector/train_model.py "path/to/your/dataset.csv"

The dataset should contain these columns:

Subject
Body
Label

After successful training, the following files will be generated:

detector/model.pkl
detector/tfidf.pkl

Model Files

model.pkl

Contains the trained Linear SVM classification model.

tfidf.pkl

Contains the fitted TF-IDF vectorizer used to convert email text into numerical features.

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

The trained TF-IDF vectorizer converts the text into numerical features.

The Linear SVM model analyzes the features.

The model returns the prediction.

The result is displayed on the web page.

Possible results:

⚠️ Spam Email

or

✅ Not Spam

🔍 Example

⚠️ Spam Email

Subject:

Congratulations! You won a lottery

Body:

You have been selected as the lucky winner.
Click the link to claim your prize now.

Prediction:

⚠️ Spam Email

✅ Normal Email

Subject:

Project Meeting Tomorrow

Body:

Hi, our project meeting is scheduled for tomorrow at 10 AM.
Please join on time.

Prediction:

✅ Not Spam

🔐 Important Machine Learning Note

The application uses the same fitted TF-IDF vectorizer for new email predictions that was used during model training.

For a new email, the text should be transformed using:

user_data_tfidf = tfid.transform(user_data)
prediction = model.predict(user_data_tfidf)

fit_transform() should only be used when fitting the TF-IDF vectorizer during training.

For new/unseen emails, use:

transform()

instead of:

fit_transform()

This ensures that the new email is converted using the same feature space expected by the trained model.

📌 Future Enhancements

The project can be further improved with the following features:

📧 Gmail integration

🗄️ Store prediction history in MySQL

👤 User authentication

📈 Admin dashboard

📊 Spam detection analytics

🔔 Email notifications

☁️ Cloud deployment

🔄 Automatic model retraining

📱 Improved mobile interface

📈 Model performance dashboard

💡 Applications

This type of spam detection system can be used as a foundation for:

Email filtering systems

Automated message classification

Customer communication platforms

Cybersecurity applications

NLP-based text classification systems

Email management applications

🎓 Learning Outcomes

Through this project, the following concepts are demonstrated:

Python programming

Data preprocessing

CSV dataset handling

Natural Language Processing

TF-IDF Vectorization

Supervised Machine Learning

Linear SVM classification

Model training and prediction

Django application development

Machine Learning model integration with Django

Git and GitHub project management

👨‍💻 Author

Mahesh Lodhe

GitHub:
https://github.com/Maheshlodhemp9696

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

📜 License

This project is created for educational and development purposes.
