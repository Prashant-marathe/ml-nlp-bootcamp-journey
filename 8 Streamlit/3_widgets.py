import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name = st.text_input('Enter your name: ')
age = st.slider('Select Your age: ', 0, 100, 25)
options = ['Python', 'Java', 'C++', 'Javascript']
choice = st.selectbox('Choose your favourite language: ', options)

if name:
    st.write(f'Hello, {name}')

st.write(f'You selected {choice}.')

st.write(f'Your age is {age}')

data ={
    "Name":['John', 'Jane', 'Jake', 'Jill'],
    "Age":[28, 24, 35, 40],
    'City':['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

upload_file = st.file_uploader('Choose a CSV file', type='csv')
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)