import streamlit as st
import pandas as pd

# Load the Excel data
data = pd.read_excel('student_marks.xlsx')  # Replace with your actual file name

# Function to get marks of a student in a subject
def get_marks(student_name, subject):
    student_row = data[data[data['Name'].str.lower() == student_name.lower()]]
    if student_row.empty:
        return f"Student not found."
    
    subject_title = subject.strip().title()  # Standardize the subject name (e.g., math → Math)

    if subject_title not in data.columns:
        return "Subject not found."
    
    mark = student_row.iloc[0][subject_title]
    return f"{student_name} scored {mark} in {subject_title}."

# Function to predict pass/fail (pass = 40 or more in each subject)
def predict_pass_fail(student_name):
    student_row = data[data["Name"].str.lower() == student_name.lower()]

    if student_row.empty:
        return "Student not found."
    
    # Exclude the 'Name' column and check pass/fail
    marks = student_row.drop(columns=['Name']).iloc[0]
    pass_count = (marks >= 40).sum()
    total_subjects = len(marks)
    
    if pass_count == total_subjects:
        return f"{student_name} is likely to PASS all subjects."
    elif pass_count >= total_subjects / 2:
        return f"{student_name} may PASS, but needs improvement."
    else:
        return f"{student_name} is likely to FAIL based on current marks."

# Streamlit UI
st.title("🎓 Student Marks Chatbot")

user_input = st.text_input("Ask a question like:")
st.markdown("- *What are John's marks in Math?*")
st.markdown("- *Will Mary pass?*")

if user_input:
    #for handling marks queries
    if "marks" in user_input.lower():
        name = st.text_input("Enter student name")
        subject = st.text_input("Enter subject")
        if name and subject:
            st.write(get_marks(name, subject))
    
    #for handling pass/fail queries
    elif "pass" in user_input.lower() or "fail" in user_input.lower():
        name = st.text_input("Enter student name")
        if name:
            st.write(predict_pass_fail(name))
    
    else:
        st.write("Please ask about marks or pass/fail prediction.")
