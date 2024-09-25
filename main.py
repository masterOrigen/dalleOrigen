import os
from openai import OpenAI
import streamlit as st

# Configuración de la página Streamlit
st.set_page_config(page_title="Brainstorm generador de Imagenes")

# Función para generar la imagen
def generate_image(image_description):
    # Obtener la clave API de la variable de entorno
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("No se encontró la clave API de OpenAI. Asegúrate de configurar la variable de entorno OPENAI_API_KEY.")

    client = OpenAI(api_key=api_key)
    
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        raise Exception(f"Error al generar la imagen: {str(e)}")

# Interfaz de usuario de Streamlit


img_description = st.text_input('Hola! describe de la forma más detallada posible la imagen que te gustaría te ayude a generar.')

if st.button('Generar Imagen'):
    if img_description:
        try:
            with st.spinner('Generando imagen...'):
                generated_img = generate_image(img_description)
            st.image(generated_img)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter an image description.")
