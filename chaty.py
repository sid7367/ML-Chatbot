import streamlit as st
import pandas as pd

# Load the Excel data
data = pd.read_excel('student_marks.xlsx')  # Replace with your actual file name

# Function to get marks of a student in a subject
def get_marks(student_name, subject):
    result = data[(data['Name'].str.lower() == student_name.lower()) &
                  (data['Subject'].str.lower() == subject.lower())]
    if not result.empty:
        return f"{student_name} scored {result.iloc[0]['Marks']} in {subject}."
    else:
        return "Student or subject not found."

# Function to predict pass/fail
def predict_pass_fail(student_name):
    student_data = data[data['Name'].str.lower() == student_name.lower()]
    if student_data.empty:
        return "Student not found."
    
    pass_count = (student_data['Marks'] >= 40).sum()
    total = len(student_data)
    
    if pass_count == total:
        return f"{student_name} is likely to PASS all subjects."
    elif pass_count >= total / 2:
        return f"{student_name} may PASS, but needs improvement."
    else:
        return f"{student_name} is likely to FAIL based on current marks."

# Streamlit UI
st.title("🎓 Student Marks Chatbot")

user_input = st.text_input("Ask a question like:")
st.markdown("- *What are John's marks in Math?*")
st.markdown("- *Will Mary pass?*")

if user_input:
    if "marks" in user_input.lower():
        name = st.text_input("Enter student name")
        subject = st.text_input("Enter subject")
        if name and subject:
            st.write(get_marks(name, subject))
    
    elif "pass" in user_input.lower() or "fail" in user_input.lower():
        name = st.text_input("Enter student name")
        if name:
            st.write(predict_pass_fail(name))
    
    else:
        st.write("Please ask about marks or pass/fail prediction.")
