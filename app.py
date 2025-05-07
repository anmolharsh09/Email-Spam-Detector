import streamlit as st
import pickle
import base64

# Load model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# App title and emoji
st.set_page_config(page_title="Email Spam Detector", page_icon="📧")
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: #4B8BBE;
    }
    .footer {
        position: fixed;
        bottom: 10px;
        text-align: center;
        width: 100%;
        color: grey;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="title">📧 Email Spam Detector</div>', unsafe_allow_html=True)
st.write("### Paste any email message below and check if it's spam or not:")

# Email input
email = st.text_area("📝 Your Email Content", height=200)

# Detect button
if st.button("🔍 Detect Spam"):
    if not email.strip():
        st.warning("⚠️ Please enter some email content first.")
    else:
        features = vectorizer.transform([email])
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.error("🚫 Spam Detected: This looks like a spam email!")
        else:
            st.success("✅ Legit Email: This does not look like spam.")

