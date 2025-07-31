import streamlit as st
from PIL import Image
import os

# Set page configuration
st.set_page_config(page_title="Reasons Why I Love Oge", layout="centered")

# Custom background color
st.markdown(
    """
    <style>
        body {
            background-color: #fff0f5;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown(
    "<h2 style='text-align: center; color: pink;'>Welcome my Princess to the reasons why I Love You So So Much</h2>",
    unsafe_allow_html=True
)

# Reasons and absolute image paths
reasons = [
    "You always know what to say when I'm down 😍",
    "You make me laugh even when I don’t want to 😄",
    "You believe in me more than I do 💖",
    "Your hugs feel like home 🤗",
    "You’re my favorite person in the whole world 🌍",
    "Your Ass Jiggles when you walk tooooooo 🍑"
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_paths = [os.path.join(BASE_DIR, f"reason{i+1}.png") for i in range(6)]

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = 0

# Buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("💌 Show Me a Reason"):
        st.session_state.index += 1
with col2:
    if st.button("🔄 Restart"):
        st.session_state.index = 0

# Display reason and image
i = st.session_state.index

if i < len(reasons):
    st.markdown(f"<h4 style='color: darkred;'>{reasons[i]}</h4>", unsafe_allow_html=True)
    image = Image.open(image_paths[i])
    st.image(image, width=500)
else:
    st.markdown(
        "<h4 style='color: darkred;'>That's not even all!!! There's so much more but I can't list them all — just know you're perfect 💕</h4>",
        unsafe_allow_html=True
    )
