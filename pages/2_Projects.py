import streamlit as st

st.set_page_config(page_title="Projects – Mikhail Avrutskii", page_icon="🧠", layout="wide")

st.title("🧠 Projects & Applications")
st.markdown("""
Below is a curated list of my key projects, showcasing practical experience in AI, software engineering, and research.
""")

# --- Software Engineering: Titanic Prediction ---
with st.expander("🚢 Titanic Prediction (2025)", expanded=False):
    st.markdown("""
**Software Engineering Project – Titanic Survival Prediction Web App**  
**Institution**: Deggendorf Institute of Technology (DIT)  
**Course**: Software Engineering (Prof. Dr. Christoph Schober)  
**Semester**: Summer 2025  
**Team Size**: 7 students  
**Role**: Backend Lead, Integration Coordinator  

As part of a semester-long software engineering project, our team of seven developed a fully Dockerized, AI-powered web application that predicts whether a Titanic passenger would have survived, based on user-input features.

The project consisted of four main microservices:

* **Web Frontend** (React-based SPA): for user interaction, including login, registration, input of Titanic passenger data, real-time predictions, and access to user history.
* **Web Backend** (FastAPI): the central API layer I designed and implemented, handling all client requests, routing them to appropriate services, and enforcing API consistency and user authorization.
* **Model Backend** (FastAPI): manages ML model training, storage, and inference via REST APIs. Supports multiple algorithms (SVM, Random Forest, etc.) and dynamic model creation by admin users.
* **Database** (PostgreSQL): for persistent user data, model metadata, and prediction history.

Key functional features included:

* Account management: register/login/logout
* A “Survival Calculator” with continuous prediction updates based on user input (age, class, fare, etc.)
* Admin panel for model creation and deletion
* History of recent predictions for logged-in users
* Course promotion page showcasing the use of AI in web apps

Non-functional achievements:

* Full Docker support with Nginx reverse proxy
* CI/CD using GitLab Pipelines with unit, integration, and nightly end-to-end tests
* Modular code structure with shared Git repositories and git submodules
* Mobile-optimized frontend compatible with Chrome, Firefox, Safari

**My Responsibilities**:

* Led the design of the overall backend architecture and REST API structure
* Developed the core logic of the **web-backend** service acting as the central connector between frontend, model backend, and database
* Coordinated the work distribution and integration efforts between sub-teams
* Defined interfaces between services and ensured communication consistency
* Oversaw and supported sprint planning and SCRUM documentation

**Key Skills Gained**:

* Microservice orchestration and Docker Compose
* FastAPI development and REST API design
* Team leadership and SCRUM-based project management
* CI/CD pipeline configuration in GitLab
* End-to-end testing with Cypress

*Note: Due to course policy, the full codebase will only be made public after July 2025. A personal demonstration is possible during interviews.*
    """)

# --- Machine Learning: Garbage Classification ---
with st.expander("🗑️ Garbage Classification (2025)", expanded=False):
    st.markdown("""
**2025 Machine Learning – Garbage Classification**  
**Institution**: Deggendorf Institute of Technology (DIT)  
**Course**: Machine Learning (Prof. Dr. Markus Mayer)  
**Semester**: Summer 2025  
**Team Size**: 2 students  
**Role**: ML Pipeline Engineer, Model Hyperparameter Tuner  

As part of the university Machine Learning course, this project focused on building and evaluating a full ML pipeline for an image classification task using only classical machine learning methods (no deep learning or unsupervised learning). The aim was not only to develop a working model but to **justify** that it is the optimal solution within the allowed methods.

**Dataset**: [TrashNet Dataset](https://github.com/garythung/trashnet)
(\~2,500 labeled images of trash in 6 categories: cardboard, glass, metal, paper, plastic, and trash)

**Pipeline Steps**:

* **Data Acquisition**: Public image dataset for waste classification
* **Data Preprocessing**: Cleaning, resizing, and converting images to feature vectors
* **Feature Extraction**: Classical computer vision features (e.g. HOG, color histograms, edge detection)
* **Data Analysis**: Investigated class distribution, separability, and feature correlations
* **Train/Validation/Test Split**
* **Feature Engineering & Selection**: Generated new features and combinations to improve class separability
* **Model Selection**: Compared multiple algorithms (SVM, Random Forest, KNN, Logistic Regression)
* **Hyperparameter Tuning**: Optimization of hyperparameters for different pipelines (in progress)
* TBA

The project emphasized explainability and analytical rigor over raw accuracy, reinforcing the value of **understanding ML foundations** rather than relying on black-box models.

**Achievements**:

* Received **grade 1.0** for the full pipeline development up to model training
* Demonstrated that classical ML approaches can meaningfully solve real-world image classification with limited data and computation

**Key Skills Gained**:

* Image feature engineering without neural networks
* Pipeline design and validation using classical ML techniques
* Statistical hypothesis testing for model evaluation
* Hands-on experience with SVMs, decision trees, space lifting, and dimensionality reduction

*Note: Due to course policy, the project is confidential until final submission in July 2025. However, I am happy to present the project in a private setting or during an interview.*
    """)

