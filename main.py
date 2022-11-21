# streamlit run main.py

import streamlit as st
import pandas
import time
import calendar

data = {
    'Series_1': [1, 2, 4, 6, 9, 22, 50],
    'Series_2': [22, 5, 7, 77, 9, 45, 8]
}

df = pandas.DataFrame(data)

st.title('second test with streamlit, git and python')
st.subheader('This is a subheader')
st.write('''This is a first test with the framework streamlit.io and python. Just for deploying python web apps.
write code in editor, push and automated publish. Is realtime code updates also possible?''')

st.write(df)
st.line_chart(df)
st.area_chart(df)
st.balloons()
st.error('This is an error')
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

sl_val = st.slider("Celsius")
st.write(sl_val, "in Farhernheit is:", sl_val * 9/5 + 32)

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

with st.echo():
    st.write('This code will be printed')
   
yy = 2022
mm = 11
   
# display the calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2022, 1, 1, 1)
st.text(str)

add_selectbox = st.sidebar.text(str)


st.line_chart({"data": [130, 5*sl_val, 2*sl_val, 6*sl_val, 2*sl_val, 210, sl_val]})

with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg")

col1, col2 = st.columns(2)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg")

with col2:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    st.text(str)