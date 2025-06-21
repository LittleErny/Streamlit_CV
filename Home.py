import streamlit as st
from PIL import Image
from helpers import get_current_age, get_my_gpa

st.set_page_config(page_title="Mikhail Avrutskii", page_icon="👨‍💻", layout="wide")


my_grades = get_my_gpa()
my_age = get_current_age()

col1, col2 = st.columns([1, 3])
with col1:
    # Photo
    image = Image.open("assets/profile.jpg")
    st.image(image, width=200)

    # Contacts
    st.markdown("### 📬 Contacts:")
    st.markdown("""
    - LinkedIn: [Mikhail Avrutskii](https://www.linkedin.com/in/mikhail-avrutskii-480041294/)
    - GitHub: [@LittleErny](https://github.com/LittleErny)
    - Email: mi.avrutskiy@gmail.com
    """)

with col2:
    # Main
    st.write("# Mikhail Avrutskii")
    st.write(f"👋 Hi, I'm **Mikhail**, a {my_age}-year-old AI student with a passion for machine learning, teaching, and building useful software.")

    st.markdown("""
I'm currently pursuing a **B.Sc. in Artificial Intelligence** at the Deggendorf Institute of Technology (Germany), 
where I combine strong theoretical knowledge with hands-on projects in **data analysis**, **computer vision**, and **software development**.

💡 Originally from **Rostov-on-Don, Russia**, now I live and study in **Deggendorf, Bavaria**, and work as a **Teaching Assistant in Mathematics** for first-year AI students.  
I also provide **private tutoring** for school students in math and programming.

I'm deeply interested in **machine learning**, **popular science**, and **educational tools** — and I love helping others understand complex topics.

---

🔍 **Currently looking for**:
- A **mandatory internship (Pflichtpraktikum)** starting in **September 2025**  
- In **Data Science**, **Machine Learning**, or **Software Engineering**  
- Ideally with a strong focus on **mentorship**, **best practices**, and **teamwork**

""")

    # Language Proficiency Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="🎓 German GPA",
            value=my_grades['german_gpa'],
            help=f"  \n(German GPA is inverted: 1.0 is best, while 5.0 is worst)"
                 f"  \nPercentage: {int(my_grades['percentage'] * 100)}%"
                 f"  \nUSA: {my_grades['us_gpa']} / 4.0"
                 f"  \nRussia: {my_grades['russian_score']} / 5",
        )

    with col2:
        st.metric(
            label="🇬🇧 English",
            value="C1",
            help="C1 (Advanced): Can understand demanding texts, express ideas fluently and spontaneously, and use language flexibly for social, academic, and professional purposes.",
        )

    with col3:
        st.metric(
            label="🇩🇪 German",
            value="B2.1",
            help="B2 (Upper-Intermediate): Can understand the main ideas of complex texts, interact with native speakers with a degree of fluency, and produce detailed text on a wide range of topics.",
        )

    with col4:
        st.metric(
            label="🇷🇺 Russian",
            value="Native",
            help="Native proficiency: Full command of the language, including idiomatic expressions and cultural context.",
        )
