import streamlit as st

st.title("Simple Calculator")

# Display input as a string
if "input_str" not in st.session_state:
    st.session_state.input_str = ""

def append_char(char):
    st.session_state.input_str += char

def clear_input():
    st.session_state.input_str = ""

def calculate():
    try:
        # Evaluate the expression safely
        result = eval(st.session_state.input_str)
        st.session_state.input_str = str(result)
    except Exception:
        st.session_state.input_str = "Error"

# Layout for number buttons
cols = st.columns(4)
for i in range(1, 10):
    if cols[(i-1)%3].button(str(i)):
        append_char(str(i))
if cols[3].button("0"):
    append_char("0")
if cols[3].button("."):
    append_char(".")

# Layout for operation buttons
op_cols = st.columns(4)
if op_cols[0].button("+"):
    append_char("+")
if op_cols[1].button("-"):
    append_char("-")
if op_cols[2].button("*"):
    append_char("*")
if op_cols[3].button("/"):
    append_char("/")

# Clear and equals buttons
action_cols = st.columns(2)
if action_cols[0].button("Clear"):
    clear_input()
if action_cols[1].button("="):
    calculate()

st.text_input("Expression", value=st.session_state.input_str, disabled=True)