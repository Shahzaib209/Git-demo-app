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

<<<<<<< HEAD
# --- SIDEBAR (Optional cleanup) ---
st.sidebar.title("Find Me Online")
st.sidebar.info("🔗 [LinkedIn](https://linkedin.com)\n\n🐙 [GitHub](https://github.com)")
=======
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

# --- PROJECTS SECTION ---
elif selected == "Projects":
        st.title("🚀 Featured Projects")

        col_a, col_b = st.columns(2)

        with col_a:
            with st.container(border=True):
                st.subheader("Computer Vision: Object Detection")
                st.write("Implemented a real-time YOLOv8 model for industrial safety monitoring.")
                st.button("View Source Code", key="proj1")

        with col_b:
            with st.container(border=True):
                st.subheader("NLP: Sentiment Analyzer")
                st.write("A deep learning model using Transformers to analyze customer feedback.")
                st.button("View Source Code", key="proj2")



# --- RESUME SECTION ---
elif selected == "Resume":
    st.title("📄 Resume")

    # You can allow users to download your PDF
    with open("your_resume.pdf", "rb") as file:
        st.download_button(
            label="Download Full Resume",
            data=file,
            file_name="Shahzaib_AI_Resume.pdf",
            mime="application/pdf"
        )

    st.markdown("""
    ### Experience
    **AI Engineer Intern** | *Tech Solutions Inc.*
    - Built and optimized CNN models reducing error rates by 15%.
    ### Education
    **BS in Artificial Intelligence** | *Islamia University of Bahawalpur*
    """)



# --- CONTACT SECTION ---
elif selected == "Contact":
    st.title("📩 Get In Touch")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

        if submit:
            st.success(f"Thanks {name}, your message has been 'sent' (connect a backend here)!")






>>>>>>> home_page
