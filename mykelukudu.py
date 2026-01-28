
import streamlit as st
# run " py -3.11 -m venv myenv "
# PS C:\Users\akvam\Desktop\Deployment_28Jan26> py -3.11 -m venv myenv
st.title("Welcome to Streamlit Deployment!")


# today lets learn "Widgets"
language = st.selectbox("Select your favorite programming language:",
                        ("Python", "JavaScript", "Java", "C++", "Ruby"))
st.write("You selected:", language)

st.header("Sliders")
age = st.slider("What is your age?", 0, 130, 25)

st.header("Date input")
dob = st.date_input("what is your date of birth",min_value=datetime.date(1900, 1, 1),max_value=datetime.date.today())
st.write("my date of birth is:", dob)