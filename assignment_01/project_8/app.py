import streamlit as st
import pandas as pd

data = {"Name": ["John","Anna","Peter"],
    "Age": [23,34,45],
    "City": ["abcd","xyz","def"]}

df = pd.DataFrame(data)
#st.dataframe(df)
#st.table(df)

city = st.selectbox("Choose a city to filter", df["City"].unique())
filtered_data = df[df["City"] == city]
st.dataframe(filtered_data)

st.title("Streamlit Fundamentals")
st.header("This is a Header")
st.subheader("This is a Subheader")

st.write("This is my first streamlit app")

st.markdown("**This is bold text usig markdown**")

age = st.slider("Select your age",0,100,25)
name = st.text_input("Enter your name")

if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old.")

