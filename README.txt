EMAIL SPAM DETECTOR - DJANGO + SVM + TF-IDF

1. Open terminal in this project folder.

2. Create virtual environment:
   python -m venv venv

3. Activate on Windows:
   venv\Scripts\activate

4. Install packages:
   pip install -r requirements.txt

5. Train the model using your CSV:
   python detector/train_model.py "C:\Users\HP\Downloads\SVM_Gmail_data (1).csv"

   CSV must contain:
   Subject
   Body
   Label

6. Start Django:
   python manage.py runserver

7. Open:
   http://127.0.0.1:8000/

Important:
- Label 1 is treated as Spam.
- Label 0 is treated as Not Spam, based on the supplied dataset.
- Do not use fit_transform() on a new email.
- New email must use tfid.transform().
