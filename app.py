import streamlit as st
#from speech_to_text import get_spoken_text
from image_gen import generate_image
from PIL import Image
import time
from streamlit.components.v1 import html
import base64

# ----- Style (CSS + Gradient) -----
st.markdown("""
    <style>
        /* Gradient background
        .stApp {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 2rem;
        }*/

        /* Sidebar (optional) */
        [data-testid="stSidebar"] {
            background: #3f3f46;
        }

        /* Stylish button */
        .stButton>button {
            background-color: #00c9a7;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 0.5rem 1.2rem;
            margin-top: 1rem;
        }

        .stButton>button:hover {
            background-color: #00796b;
        }

        /* Card look for blocks */
        [data-testid="stVerticalBlock"] {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);

        /* Style the selectbox */
        [data-baseweb="select"] {
            background-color: #2b2b2b; /* Background */
            color: white;              /* Text */
            border-radius: 8px;
            border: 1px solid #00c9a7;
            padding: 4px;
        }

        /* Style selected item in dropdown */
        [data-baseweb="select"] > div {
            color: #ffffff;            /* Text of selected item */
        }

        /* Style dropdown options */
        [data-baseweb="menu"] {
            background-color: #1f1f1f; /* Dropdown background */
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

def play_beep(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        html_code = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        html(html_code, height=0)

def apply_style(prompt, style):
    style_keywords = {
        "Realistic": "highly detailed, realistic photograph",
        "Anime": "anime style, vibrant colors, cel shading",
        "Sketch": "pencil sketch, monochrome, hand-drawn",
        "Oil Painting": "oil painting, thick brush strokes, canvas texture",
        "Cyberpunk": "cyberpunk, neon lights, futuristic city"
    }
    return f"{prompt}, {style_keywords.get(style, '')}"     

st.title("🎤 Voice to Image Generator")

# Style filter
style = st.selectbox("🎨 Choose a Style", ["Realistic", "Anime", "Sketch", "Oil Painting", "Cyberpunk"])

#Image resolution sliders 
st.markdown("### 🖼️ Select Image Resolution")
width = st.slider("Width", min_value=256, max_value=1024, value=512, step=64)
height = st.slider("Height", min_value=256, max_value=1024, value=512, step=64)

prompt = st.text_input("📝 Type your image description prompt here:")

'''if st.button("Generate Image"):
    if not prompt.strip():
        st.error("Please enter a valid prompt.")
    else:
        styled_prompt = apply_style(prompt, style)

        with st.spinner("🧠 Generating image..."):
            img_path = generate_image(styled_prompt, width, height)

        st.image(Image.open(img_path), caption="✨ AI-Generated Image", use_column_width=True)

        with open(img_path, "rb") as f:
            st.download_button("📥 Download Image", f, "generated_image.png", mime="image/png")'''

if st.button("Start Speaking", on_click=None):
    # Play beep
    #play_beep("assets/beep.mp3")
    
    with st.spinner('🎙️ Listening...'):
        prompt = get_spoken_text()

    if prompt == 'ERROR_SPEECH_NOT_RECOGNIZED':
        st.error("❌ Could not capture valid speech input. Please try again.")
    else:
        st.markdown(f"<p class='big-font'>🗣️ You said: <em>{prompt}</em></p>", unsafe_allow_html=True)

        with st.spinner('🧠 Generating image...'):
            time.sleep(1)  # Simulate wait
            styled_prompt = apply_style(prompt, style)
            img_path = generate_image(styled_prompt, width, height)

        st.image(Image.open(img_path), caption="✨ AI-Generated Image", use_container_width=True)

        #Download image
        with open(img_path, "rb") as f:
            st.download_button("📥 Download Image", f, "generated_image.png", mime="image/png")