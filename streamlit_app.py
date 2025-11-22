import streamlit as st
from PIL import Image
import base64
import os
import requests
from streamlit_lottie import st_lottie
import time

# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------
st.set_page_config(
    page_title="Happy Birthday My cutiee pai ❤️ ",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------
# UTILITY FUNCTIONS
# ---------------------------------------
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Load Premium Animations
lottie_birthday = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_u4yrau.json") # Gift/Balloons
lottie_cake = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_w51pcehl.json") # Cake
lottie_hearts = load_lottieurl("https://lottie.host/5870f484-097e-476b-8871-385241333724/r7Zz7vUqZc.json") # Floating Hearts

# ---------------------------------------
# CSS STYLING (THE WOW FACTOR)
# ---------------------------------------
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600&family=Sacramento&display=swap');

    /* Animated Gradient Background - Restored Blue & Red Combo */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Glassmorphism Card Design */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 30px;
        margin-bottom: 30px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
    }

    /* Typography */
    h1 {
        font-family: 'Great Vibes', cursive;
        color: #fff;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.2);
        font-size: 70px !important;
        font-weight: normal;
        margin-bottom: 0px;
    }

    h2, h3 {
        font-family: 'Great Vibes', cursive;
        color: #fff; 
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        font-weight: normal;
    }
    
    p, .stMarkdown, .stText {
        font-family: 'Poppins', sans-serif;
        color: #fff;
        font-size: 18px;
        line-height: 1.6;
        text-shadow: 0px 1px 2px rgba(0,0,0,0.1);
    }

    /* Signature Style */
    .signature {
        font-family: 'Sacramento', cursive;
        font-size: 35px;
        color: #fff;
        text-align: right;
        margin-top: 20px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }

    /* Photo Frame - Polaroid Style */
    .polaroid-frame {
        background: white;
        padding: 15px; 
        padding-bottom: 60px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        transform: rotate(-2deg);
        transition: all 0.4s ease;
        border-radius: 4px;
        width: 80%;
        margin: 0 auto;
    }
    
    .polaroid-frame:hover {
        transform: rotate(0deg) scale(1.02);
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
        z-index: 10;
    }

    .polaroid-frame img {
        width: 100%;
        border-radius: 2px;
        object-fit: cover;
    }

    /* Custom Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #ff8a00, #e52e71);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 12px 28px;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(229, 46, 113, 0.4);
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(229, 46, 113, 0.6);
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# HEADER SECTION
# ---------------------------------------
# ---------------------------------------
# HEADER SECTION (FIXED PERFECT ALIGNMENT)
# ---------------------------------------
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.write("")  # padding
    if lottie_birthday:
        st_lottie(lottie_birthday, height=140, key="animation_top", speed=1)
    else:
        st.write("🎉")

with col2:
    st.markdown("""
        <div style="text-align: center; margin-top: 30px;">
            <h1 style="font-size: 75px; margin-bottom: -10px;">Happy Birthday</h1>
            <h1 style="font-size: 75px;">My cutiee pai ❤️</h1>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.write("")  # padding
    st.markdown('<div style="margin-top: 40px; font-size: 90px;">💖</div>', unsafe_allow_html=True)



st.markdown("""
<div class="glass-card">
    <p style="font-size: 20px; font-weight: 600; color: #fff;">
        <i>To the girl who brings magic into the mundane. ✨</i>
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------------------------------
# ELEGANT PHOTO GALLERY
# ---------------------------------------
image_folder = "images"
if not os.path.exists(image_folder):
    st.error("⚠️ System Check: Please create an 'images' folder and add her photos there.")
    images = []
else:
    # Sort images to keep order consistent
    images = sorted([os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png'))])

if images:
    if "photo_index" not in st.session_state:
        st.session_state.photo_index = 0

    # Layout for Gallery
    c_prev, c_image, c_next = st.columns([1, 6, 1])

    with c_prev:
        st.write("\n\n\n\n\n")
        if st.button("❮"):
            st.session_state.photo_index = (st.session_state.photo_index - 1) % len(images)
            st.rerun()

    with c_image:
        img_path = images[st.session_state.photo_index]
        with open(img_path, "rb") as f:
            img_data = base64.b64encode(f.read()).decode()
        
        st.markdown(f"""
        <div class="polaroid-frame">
            <img src="data:image/jpeg;base64,{img_data}">
            <div style="text-align: center; font-family: 'Sacramento', cursive; font-size: 28px; margin-top: 15px; color: #444;">
                Timeless Moments ❤️
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c_next:
        st.write("\n\n\n\n\n")
        if st.button("❯"):
            st.session_state.photo_index = (st.session_state.photo_index + 1) % len(images)
            st.rerun()
            
else:
    st.info("Add photos to the 'images' folder to unlock the gallery.")

st.write("---")

# ---------------------------------------
# THE HEARTFELT LETTER (Corrected & Beautified)
# ---------------------------------------
st.markdown("""
<div class="glass-card" style="text-align: left;">
    <h2 style="text-align: center; font-size: 40px;">A Note for You...</h2>
    <p>
        <b>Dear Swati,</b><br><br>
        Some people just make the world brighter by being in it, and you are definitely one of them. 
        I often find myself looking for words to describe exactly what you mean to me, but honestly, 
        feelings this special don’t fit into simple definitions.
        <br><br>
        There is absolutely no competition for your smile—it’s my favorite sight. 
        Every conversation with you turns into a memory I want to keep. 
        You have this rare ability to make ordinary days feel extraordinary, and 
        chaos feel like calm.
        <br><br>
        Whatever this bond is, it is my favorite thing. You are essential.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------
# "WHAT MAKES YOU SPECIAL" (Interactive)
# ---------------------------------------
st.markdown("<h3 style='text-align: center; margin-top: 20px;'>✨ The Little Things ✨</h3>", unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    with st.expander("💖 Your Energy"):
        st.write("You carry a vibe that can light up the darkest rooms. It’s rare, and it’s beautiful.")
    with st.expander("🦋 Your Impact"):
        st.write("You don't just exist in my life; you add color to it. Everything is just better when you are around.")

with col_b:
    with st.expander("🌙 The Connection"):
        st.write("Talking to you is effortless. It feels like home, excitement, and peace all at once.")
    with st.expander("⚡ Just You"):
        st.write("You are perfectly, uniquely you. And that is my favorite thing about the world.")

# ---------------------------------------
# FINAL SURPRISE & SIGN-OFF
# ---------------------------------------
st.write("")
st.write("")

col_centered = st.columns([1, 2, 1])
with col_centered[1]:
    if st.button("🎁 Click for a Birthday Wish"):
        st.balloons()
        time.sleep(1.5)
        
        # Display Cake Animation
        if lottie_cake:
            st_lottie(lottie_cake, height=250, key="cake_anim")
        
        # Final Message Card
        st.markdown("""
        <div class="glass-card" style="background: rgba(255, 245, 238, 0.9); border: 2px solid #ffb7b2;">
            <h2 style="color: #e52e71; margin-bottom: 10px;">Happy Birthday, Swati! 🎂</h2>
            <p style="color: #2e1c2b;">
                May this year bring you as much joy as you bring to everyone around you.<br>
                Keep shining, keep smiling, and never forget how incredibly special you are.
            </p>
            <div class="signature" style="color: #e52e71;">
                With all my love,<br>
                Yash Tripathi
            </div>
        </div>
        """, unsafe_allow_html=True)