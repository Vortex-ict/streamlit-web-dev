import streamlit as st
import pandas

data = {
    'Series_1': [1, 2, 4, 6, 9, 22, 50],
    'Series_2': [22, 5, 7, 77, 9, 45, 8]
}

df = pandas.DataFrame(data)

st.title('first test with streamlit, git and python')
st.subheader('This is a subheader')
st.write('''This is a first test with the framework streamlit.io and python. Just for deploying python web apps.
write code in editor, push and automated publish. Is realtime code updates also possible?''')

st.write(df)
st.line_chart(df)
