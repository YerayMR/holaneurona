import streamlit as st

# Título de la página
st.title("¡Hola neurona!")

# Imagen de la neurona
st.image("image.png", caption="Neurona", use_column_width=True)

# Crear las pestañas
tabs = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

# Pestaña 1: Una entrada y un peso
with tabs[0]:
    st.subheader("Una neurona con una entrada y un peso")
    peso = 0.5  # Peso ajustado
    entrada = st.number_input("Introduzca el valor de la entrada", min_value=0.0, step=0.01, value=0.0)
    if st.button("Calcular la salida", key="btn1"):
        salida = peso * entrada
        st.write(f"La salida de la neurona es: {salida:.2f}")

# Pestaña 2: Dos entradas y dos pesos
with tabs[1]:
    st.subheader("Dos entradas y dos pesos")
    peso_w1 = 1.5  # Peso ajustado
    peso_w2 = 2.5  # Peso ajustado
    entrada_x1 = st.number_input("Entrada x1", min_value=0.0, step=0.01, value=0.0, key="x1_tab2")
    entrada_x2 = st.number_input("Entrada x2", min_value=0.0, step=0.01, value=0.0, key="x2_tab2")
    if st.button("Calcular la salida", key="btn2"):
        salida = peso_w1 * entrada_x1 + peso_w2 * entrada_x2
        st.write(f"La salida de la neurona es: {salida:.2f}")

# Pestaña 3: Tres entradas, tres pesos y un sesgo
with tabs[2]:
    st.subheader("Tres entradas, tres pesos y un sesgo")
    peso_w1 = 1  # Peso ajustado
    peso_w2 = 2  # Peso ajustado
    peso_w3 = 3  # Peso ajustado
    sesgo = 10  # Sesgo ajustado
    entrada_x1 = st.number_input("Entrada x1", min_value=0.0, step=0.01, value=0.0, key="x1_tab3")
    entrada_x2 = st.number_input("Entrada x2", min_value=0.0, step=0.01, value=0.0, key="x2_tab3")
    entrada_x3 = st.number_input("Entrada x3", min_value=0.0, step=0.01, value=0.0, key="x3_tab3")
    if st.button("Calcular la salida", key="btn3"):
        salida = peso_w1 * entrada_x1 + peso_w2 * entrada_x2 + peso_w3 * entrada_x3 + sesgo
        st.write(f"La salida de la neurona es: {salida:.2f}")
