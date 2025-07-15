# Paso 1: Importar librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Paso 2: Leer el archivo CSV (asegúrate que esté en la misma carpeta que app.py)
try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("🚨 El archivo 'vehicles_us.csv' no se encuentra en la misma carpeta que app.py.")
    st.stop()

# Paso 3: Crear el encabezado de la app
st.header('Análisis de vehículos en venta en EE.UU.')

# Paso 4: Botón para mostrar histograma
hist_button = st.button('Mostrar histograma de kilometraje')

if hist_button:
    st.write('Histograma del kilometraje de los autos (columna: odometer)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Paso 5: Botón para mostrar gráfico de dispersión
scatter_button = st.button('Mostrar gráfico de dispersión: precio vs. kilometraje')

if scatter_button:
    st.write('Gráfico de dispersión entre precio y kilometraje')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)


