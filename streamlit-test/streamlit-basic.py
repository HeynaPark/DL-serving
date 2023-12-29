import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Title")
st.header("Header")
st.subheader("subheader")

st.write("write something")


if st.button("Button1 click here!"):
    st.write("Button1 is clicked.")

if st.button("Button2 click here!"):
    st.write("Button2 is clicked.")

checkbox_btn = st.checkbox("check box")
checkbox_btn2 = st.checkbox("check box2", value=True)


if checkbox_btn:
    st.write("check box clicked!")

if checkbox_btn2:
    st.write("check box 2 clicked!")

# with st.spinner("Please wait.."):
#     time.sleep(3)

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40],
    })

st.markdown("=============================")

st.write(df)
st.dataframe(df) #컬럼 클릭 가능, 정렬 가능
st.table(df) # static한 Dataframe

st.dataframe(df.style.highlight_max(axis=0))
st.dataframe(df.style.highlight_min(axis=0))
st.table(df.style.highlight_max(axis=0))

st.metric("My metric", 42, 2)

st.json(df.to_json())

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)

st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000,2) /  [50, 50] +[37.5665, 126.9780], #서울
    columns=['lat', 'lon'] # 위도, 경도
)
st.map(map_data)


st.markdown("=============================")

selected_item = st.radio("Radio Part", ("A", "B", "C"))

if selected_item == "A":
    st.write("A")
if selected_item == "B":
    st.write("B")
if selected_item == "C":
    st.write("C")

option = st.selectbox("please select in selectbox",
                      ('kyle', 'seongyun', 'hyena'))

st.write('You selected:', option)

multi_select = st.multiselect('Please select somethings in multi selectbox!',
                              ['A','B','C','D'])

st.write('You selected:', multi_select)


values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)



st.markdown("=============================")
# text_input = st.text_input("input text here")
# st.write(text_input)

password_input= st.sidebar.text_input("Enter your password", type="password")

number_input = st.sidebar.number_input("숫자를 입력하세요")
st.write(number_input)

st.sidebar.date_input("날짜를 입력하세요")
st.sidebar.time_input("시간을 입력하세요")

st.caption("This is caption")
st.code("a=123")
st.latex("\int a x^2 \,dx")

st.sidebar.button("hi")
st.sidebar.text_input("input text here")


col1, col2, col3, col4 = st.columns(4)
col1.write("this is col1")
col2.write("this is col2")
col3.write("this is col3")
col4.write("this is col4")

with st.expander("클릭하면 열림"):
    st.write("열림!")



# st.balloons()

st.success("Success")
st.info("Info")
st.warning("Warning")
st.error("Error message")

with st.form(key="입력 form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    # submin_button = st.form_submin_button(label="Login")
    st.form_submit_button("login")

# if submin_button:
#     st.write(f"{text_input}로 로그인 되었습니다.")

uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])# 200MB제한



# session state
st.title("Counter Example with session state")

#count session_state 에 init
if 'count' not in st.session_state:
    st.session_state.count=0

increment = st.button('Increment1')
if increment:
    st.session_state.count += 1

decrement = st.button('Decrement2')
if decrement:
    st.session_state.count -= 1

st.write('Count = ', st.session_state.count)