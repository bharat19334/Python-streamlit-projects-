import streamlit as st
st.set_page_config(layout="wide")
st.markdown(
    "<h1 style='font-size:70px;'>Basic Calculator App</h1>",
    unsafe_allow_html=True
)
st.title("Basic calculator Calculator App")

a = st.number_input("Enter First Number")
b = st.number_input("Enter Second Number")

o = st.selectbox(
    "Choose Operation",
    ["+", "-", "*", "/"]
)

if st.button("Calculate"):

    match o:
        case "+":
            st.success(f"Addition : {a+b}")

        case "-":
            st.success(f"Subtraction : {a-b}")

        case "*":
            st.success(f"Multiplication : {a*b}")

        case "/":
            if b != 0:
                st.success(f"Division : {a/b}")
            else:
                st.error("Cannot divide by zero")