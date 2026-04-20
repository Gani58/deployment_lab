import streamlit as st

st.title("Hello World Deployment 🚀")


st.subheader("Mini Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = a + b
    elif operation == "Subtract":
        result = a - b
    elif operation == "Multiply":
        result = a * b
    elif operation == "Divide":
        if b == 0:
            st.error("Cannot divide by zero!")  # ← intentional bug trigger
        else:
            result = a / b
            st.success(f"Result: {result}")