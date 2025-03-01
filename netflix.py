import streamlit as st 
import pandas as pd 
import numpy as np 

import streamlit as st
import pandas as pd

st.title('Netflix App')

DATA_URL = 'https://github.com/adsoftsito/streamlit-m5/blob/main/movies.csv'

@st.cache_data
def load_data(nrows=1000):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding='latin1')
    data.columns = data.columns.str.lower()  # Convertir nombres de columnas a minúsculas
    return data

def filter_data_by_filme(filme, data):
    if 'name' in data.columns:
        return data[data['name'].str.upper().str.contains(filme, na=False)]
    return pd.DataFrame()  # Retorna DataFrame vacío si no existe la columna

def filter_data_by_director(director, data):
    return data[data['director'] == director]

# Carga de datos
data_load_state = st.text('Cargando datos...')
data = load_data()
data_load_state.text("¡Datos cargados exitosamente!")

# Mostrar todos los filmes
if st.sidebar.checkbox('Mostrar todos los filmes'):
    st.subheader('Todos los filmes')
    st.write(data)

# Filtrado por título del filme
titulofilme = st.sidebar.text_input('Título del filme:')
btnBuscar = st.sidebar.button('Buscar filmes')

if btnBuscar and titulofilme:
    data_filme = filter_data_by_filme(titulofilme.upper(), data)
    count_row = data_filme.shape[0]  
    st.write(f"Total filmes encontrados: {count_row}")
    st.write(data_filme)

# Filtrado por director
if 'director' in data.columns:
    directores_unicos = data['director'].dropna().unique()
    selected_director = st.sidebar.selectbox("Seleccionar Director", directores_unicos)
    btnFilterbyDirector = st.sidebar.button('Filtrar por Director')

    if btnFilterbyDirector:
        filterbydir = filter_data_by_director(selected_director, data)
        count_row = filterbydir.shape[0]
        st.write(f"Total filmes dirigidos por {selected_director}: {count_row}")
        st.dataframe(filterbydir)