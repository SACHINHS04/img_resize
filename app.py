from PIL import Image
import streamlit as st

# Open the image
image = Image.open("image.jpg")

# Get the desired size from the user
desired_size = st.sidebar.slider("Select the desired size", min_value=100, max_value=800, value=400)

# Resize the image
image = image.resize((desired_size, desired_size))

# Get the desired number of channels from the user
desired_channels = st.sidebar.selectbox("Select the desired number of channels", ["RGB", "RGBA", "Grayscale"])

# Convert the image to the desired number of channels
if desired_channels == "RGB":
    image = image.convert("RGB")
elif desired_channels == "RGBA":
    image = image.convert("RGBA")
else:
    image = image.convert("L")

# Show the image
st.image(image, caption="Resized Image")
if st.button("Download Resized Image"):
    image.save("resized_image.jpg")
    st.success("Image downloaded!")

