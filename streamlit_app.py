import streamlit as st
import pandas as pd
import numpy as np
st.title("Dhiraj")
df=pd.DataFrame(np.random.randn(50,20),columns=("col %d" % i for i in range(20)))
st.dataframe(df)
st.image('data/VBGY.gif')
st.sidebar.image('data/VBGY.gif')
st.image('data/Skqu.gif')
st.sidebar.image('data/Skqu.gif')
st.image('data/OIP.jpg')
st.sidebar.image('data/OIP.jpg')
col1, col2, col3 = st.columns(3)
with col1:
    st.title("LION")
    st.image('data/VBGY.gif')
    st.sidebar.image('data/VBGY.gif')

with col2:
    st.title("TIGER")
    st.image('data/Skqu.gif')
    st.sidebar.image('data/Skqu.gif')

with col3:
    st.title("DOG")
    st.image('data/OIP.jpg')
    st.sidebar.image('data/OIP.jpg')