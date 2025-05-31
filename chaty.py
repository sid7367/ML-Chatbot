import streamlit as st
import pandas as pd

# Load and clean the Excel data
data = pd.read_excel('student_marks.xlsx')
print(data.columns.tolist())
print(data.head())
data.columns = data.columns.str.strip().str.lower()  # Standardize column names
print(data['name'])

# Function to get marks of a student in a subject
def get_marks(student_name, subject):
    cleaned_name = student_name.strip().lower()
    st.write("Cleaned name input:", cleaned_name)

    st.write("All column names:", list(data.columns))  # Check column names

    # Show what data['name'] looks like
    st.write("Name column values:", data['name'].str.lower())  # Assuming column is 'Name'

    # Show the Boolean mask
    name_mask = data['name'].str.lower() == cleaned_name
    st.write("Boolean mask for name match:", name_mask)

    # Apply the mask to filter the row
    student_row = data[name_mask]
    st.write("Filtered student row:", student_row)

    if student_row.empty:
        return "Student not found."

    subject_title = subject.strip()
    st.write(data.columns)
    if subject_title not in data.columns:
        return "Subject not found."

    mark = student_row.iloc[0][subject_title]
    return f"{student_name} scored {mark} in {subject_title}."

# Function to predict pass/fail
def predict_pass_fail(student_name):
    cleaned_name = student_name.strip().lower()
    st.write("Cleaned name input:", cleaned_name)

    st.write("All column names:", list(data.columns))  # Check column names

    # Show what data['name'] looks like
    st.write("Name column values:", data['name'].str.lower())  # Assuming column is 'Name'

    # Show the Boolean mask
    name_mask = data['name'].str.lower() == cleaned_name
    st.write("Boolean mask for name match:", name_mask)

    # Apply the mask to filter the row
    student_row = data[name_mask]
    st.write("Filtered student row:", student_row)

    if student_row.empty:
        return "Student not found."

    st.write(data.columns)

    # Get all subject marks (excluding 'name')
    marks = student_row.drop(columns=['name']).iloc[0]
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
