import streamlit as st
from PIL import Image

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("ð Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.markdown('# 1kmã¡ãã·ã¥')
    il = [Image.open(f'fig/1000_{i}.png') for i in range(3)]
    time1000 = st.slider('1kmã®æé', 0, 2)
    st.image(il[time1000])


    st.markdown('# 250mã¡ãã·ã¥')
    il2 = [Image.open(f'fig/250_{i*100}.png') for i in range(24)]
    time250 = st.slider('250mã®æé', 0, 23)
    st.image(il2[time250])


    st.markdown('# 50mã¡ãã·ã¥')
    il1 = [Image.open(f'fig/50_{i*100}.png') for i in range(24)]
    time50 = st.slider('50mã®æé', 0, 23)
    st.image(il1[time50])
