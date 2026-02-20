import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="Shahzaib | AI Portfolio", page_icon="🤖", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp {
        background: #0e1117;
        color: #ffffff;
    }
    .skill-tag {
        display: inline-block;
        padding: 5px 15px;
        margin: 5px;
        border-radius: 20px;
        background-color: #1e222d;
        border: 1px solid #00d4ff;
        font-size: 14px;
        transition: 0.3s;
    }
    .skill-tag:hover {
        background-color: #00d4ff;
        color: #000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Resume", "Contact"],
    icons=["house", "cpu", "file-text", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# --- SIDEBAR (Optional cleanup) ---
st.sidebar.title("Find Me Online")
st.sidebar.info("🔗 [LinkedIn](https://linkedin.com)\n\n🐙 [GitHub](https://github.com)")