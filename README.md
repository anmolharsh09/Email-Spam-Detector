Email Spam Detector
A machine learning-powered Streamlit web application that detects whether an email message is spam or not using Natural Language Processing.

Features
-Trained using Scikit-learn (Multinomial Naive Bayes)
-Input any email content and check for spam
-Real-time predictions

Requirements
- Python 3.7+
- scikit-learn
- streamlit
- numpy
- pandas

Install dependencies with:
   pip install -r requirements.txt

How to Run
-Clone or download the repo.
-Make sure spam_model.pkl and vectorizer.pkl are in the same folder as app.py.
-Launch the app:
   streamlit run app.py

Model Info
-Algorithm: Multinomial Naive Bayes
-Vectorizer: TF-IDF
-Trained on: Spam-Ham dataset (can be customized)