# --- Assistance Systems: CarLab ---
with st.expander("🚗 CarLab – Used Car Price Predictor (2024)", expanded=False):
    st.markdown("""
**2024 Assistance Systems – CarLab**  
**Institution**: Deggendorf Institute of Technology (DIT)  
**Course**: AIN-B Assistance Systems (Prof. Dr. Udo Garmann)  
**Semester**: Winter 2023/24  
**Team Size**: 2 students  
**Role**: Data Analyst, UI/UX Developer  

This project, developed during the “Assistance Systems” course, focused on creating an intelligent web assistant that helps users select a used car based on their preferences. The system had to combine a predictive model with a user-friendly interface and chatbot support.

**Dataset**: Open-source dataset of used German cars (price, brand, age, engine type, etc.)

**Key Project Goals**:

* **Data Exploration**: Analyzed structure, distribution, and patterns in used car data
* **Data Preprocessing**: Cleaning, feature selection, encoding categorical variables, normalization
* **Modeling**: Built a regression model to predict car prices (mainly handled by teammate)
* **Interface**: Designed and implemented a responsive Streamlit app for user interaction
* **Chatbot**: Connected a basic natural-language assistant to help users navigate the app
* **Deployment**: Deployed the full project as a web app on Streamlit Cloud

**Responsibilities**:

* Conducted initial data analysis and dataset preprocessing
* Built a dynamic Streamlit-based user interface for data input and visualization
* Coordinated with teammate on chatbot integration and model pipeline

**Technical Highlights**:

* Streamlit frontend with dynamic visualizations
* Pandas and scikit-learn for data processing
* SOLID principles partially applied for better project structure (lessons learned)
* Git-based team collaboration via THD GitLab

**Lessons Learned**:

* The importance of designing architecture early with best practices (e.g., SOLID)
* Realized later during the Machine Learning course that some techniques (correlation use, normalization, model tuning) were naïvely implemented — a valuable learning moment
* Gained interest in the software engineering aspect of ML tools and UI development

**Grade**: 1.3
**Links**:  

* [Web Demo (Streamlit)](https://erny-carlab.streamlit.app/)
* [Source Code & Documentation](https://mygit.th-deg.de/ma06524/sas-thd) *(hosted on THD GitLab)*
    """)

# --- Internet Technologies: Restaurant Reservation App ---
with st.expander("🍽️ Table Reservation Web App (2024)", expanded=False):
    st.markdown("""
    **2024 Internet Technologies – Table Reservation Web App**  
    **Institution**: Deggendorf Institute of Technology (DIT)  
    **Course**: AIN-B Internet Technologies  
    **Semester**: Winter 2023/24  
    **Team Size**: 4 students  
    **Role**: Full-Stack Developer & Database Integrator  

    In this course project, my team designed and implemented a full-stack web application enabling customers to reserve restaurant tables, complete with a responsive chatbot assistant and real-time reservation handling.

    **Key Features**:

    * **Chatbot Interface**: A JavaScript-based front-end chatbot using simple keyword spotting, defaulting to ChatGPT API for complex queries.
    * **Real-Time Reservation Management**: Firestore backend ensures synchronized table availability updates across all users.
    * **User Flow**: Users can query table availability, make a reservation, and receive confirmation via the chatbot interface.

    **Technical Stack**:

    * **Frontend & Backend**: JavaScript (Node.js, Express) for API routes and UI rendering.
    * **Database**: Google Firestore for storing reservation data and maintaining consistency.
    * **Chatbot Integration**: Basic keyword detection with fallback to ChatGPT API for natural responses.
    * **Hosting**: Deployed on a Microsoft Azure server for continuous availability and testing.

    **Key Learnings and Outcomes**:

    * Gained hands-on experience connecting a dynamic front-end chatbot to a real-time database.
    * Improved understanding of asynchronous operations in JavaScript and Firestore listeners.
    * Learned valuable lessons in teamwork and version control—our major challenges stemmed from coordination inefficiencies.
    * Recognized the importance of clean code and structured practices, leading me to later adopt better software architecture principles.

    **Repository**: [GitHub – AI-Chatbot](https://github.com/LittleErny/AI-Chatbot)
        """)

