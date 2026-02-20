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

# --- HOME SECTION ---
if selected == "Home":
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        # Placeholder for your image - ensure the file exists in your directory
        st.image('my imh.jpg', use_container_width=True)

    with col2:
        st.title("Muhammad Shahzaib")
        st.subheader("AI Engineer & ML Specialist")
        st.write("""
            As a passionate and results-driven AI Engineer, I specialize in designing, 
            developing, and deploying machine learning models to solve complex problems. 
            I bridge the gap between raw data and actionable intelligence.
        """)

        st.write("---")
        st.header("Technical Arsenal")

        skills = ["Python", "TensorFlow", "PyTorch", "Scikit-Learn", "OpenCV", "NLP", "Streamlit", "SQL", "Docker"]
        skill_html = "".join([f'<div class="skill-tag">{s}</div>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)


        



