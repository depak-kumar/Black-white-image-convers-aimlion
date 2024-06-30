

# import streamlit as st
# from PIL import Image
# import numpy as np

# # Function to convert image to black and white
# def convert_to_bw(image, intensity):
#     # Convert the image to grayscale
#     grayscale = image.convert('L')
#     # Convert grayscale image to numpy array
#     bw_array = np.array(grayscale)
#     # Apply intensity level to create black and white effect
#     threshold = 255 * intensity
#     bw_array[bw_array < threshold] = 0
#     bw_array[bw_array >= threshold] = 255
#     # Convert numpy array back to image
#     bw_image = Image.fromarray(bw_array)
#     return bw_image

# # Function to convert image to color
# def convert_to_color(image):
#     # Convert grayscale image to RGB
#     color_image = image.convert('RGB')
#     return color_image

# # Main Streamlit app
# def main():
#     st.title("Image Converter")

#     # Navigation bar
#     nav_option = st.sidebar.radio("Navigation", ["Convert to Black and White", "Convert to Color"])

#     if nav_option == "Convert to Black and White":
#         # File uploader
#         uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

#         if uploaded_file is not None:
#             # Display uploaded image
#             st.subheader("Original Image")
#             original_image = Image.open(uploaded_file)
#             st.image(original_image, caption="Original Image", use_column_width=True)

#             # Add intensity slider
#             intensity = st.slider("Intensity", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

#             # Convert image to black and white
#             bw_image = convert_to_bw(original_image, intensity)
#             st.subheader("Black and White Image")
#             st.image(bw_image, caption="Black and White Image", use_column_width=True)

#     elif nav_option == "Convert to Color":
#         # File uploader for black and white image
#         uploaded_bw_file = st.file_uploader("Upload a black and white image", type=["jpg", "jpeg", "png"])

#         if uploaded_bw_file is not None:
#             # Display uploaded black and white image
#             st.subheader("Black and White Image")
#             bw_image = Image.open(uploaded_bw_file)
#             st.image(bw_image, caption="Black and White Image", use_column_width=True)

#             # Convert black and white image to color
#             color_image = convert_to_color(bw_image)
#             st.subheader("Color Image")
#             st.image(color_image, caption="Color Image", use_column_width=True)

# if __name__ == "__main__":
#     main()


import streamlit as st
from PIL import Image
import numpy as np
import cv2
# import streamlit as st
st.markdown(
    """
    # <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    """,
    unsafe_allow_html=True
)
st.markdown('''
  <!-- As a link -->
<nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Project - Converting Images to Black and White and Vice-versa</a>
  </div>
</nav>

<!-- As a heading -->
<nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <span class="navbar-brand mb-0 h1"></span>
  </div>
</nav>''',unsafe_allow_html=True)

   
# Run the app

# Function to convert image to black and white
def convert_to_bw(image, intensity):
    # Convert the image to grayscale
    grayscale = image.convert('L')
    # Convert grayscale image to numpy array
    bw_array = np.array(grayscale)
    # Apply intensity level to create black and white effect
    threshold = 255 * intensity
    bw_array[bw_array < threshold] = 0
    bw_array[bw_array >= threshold] = 255
    # Convert numpy array back to image
    bw_image = Image.fromarray(bw_array)
    return bw_image

# Function to convert black and white image to color with adjustable intensity
def colorize_image(image, intensity):
    # Convert black and white image to OpenCV format
    bw_array = np.array(image)
    bw_array = cv2.cvtColor(bw_array, cv2.COLOR_RGB2GRAY)
    # Adjust the intensity of colorization
    colorized_array = np.stack((bw_array,) * 3, axis=-1)  # Convert to 3-channel grayscale
    colorized_image = np.clip(colorized_array * intensity, 0, 255).astype(np.uint8)
    # Convert numpy array back to image
    colorized_image = Image.fromarray(colorized_image)
    return colorized_image

# Main Streamlit app
def main():
    st.title("Image Converter To Black and White")
    st.image('https://th.bing.com/th/id/OIP.bFBDWGp_UkmgDeZFYBvrFwHaEK?w=321&h=181&c=7&r=0&o=5&dpr=1.3&pid=1.7')
    # Navigation bar
    nav_option = st.sidebar.radio("Navigation", ["Convert to Black and White", "Convert to Color"])

    if nav_option == "Convert to Black and White":
        # File uploader
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Display uploaded image
            st.subheader("Original Image")
            original_image = Image.open(uploaded_file)
            st.image(original_image, caption="Original Image", use_column_width=True)

            # Add intensity slider
            intensity = st.slider("Intensity", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

            # Convert image to black and white
            bw_image = convert_to_bw(original_image, intensity)
            st.subheader("Black and White Image")
            st.image(bw_image, caption="Black and White Image", use_column_width=True)

    elif nav_option == "Convert to Color":
        # File uploader for black and white image
        uploaded_bw_file = st.file_uploader("Upload a black and white image", type=["jpg", "jpeg", "png"])

        # Add slider for color intensity
       

        if uploaded_bw_file is not None:
            # Display uploaded black and white image
            st.subheader("Black and White Image")
            bw_image = Image.open(uploaded_bw_file)
            st.image(bw_image, caption="Black and White Image", use_column_width=True)
            intensity = st.slider("Color Intensity", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
            # Convert black and white image to color with adjustable intensity
            colorized_image = colorize_image(bw_image, intensity)
            st.subheader("Colorized Image")
            st.image(colorized_image, caption="Colorized Image", use_column_width=True)

# if __name__ == "__main__":
    # main1()

main()
st.subheader("Made BY Deepak Kumar")
