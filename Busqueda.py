import pandas as pd
import streamlit as st
import Proceso as pc

st.title("🔍 HERRAMIENTA INFORMATIVA ")

tab1, tab2 = st.tabs(["👤 Datos Cliente", "🎯 Verificacion Campaña"])

# ================= TAB 1 =================
with tab1:
    st.subheader("Búsqueda de Cliente")

    dato = st.number_input(
        "Ingrese DNI (8) o Teléfono (9)",
        min_value=0,
        max_value=999999999,
        step=1,
        key="Ingrese un DNI o Teléfono"
    )

    if dato == 0:
        st.info("Ingrese un DNI o Teléfono")
    elif dato < 999999:
        st.warning("⚠️ Número inválido")
    elif dato > 9999999999:
        st.warning("⚠️ Número inválido")    
    else:
        resultado = pc.buscar(dato)

        if resultado.empty:
            st.warning("⚠️ Cliente no encontrado")
        else:
            st.success("✅ Cliente encontrado")
            st.dataframe(resultado, use_container_width=True)

# ================= TAB 2 =================
with tab2:
    st.subheader("Campaña del Cliente")

    dato2 = st.number_input(
        "Ingrese DNI (8 dígitos)",
        min_value=0,
        max_value=99999999,
        step=1,
        key="dni_campaña"
    )

    if dato2 == 0:
        st.info("Ingrese un DNI")
    elif dato2 < 999999:
        st.warning("⚠️ DNI inválido")
    elif dato2 > 99999999 :
        st.warning("Debes ingresar dni de 8 digitos ⚠️")
    else:
        resultado2 = pc.encontrar(dato2)

        if resultado2.empty:
            st.warning("⚠️ Cliente sin campaña")
        else:
            st.success("✅ Campaña encontrada")
            st.dataframe(resultado2, use_container_width=True)