# --- Computer Vision: JetRacer ---
with st.expander("🏁 JetRacer – Autonomous Racing Car (2024)", expanded=False):
    st.markdown("""
**2024 JetRacer – Computer Vision Self-Driving Car**  
**Institution**: Deggendorf Institute of Technology (DIT)  
**Course**: AIN-B Computer Vision  
**Semester**: Summer 2024  
**Team Size**: 4 students (however, only 2 of them actively participated)  
**Role**: Computer Vision Engineer & ML Pipeline Developer  

As a second-semester student, I proactively enrolled in a Computer Vision course typically taken in the fourth semester. For our team project, we built and programmed a self-driving miniature race car using NVIDIA JetRacer Pro.

**Project Highlights**:

* **Hardware Setup**: Assembled the JetRacer, flashed it with the correct Jetson Nano Linux image, and configured the software stack.
* **Data Collection**: Recorded driving data via the onboard camera and collected labeled datasets to train steering prediction models.
* **Model Training**: Trained a small Convolutional Neural Network (CNN) to predict steering angles based on real-time video input.
* **Iteration & Improvement**:

  * Initially trained a lightweight CNN on a small dataset, which led to slow and unreliable driving.
  * Used the initial model to automate driving and gather larger, more diverse datasets.
  * Retrained a deeper CNN for significantly improved performance.

**Results**:

* Achieved autonomous driving on a closed racing track with stable and reliable steering.
* Final model performed well under real-time constraints and showed strong generalization on varied track segments.
* Received the top grade of **1.0** for the project.

**Technologies Used**:

* Python, PyTorch, OpenCV
* NVIDIA Jetson Nano, JetRacer Pro platform
* Custom data collection and augmentation scripts

**Repository**: [GitHub – JetRacer Project](https://github.com/LittleErny/JetRacer)
""")

# --- iOS App: Random Cat Generator ---
with st.expander("🐱 Random Cat Generator iOS App (2023)", expanded=False):
    st.markdown("""
**2023 iOS App – Random Cat Generator**  
**Institution**: Innopolis University  
**Course**: IOS Development with Swift (Elective)  
**Year**: 2023  
**Team Size**: 2 students  
**Role**: iOS Developer & UI/UX Designer  

In this elective course, my teammate and I designed and built a Swift-based iOS app that fetches and displays random cat images, providing users with the ability to view adorable photos and save their favorites to a local gallery.

**Project Highlights**:

* **API Integration**: Connected to a public cat image API to retrieve random images.
* **Persistent Storage**: Implemented local image saving using Core Data so users can access saved images offline.
* **Responsive UI Design**: Learned to design adaptive interfaces by considering multiple device orientations and screen sizes—including support for camera “island” notch layouts—using iOS Safe Area constraints.
* **Industry-Led Instruction**: The course was taught by professionals from Tinkoff Bank, introducing us to real-world app architecture, networking, database integration, and code quality practices.

**Key Learnings and Outcomes**:

* Applied UIKit and Swift to build a functional and responsive mobile interface.
* Mastered best practices for persistent storage and API-driven features.
* Understood the importance of layout adaptation and safe area design for diverse device families.
* Improved discipline in modular code organization and collaboration under industry-style guidance.

**Repository**: [GitHub – RandomCatGeneratorSwift](https://github.com/LittleErny/RandomCatGeneratorSwift)
    """)

