import pandas as pd
import streamlit as st

st.title('Netflix App')

DATA_URL = ('movies.csv')
DATE_COLUMN = 'released'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Done')

no_filter = st.sidebar.checkbox(label='Mostrar todos los filmes', value=True)
if no_filter == True:
    st.header('Todos los filmes')
    st.dataframe(data)

name = st.sidebar.text_input('Título del filme:')
if st.sidebar.button('Buscar filmes'):
    no_filter = False
    df_name = data[data['name'].str.lower().str.contains(name.lower())]
    st.header('Filmes filtrados por nombres')
    st.dataframe(df_name)

director = st.sidebar.selectbox(label='Seleccionar Director', options=data['director'].unique())
if st.sidebar.button('Filtrar director'):
    no_filter = False
    df_dir = data[data['director'].str.contains(director)]
    st.header('Filmes filtrados por director')
    st.dataframe(df_dir)