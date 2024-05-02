import streamlit as st
import joblib


model=joblib.load("news-classification-model.pkl")

news_labels={'0':"Technical",'1':'Business','2':'sport','3':'entertainment','4':'politics'}

st.title("News Classification")
user_input=st.text_area("Enter your news here:")
if st.button("Predict"):
    predicted_label=model.predict([user_input])[0]
    print(predicted_label)
    pred_news_label=news_labels[str(predicted_label)]
    st.info(f"Predicted Sentiment: {pred_news_label}")