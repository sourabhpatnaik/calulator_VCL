import streamlit as st

st.title("Calculator Application")

number1 = st.number_input("Enter First Number",placeholder="Example: 5")
number2 = st.number_input("Enter Second Number",placeholder="Ex: 10")


option = st.selectbox(
    "Select the Operation",
    ['Addition','Subtraction','Multiplication','Division'],
    index=None
)

res = st.button("Calculate")
if res:
    if option == 'Addition':
        result = number1 + number2
        st.write(f"Result for {option}: {result}")
    elif option == "Subtraction":
        result = number1 - number2
        st.write(f"Result for {option}: {result}")
    elif option == "Multiplication":
        result = number1 * number2
        st.write(f"Result for {option}: {result}")
    elif option == "Division":
        result = number1 / number2
        st.write(f"Result for {option}: {result}")