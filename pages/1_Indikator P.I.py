import streamlit as st
import pandas as pd
import numpy as np

st.title("Indikator Perubahan Iklim")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("suhu bulan januari")
    st.metric(label="Temperature", value="30 °C", delta="-0.2 °C")

with col2:
    st.subheader("suhu bulan desember")
    st.metric(label="Temperature", value="31 °C", delta="0.2 °C")

with col1:
    st.subheader("suhu bulan november")
    st.metric(label="Temperature", value="33 °C", delta="1.2 °C")