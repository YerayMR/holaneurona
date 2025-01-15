import streamlit as st
from PIL import Image
import os

# Título de la página
st.title("¡Hola neurona!")

# Imagen de la neurona
image_path = "img.png"
if os.path.exists(image_path):
    st.image(image_path, caption="Neurona", use_container_width=True)
else:
    st.error("La imagen 'img.png' no se encuentra en el directorio.")

# Crear las pestañas
tabs = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

# Pestaña 1: Una entrada y un peso
with tabs[0]:
    st.subheader("Una neurona con una entrada y un peso")
    entrada = st.number_input("Introduzca el valor de la entrada", min_value=0.0, step=0.01, value=0.0)
    peso = st.number_input("Introduzca el valor del peso", min_value=0.0, step=0.01, value=0.5)
    if st.button("Calcular la salida", key="btn1"):
        salida = peso * entrada
        st.write(f"La salida de la neurona es: {salida:.2f}")

# Pestaña 2: Dos entradas y dos pesos
with tabs[1]:
    st.subheader("Dos entradas y dos pesos")
    entrada_x1 = st.number_input("Entrada x1", min_value=0.0, step=0.01, value=0.0, key="x1_tab2")
    entrada_x2 = st.number_input("Entrada x2", min_value=0.0, step=0.01, value=0.0, key="x2_tab2")
    peso_w1 = st.number_input("Peso w1", min_value=0.0, step=0.01, value=1.5, key="w1_tab2")
    peso_w2 = st.number_input("Peso w2", min_value=0.0, step=0.01, value=2.5, key="w2_tab2")
    if st.button("Calcular la salida", key="btn2"):
        salida = peso_w1 * entrada_x1 + peso_w2 * entrada_x2
        st.write(f"La salida de la neurona es: {salida:.2f}")

# Pestaña 3: Tres entradas, tres pesos y un sesgo
with tabs[2]:
    st.subheader("Tres entradas, tres pesos y un sesgo")
    entrada_x1 = st.number_input("Entrada x1", min_value=0.0, step=0.01, value=0.0, key="x1_tab3")
    entrada_x2 = st.number_input("Entrada x2", min_value=0.0, step=0.01, value=0.0, key="x2_tab3")
    entrada_x3 = st.number_input("Entrada x3", min_value=0.0, step=0.01, value=0.0, key="x3_tab3")
    peso_w1 = st.number_input("Peso w1", min_value=0.0, step=0.01, value=1.0, key="w1_tab3")
    peso_w2 = st.number_input("Peso w2", min_value=0.0, step=0.01, value=2.0, key="w2_tab3")
    peso_w3 = st.number_input("Peso w3", min_value=0.0, step=0.01, value=3.0, key="w3_tab3")
    sesgo = st.number_input("Sesgo", min_value=0.0, step=0.01, value=10.0, key="sesgo_tab3")
    if st.button("Calcular la salida", key="btn3"):
        salida = peso_w1 * entrada_x1 + peso_w2 * entrada_x2 + peso_w3 * entrada_x3 + sesgo
        st.write(f"La salida de la neurona es: {salida:.2f}")
