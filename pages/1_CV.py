import streamlit as st
from helpers import get_my_gpa

st.set_page_config(page_title="CV – Mikhail Avrutskii", page_icon="📄", layout="wide")

st.title("📄 Curriculum Vitae – Mikhail Avrutskii")

# --- PDF Download ---
with open("assets/Sample_CV.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📥 Download full CV (PDF)",
    data=PDFbyte,
    file_name="Mikhail_Avrutskii_CV.pdf",
    mime="application/pdf",
)

st.markdown("---")

# --- Education ---
st.subheader("🎓 Education")

col1, col2 = st.columns(2)

col1.markdown("""
#### **B.Sc. Artificial Intelligence**  
##### [Deggendorf Institute of Technology](https://th-deg.de/en) (Germany) | *Oct 2023 – Mar 2027*  

Most of the courses here are practice-oriented and project-based. 
I focused on applying theory to real-world problems in machine learning, computer vision, and software development.

##### Some of the most useful courses:
- Machine Learning
- Software Engineering
- Computer Vision
- Natural Language Processing
- Databases
- Project Management
- Operating Systems & Networks
- German
""")

my_grades = get_my_gpa()
col1.metric(
    label="🎓 German GPA",
    value=my_grades['german_gpa'],
    help=f"  \n(German GPA is inverted: 1.0 is best, while 5.0 is worst)"
         f"  \nPercentage: {int(my_grades['percentage'] * 100)}%"
         f"  \nUSA: {my_grades['us_gpa']} / 4.0"
         f"  \nRussia: {my_grades['russian_score']} / 5",
)

col2.markdown("""
#### **B.Sc. Computer Science** *(transferred)*  
##### [Innopolis University](https://innopolis.university/en/) (Russia) | *Sep 2022 – Aug 2023*  

This year gave me a very strong theoretical foundation in mathematics and computer science. 
I completed many core courses in math, logic, algorithms, programming, and systems design.

##### Some of the most useful courses:
- Calculus I & II, Linear Algebra I & II, Discrete Mathematics
- Computer Architecture
- Data Structures & Algorithms
- Software Systems Analysis & Design
- Software Project
- IOS Development with Swift
- Academic English
- Business Communications
""")

my_grades = get_my_gpa(country="russia")
col2.metric(
    label="🎓 German GPA",
    value=my_grades['german_gpa'],
    help=f"My average GPA from Innopolis University, but in german format."
         f"  \n(German GPA is inverted: 1.0 is best, while 5.0 is worst)"
         f"  \nPercentage: {int(my_grades['percentage'] * 100)}%"
         f"  \nUSA: {my_grades['us_gpa']} / 4.0"
         f"  \nRussia: {my_grades['russian_score']} / 5",
)

# --- Experience ---
st.subheader("💼 Experience")

st.markdown("""
##### **Teaching Assistant – Mathematics**  
Deggendorf Institute of Technology | *Apr 2025 – Present*  
- Support first-year AI students in discrete mathematics and calculus
- Conduct weekly exercise sessions
- Provide extra learning materials


##### **Private Tutor (Freelance)**  
Remote | *2023 – Present*  
- Taught 4 school students mathematics and computer science
- Focused on exam preparation and in-depth topic understanding
""")

# --- Skills ---
st.subheader("💻 Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
#### 🖥️ **Programming languages**:
- Python
- Java
- C/C++
- JavaScript
- Swift
- Kotlin
- Assembly    
""")

with col2:
    st.markdown("""
    #### 📚 **Frameworks & Libraries**:
- Scikit-learn
- TensorFlow
- OpenCV (cv2)
- Pandas
- Matplotlib
- Django
- FastAPI
- pytest
- Streamlit
- nltk (Natural Language Toolkit), wordcloud, Praat
    """)

with col3:
    st.markdown("""
#### ⚙️ **Tools & Platforms**:
- Git / GitHub / GitLab
- Docker
- Linux
- Raspberry Pi
- Jupyter / Colab
- VS Code
- JetBrains (PyCharm, CLion)
- ChatGPT / Gemini
- Arduino (C++ / microcontrollers)
    """)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    #### ☁️ **Databases & Deployment**:
- PostgreSQL
- SQLite
- Google Firestore
- Microsoft Azure
- AWS (Amazon Web Services)
- Streamlit Community Cloud
    """)

with col2:
    st.markdown("""
    #### 🦾 **AI & ML-Specific Techniques**:
- Classical ML pipelines (feature engineering, model selection, hyperparameter tuning)
- ML Evaluation
- Convolutional Neural Networks
- Reinforcement Learning
- Prompt-engineering
    """)

with col3:
    st.markdown("""
    #### 🔧 **Methodologies & Practices**:
- Object-Oriented Programming (OOP)
- Design Patterns
- Agile / Scrum
- CI/CD
- Microservice Architecture (REST APIs)
- Version Control workflows
    """)

# --- Soft Skills ---
st.subheader("🤝 Soft Skills")

st.markdown("""
- Fast learner and intellectually curious  
- Strong analytical thinking
- Natural curiosity and eagerness to explore
- Empathy and active listening
- Strong teaching and communication skills  
- Ability to explain complex concepts simply
- Responsible and well-organized  
- Collaborative mindset, enjoys working in teams
- Cross-cultural communication skills
""")

# --- Certifications ---
st.subheader("📜 Certifications & Trainings")

st.markdown("""
- **CERN Spring Campus** (Deggendorf, Germany), 2024  
- **Business Communications** (Innopolis, Russia), 2023
- **Finalist of National Technological Olympiad** (Moscow, Russia), 2022
- **Yandex Lyceum – Algorithms & Python** (Rostov-on-Don, Russia), 2019–2021
- **Arduino Club member** (Rostov-on-Don, Russia) 2016-2018
- Additional online courses in Data Science and Blockchain
""")

# --- Languages ---
st.subheader("🌍 Languages")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        label="🇬🇧 English",
        value="C1",
        help="C1 (Advanced): Can understand demanding texts, express ideas fluently and spontaneously, and use language flexibly for social, academic, and professional purposes.",
    )

with col2:
    st.metric(
        label="🇩🇪 German",
        value="B2.1",
        help="B2 (Upper-Intermediate): Can understand the main ideas of complex texts, interact with native speakers with a degree of fluency, and produce detailed text on a wide range of topics.",
    )

with col3:
    st.metric(
        label="🇷🇺 Russian",
        value="Native",
        help="Native proficiency: Full command of the language, including idiomatic expressions and cultural context.",
    )

# --- Hobbies ---
st.subheader("🎮 Interests and Knowledge")

st.markdown("""
- Economics
- Blockchain
- Popular Science
- Teaching
- Short-Distance Travel
- Series/Film Evenings
- Hearthstone
""")
