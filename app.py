!pip install streamlit

# Create a file named 'app.py' with your Streamlit code
code = """
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
"""

with open('app.py', 'w') as file:
    file.write(code)

# Run Streamlit app in the background
!streamlit run /content/app.py &

# Create a public URL for the Streamlit app using ngrok
!pip install pyngrok
from pyngrok import ngrok
public_url = ngrok.connect(port='8501')

public_url

