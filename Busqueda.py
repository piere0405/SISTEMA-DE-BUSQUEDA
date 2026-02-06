import pandas as pd
import streamlit as st
import Proceso as pc

st.title("BUSQUEDA DE CLIENTE BASE GENERAL")

dato = st.number_input(
    "INGRESE DNI O NUMERO A BUSCAR :",
    min_value=0,
    max_value=999999999,
    step=1
)

if dato == 0:
    st.info("Ingrese un DNI (8 dígitos) o Teléfono (9 dígitos)")
elif dato > 1 and dato < 9999999:
    st.warning("⚠️ Ingrese un numero valido")
else:
    resultado = pc.buscar(dato)

    if resultado.empty:
        st.warning("⚠️ Cliente no encontrado en la base de datos")
    else:
        st.success("✅ Cliente encontrado")
        st.dataframe(resultado)