# --- Competition: National Technological Olympiad ---
with st.expander("🏆 Autonomous Transport Systems Olympiad (2022)", expanded=False):
    st.markdown("""
**2022 National Technological Olympiad – Autonomous Transport Systems**  
**Organization**: National Technological Olympiad, Russia  
**Role**: Copter System Developer (Team of 4)  
**Achievement**: Won first two stages, participated in the Final round  

This project was part of a national-level technological competition focused on advanced IT fields including programming, computer vision, machine learning, and robotics. Our team chose the “Autonomous Transport Systems” track, where we tackled multi-robot coordination in a simulated urban environment.

**Project Overview**:
The final challenge required delivering goods across a room-sized artificial city using three robots: a sorting center, an autonomous car, and a copter. The delivery workflow was: sorting the goods, transporting by car, and final delivery by copter.

**My Responsibilities**:

* Studied and operated the copter system, based on Raspberry Pi running Linux and Python.
* Developed a flight path algorithm to traverse all building roofs in the city searching for a special visual marker indicating the delivery target.
* Created and trained a computer vision model to accurately detect this marker on the roofs, enabling the copter to precisely position itself for delivery.
* Implemented the package drop mechanism onto the target marker.
* Programmed the return navigation for the copter to safely reach its docking station.

**Outcome**:

* Successfully developed and tested the copter subsystem, which completed its tasks reliably during the competition.
* The overall team did not win the final stage due to a failure in one of the other robots’ subsystems.
* Participation in this Olympiad was a highly formative experience, contributing to my receiving a fully-funded scholarship at Innopolis University.

**Certificate**: [Official Certificate (Russian)](https://diploma.kruzhok.org/s3/talent-diploma-service/a852c946-3a55-4726-be72-0efee9073052/496602.pdf)
    """)

# --- Early Projects: Yandex Lyceum ---
with st.expander("🎓 Yandex Lyceum Projects (2019–2021)", expanded=False):
    st.markdown("""
**2021 ScheduleHelper & SonataBot**  
**Organization:** Yandex Lyceum (now Yandex Academy)  
**Role:** Python Developer  

These two small projects were part of my early experience learning Python during my time at Yandex Lyceum (2019–2021). The first year focused on Python basics (loops, functions, OOP), and the second year emphasized project development.

**ScheduleHelper**
A desktop application designed to assist school administration in creating and managing lesson timetables.

* Connected the app to an SQLite database to store and retrieve scheduling data.
* Developed user interfaces from both the teacher’s and class’s perspectives.
* Implemented synchronization between interfaces so updating one (e.g., teacher’s schedule) automatically updates the other.
* This project marked my first hands-on experience with databases and SQL queries, an important milestone in my programming journey.

**SonataBot**
Inspired by the popular Rhythm bot on Discord, SonataBot is a Discord bot capable of playing music from Yandex Music.

* The bot joins a user’s Discord voice channel and streams tracks from Yandex Music playlists or direct links.
* Implements basic queue management and playback controls similar to Rhythm bot functionality but tailored for Yandex Music.
* Developed entirely in Python, it provided practical experience with API integration and asynchronous programming.

Although both projects have rough edges (messy code, Russian interface) due to my early stage of learning, they demonstrate my consistent growth and passion for programming.

**Links:**

* ScheduleHelper: [GitHub](https://github.com/LittleErny/ScheduleHelper)
* SonataBot: [GitHub](https://github.com/LittleErny/SonataBot)
    """)

# --- First Project: Arduino Robot Firefighter ---
with st.expander("🔥 Arduino Robot Firefighter (2018)", expanded=False):
    st.markdown("""
**2018 Arduino Robot Firefighter**
**Organization:** Robofinist (Competition) & StartRobot Arduino Club, Rostov-on-Don
**Role:** Programmer & Robotics Team Member

This was my very first major programming project, marking the beginning of my journey in IT and programming. I started learning C++ and Arduino, which led to participating in a regional robotics competition focused on firefighter robots.

The challenge was to simulate a real firefighter’s task: locate a fire inside a building and extinguish it. Our team developed an Arduino-based robot that:

* Navigates a labyrinth using an ultrasonic distance sensor to avoid obstacles.
* Detects fire using an infrared (IR) sensor.
* Extinguishes the fire by pouring water onto it.

Although our team did not win, this experience was incredibly valuable and solidified my passion for programming and robotics. It was the moment I realized the career path I wanted to pursue.

**Links:**

* Competition page (in Russian): [robofinist.ru](https://robofinist.ru/event/info/bids/id/185)
* Video showing the robot and me as a 13-year-old (in Russian): [YouTube](https://youtu.be/NRqVOK1ffYg) (by the way you can see my robot at 1:57 and me 13-year old at 
    """)
