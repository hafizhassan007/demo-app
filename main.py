import streamlit as st

st.title("Welcome to Corvit HCCDA-AI")
st.header("This is a simple Streamlit app.")
st.subheader("We are learning Streamlit.")
st.markdown("#### 4th heading")
st.markdown("### 3rd heading")
st.text(2)
st.write(2)
st.success("registration successful")
st.info("for more information")
st.warning("this is a warning")
st.error("this is an error")
img = "download.jpg"
st.image(img , caption="corvit logo", width=200)
if st.checkbox('male'):
    st.text("you are male")
if st.checkbox('female'):
    st.text("you are female")

status = st.radio("Select your gender", ("male", "female"))
if status == "male":
    st.success("you are brave")
else:
    st.success("you are kind lady")

hobby = st.selectbox("select your hobby", ["cricket", "football", "hockey"])
st.write("your hobby is", hobby)

if st.button("click me", type="primary"):
    st.write("you clicked me")

level = st.slider("select your level", 1, 10)    