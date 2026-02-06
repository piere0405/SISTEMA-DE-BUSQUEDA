import pandas as pd
import streamlit as st
import Proceso as pc

st.title("BUSQUEDA DE CLIENTE BASE GENERAL")

dni = st.number_input("INGRESE DNI A BUSCAR :",0,99999999)


resultado = pc.buscar(dni)

st.write("RESULTADOS ENCONTRADOS : " , resultado)