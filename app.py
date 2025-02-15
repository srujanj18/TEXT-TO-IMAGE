import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# Set Hugging Face API Key
API_KEY = "your_api_key_here"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

# Function to generate an image from text
def generate_image(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
        return None

# Streamlit UI
st.set_page_config(page_title="Text to Image Generator", layout="centered")
st.title("🖼️ Text to Image Generator")
st.markdown("Enter a description, and AI will generate an image!")

user_input = st.text_input("Enter your text description:", placeholder="E.g., A futuristic city at sunset")
generate_btn = st.button("Generate Image")

if generate_btn and user_input:
    with st.spinner("Generating... Please wait."):
        image = generate_image(user_input)
        if image:
            st.image(image, caption="Generated Image", use_column_width=True)
