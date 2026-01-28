#Basics.py
import streamlit as st
from datetime import datetime
# run " py -3.11 -m venv myenv "
# PS C:\Users\akvam\Desktop\Deployment_28Jan26> py -3.11 -m venv myenv
st.title("Welcome to Streamlit Deployment!")


# today lets learn "Widgets"
language = st.selectbox("Select your favorite programming language:",
                        ["C", "C++", "Java", "Python", "Ruby"])
st.write(f"my favorite programming language is {language}")

st.header("multi select boxes")
languages = st.multiselect(f"my favorite programming languages are:",["C", "C++", "Java", "Python", "Ruby"])
st.write("my favorite programming languages are:", languages)

st.header("select slider")
review = st.select_slider("Movie Rating",["Worst","Bad","Average","Good","Best" ])
st.write("You selected this rating:", review)

st.header("Slider")
height = st.slider("your height in cms",min_value=0,max_value=500)
st.write(f"your height is: {height} cms")

st.header("Text input")
name = st.text_input("what is your name?")
st.write(f"hello {name}, welcome to my webpage!")

st.header("Text area")
feedback = st.text_area("Please provide your feedback: ")
st.write(f"my feedback is : {feedback}")

st.header("Number input")
age = st.number_input("What is your age",min_value=0,max_value=200)
st.write(f"My age is: {age}")

st.header("Date input")
dob = st.date_input("what is your date of birth",min_value=datetime(1900, 1, 1),max_value=datetime(2026, 1, 1))
st.write("my date of birth is:", dob)

# NameError: name 'datetime' is not defined
# from datetime import datetime