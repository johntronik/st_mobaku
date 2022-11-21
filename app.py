import streamlit as st
from PIL import Image

st.markdown('# 1kmメッシュ')
il = [Image.open(f'fig/1000_{i}.png') for i in range(3)]
time1000 = st.slider('1kmの時間', 0, 2)
st.image(il[time1000])


st.markdown('# 250mメッシュ')
il2 = [Image.open(f'fig/250_{i*100}.png') for i in range(24)]
time250 = st.slider('250mの時間', 0, 23)
st.image(il2[time250])


st.markdown('# 50mメッシュ')
il1 = [Image.open(f'fig/50_{i*100}.png') for i in range(24)]
time50 = st.slider('50mの時間', 0, 23)
st.image(il1[time50])
