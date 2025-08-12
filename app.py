# import libraries
import streamlit as st
import eda, predict

# st.write("# Ini Header")
# bagian slide bar
with st.sidebar:
    st.write("# Page Navigation")

    # togle halaman
    page = st.selectbox("Pilih Halaman", ("EDA",'Predict Rating'))

    # test
    st.write(f"Halaman yang dituju {page}")

    st.write("## About")
    # Magic
    '''
    Page ini berisikan hasil analisis data terhadap pemain FIFA 2024
    dan prediksi rating berdasarkan atribut yang dimiliki
    '''


# bagian luar slide bar
if page == 'EDA':
    eda.run()
else:
    predict.run()