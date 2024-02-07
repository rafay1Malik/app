# app.py
import streamlit as st

def generate_text(prompt):
    # Use your Hugging Face model here to generate text based on the prompt
    generated_text = f"Generated text: {prompt}"
    return generated_text

st.title("Kids' Writing Assistant")

prompt = st.text_area("Enter Your Prompt:")

if st.button("Generate"):
    if prompt:
        result = generate_text(prompt)
        st.markdown(result)
    else:
        st.warning("Please enter a prompt.")
