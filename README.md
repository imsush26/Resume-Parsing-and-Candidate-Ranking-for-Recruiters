# Resume-Parsing-and-Ranking-Resume-for-Recruiters
🚀 Project Overview

This project is an AI-powered Resume Parsing and Candidate Ranking System developed to assist recruiters in automating the resume screening process. The system analyzes resumes, compares them with a given job description, and ranks candidates based on similarity scores.

The project uses Natural Language Processing (NLP) techniques such as TF-IDF Vectorization and Cosine Similarity to identify the most relevant candidates for a job role.

A Streamlit web application was also developed to provide an interactive user interface for recruiters.

🎯 Objectives
* Automate resume screening and candidate ranking
* Reduce manual effort in recruitment
* Match resumes with job descriptions efficiently
* Provide recruiters with ranked candidate recommendations
  
🛠️ Technologies Used

Programming Language
* Python

Libraries & Frameworks
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
  
NLP Techniques
* TF-IDF Vectorization
* Cosine Similarity
  
📂 Dataset Information
The project uses resume data containing:
* Candidate resume text
* Candidate categories/roles
* Skills and experience information

Dataset Source:
Divyaamith/Kaggle-Resume

⚙️ Project Workflow
1️⃣ Data Loading
* Resume dataset loaded using Hugging Face datasets library
* Converted into Pandas DataFrame
2️⃣ Data Preprocessing
* Removed null resume entries
* Cleaned and prepared resume text for NLP processing
3️⃣ TF-IDF Vectorization
* Converted textual resume data into numerical feature vectors
* Captured important keywords and terms
4️⃣ Similarity Calculation
* Compared resumes with the input job description
* Used cosine similarity to compute relevance scores
5️⃣ Candidate Ranking
* Ranked candidates based on similarity scores
* Displayed top matching resumes
6️⃣ Visualization
* Generated score visualization using Streamlit charts
  
🖥️ Streamlit Application Features
* ✅ Enter custom job descriptions
* ✅ Rank candidates automatically
* ✅ Display top matching resumes
* ✅ Interactive score visualization
* ✅ Simple and user-friendly interface

📊 Machine Learning / NLP Approach
* TF-IDF Vectorization: TF-IDF converts text into numerical vectors by measuring the importance of words within resumes and job descriptions.

*Cosine Similarity: Cosine similarity measures how closely a resume matches the job description based on vector similarity.

💻 Running the Project
Install Dependencies
* pip install pandas numpy scikit-learn streamlit datasets matplotlib

Run Streamlit App
* streamlit run app.py

📷 Project Screenshots

The project includes:
* Resume ranking interface
* Similarity score visualization
* Candidate ranking output
  <img width="825" height="357" alt="image" src="https://github.com/user-attachments/assets/f2d6aa7f-fcdc-4372-ac8d-0f603898436c" />
  <img width="1413" height="312" alt="image" src="https://github.com/user-attachments/assets/17330eb3-42a7-46a0-bf0f-22fcdb98bc47" />


🏆 Key Features
* End-to-end NLP-based recruitment system
* Automated candidate ranking
* Interactive recruiter dashboard
* Real-time job description matching
* Lightweight and easy to deploy
  
🚀 Future Enhancements
* Resume PDF/DOCX upload support
* Advanced resume parsing
* Skill extraction using NLP
* BERT/Sentence Transformer embeddings
* Recruiter feedback system
* Database integration
  
📌 Conclusion

This project demonstrates how Natural Language Processing can automate and improve recruitment workflows. By combining TF-IDF vectorization and cosine similarity, the system efficiently ranks resumes according to job requirements and provides recruiters with faster and smarter candidate selection.
