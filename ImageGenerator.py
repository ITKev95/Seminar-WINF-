from openai import OpenAI
from PIL import Image
import streamlit as st

st.set_page_config(page_title="DALL.E 3 Image Generation")  # Diese Zeile wurde nach oben verschoben

# Put the OpenAI API key in the secrets.toml file at the path ~/.streamlit/secrets.toml in the same directory as the script.
def generate_image(image_description):
  client = OpenAI()
  response = client.images.generate(
    model="dall-e-3",
    prompt=f"{image_description}",
    size="1024x1024",
    quality="standard",
    n=1,
  )

  img_url = response.data[0].url
  return img_url

OpenAI.api_key = st.secrets["OPENAI_API_KEY"]

st.title('DALL.E 3 Image Generation')
st.subheader("Powered by OpenAI and Streamlit")
img_description = st.text_input('Image Description')

if st.button('Generate Image'):
    generated_img = generate_image(img_description)
    st.image(generated_img)