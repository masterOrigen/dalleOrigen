from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey

def generate_image(image_description):
    client = OpenAI(api_key=apikey)
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"{image_description}",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    img_url = response.data[0].url
    return img_url

st.set_page_config(page_title="DALL-E 3 Image Generation")

st.title('DALL-E 3 Image Generation')
st.subheader("Powered by OpenAI and Streamlit")
img_description = st.text_input('Image Description')

if st.button('Generate Image'):
    if img_description:
        try:
            generated_img = generate_image(img_description)
            st.image(generated_img)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter an image description.")
