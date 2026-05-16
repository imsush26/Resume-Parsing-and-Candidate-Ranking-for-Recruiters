import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datasets import load_dataset

st.title("Resume Ranking System")

# Load dataset
dataset = load_dataset("Divyaamith/Kaggle-Resume")
df = dataset['train'].to_pandas()

# Remove null values
df = df.dropna(subset=['Resume_str'])

# Job description input
job_input = st.text_area("Enter Job Description")

if st.button("Rank Candidates"):

    if job_input.strip() != "":

        vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(df['Resume_str'])
        job_vector = vectorizer.transform([job_input])

        similarity = cosine_similarity(job_vector, tfidf_matrix)[0]
        df['score'] = similarity

        ranked = df.sort_values(by='score', ascending=False)

        # Store first, then display
        top10 = ranked[['Category', 'score']].head(10)
        st.write(top10)

        st.subheader("📊 Score Visualization")

        st.bar_chart(top10.set_index('Category')['score'])

    else:
        st.warning("Please enter a job description.")
