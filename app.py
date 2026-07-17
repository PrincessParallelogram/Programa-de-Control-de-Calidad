"""
app.py

Punto de entrada de la aplicación.
"""

import streamlit as st

from interfaz import ejecutar_app


st.set_page_config(
    page_title="Sistema de Auditoría",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

ejecutar_app()