import streamlit as st

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