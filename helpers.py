import streamlit as st
import datetime

MY_GERMAN_GPA = 1.8
MY_RUSSIAN_GPA = 1.6  # My GPA from Inno but in german format

def get_current_age() -> int:
    """
    Calculates the current age of the user
    :return: age: int - current age in full years
    """
    dob_str = st.secrets["birth"]["dob"]
    dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()

    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    return age


def get_my_gpa(country="germany") -> dict:
    """
    Converts German GPA (1.0–5.0 scale) to:
    - Percentage
    - US GPA (4.0 scale)
    - Russian 100-point scale
    """
    if country == "germany":
        german_gpa = MY_GERMAN_GPA
    else:
        german_gpa = MY_RUSSIAN_GPA

    if not (1.0 <= german_gpa <= 5.0):
        raise ValueError("German GPA must be between 1.0 (best) and 5.0 (worst).")

    # Convertion works not correctly for grades 4.0-5.0 (<50%)! but we hope we will never have to convert such grades:)

    # 1.0 (best) => 100%, 4.0 (pass) => 50%, 5.0 (fail) => <50%
    # Linear conversion from German GPA to percentage
    percent = round(1 - ((german_gpa - 1.0) / 3 / 2), 2)  # 3=4-1 - from 50% to 100%; 2 cause 2*50%=100%

    # Convert to US GPA (approximate)
    us_gpa = round(percent * 4.0, 2)

    # Convert to Russian 100-point system (just percent)

    russian_score = round(percent * 4 + 1, 2)

    return {
        "german_gpa": german_gpa,
        "percentage": percent,
        "us_gpa": us_gpa,
        "russian_score": russian_score
    }
