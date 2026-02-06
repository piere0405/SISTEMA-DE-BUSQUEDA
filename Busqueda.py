import pandas as pd
import streamlit as st
import Proceso as pc

st.title("BUSQUEDA DE CLIENTE BASE GENERAL")

dni = st.number_input("INGRESE DNI O NUMERO A BUSCAR :",0,999999999)


resultado = pc.buscar(dni)

if resultado.empty:
    st.warning("⚠️ Cliente no encontrado en la base de datos")
else:
    st.success("✅ Cliente encontrado")
    st.dataframe(resultado)