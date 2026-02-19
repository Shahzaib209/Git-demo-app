import streamlit as st

import streamlit as st
from streamlit_option_menu import option_menu # You may need to: pip install streamlit-option-menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="Muhammad Shahzaib | AI Engineer", page_icon="🤖", layout="wide")

# --- CUSTOM CSS ---
# This injects custom styles to make the site feel less like a "dashboard"
st.markdown("""
    <style>
    .main {
        background-color: #0f1116;
        color: #ffffff;
    }
    .stApp {
        background: linear-gradient(135deg, #0f1116 0%, #1a1c23 100%);
    }
    h1, h2, h3 {
        color: #00d4ff !important;
    }
    .skill-tag {
        display: inline-block;
        padding: 5px 15px;
        margin: 5px;
        border-radius: 20px;
        background-color: #1e222d;
        border: 1px solid #00d4ff;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Muhammad Shahzaib")
col1,col2 = st.columns(2)

with col1:
    st.image('my imh.jpg')
with col2:
    st.write('''As a passionate and results-driven AI Engineer, I specialize in designing, developing, and deploying machine learning and deep learning models to solve complex real-world problems. With a strong foundation in Python and hands-on experience with frameworks like TensorFlow and PyTorch, I am adept at every stage of the AI project lifecycle, from data preprocessing and feature engineering to model training, evaluation, and deployment.''')


st.header('About')
st.markdown('''A passionate AI/ML Engineer. Ready to dive deep in the world of AI''')
st.subheader('Skills')
st.markdown(''''Data Preprocessing and Feature Engineering''')