import streamlit as st
import pandas as pd
import numpy as np

info = '''Ao selecionar uma especialidade,
todos os pacientes dessa especialidade vao aparecer'''
st.title('Painel de controle de tempos do PA')


def ler_csv(nome_csv, pd_):
    with open(f'{nome_csv}', encoding='utf-8') as csv_file:
        df = pd_.read_csv(csv_file)
    return st.dataframe(df)


def ler_csv_all(nome_csv, pd_):
    with open(f'{nome_csv}', encoding='utf-8') as csv_file:
        df = pd_.read_csv(csv_file)
    return df


filas = st.sidebar.selectbox(
    'Selecione uma fila:',
    ('Triagem', 'Cadastro', 'Medico', 'Todos'))
filas

if filas == 'Triagem':
    # st.write('Tiagem')
    ler_csv("TRIAGEM.csv", pd)
    df = ler_csv_all("filas.csv", pd)
    especialidades = np.unique(df['Especialidades'].values)
    options = st.sidebar.multiselect(
        'Escolha a Especialidade',
        especialidades,
        help=info,
        default=['CLÍNICA MÉDICA']
        )

    st.write('Especialidade selecionada:', options)
    df_filtrado = df[df['Especialidades'].isin(options)]
    st.dataframe(df_filtrado)
elif filas == 'Cadastro':
    ler_csv("CADASTRO.csv", pd)
elif filas == 'Medico':
    ler_csv("MEDICO.csv", pd)
else:
    ler_csv("TRIAGEM.csv", pd)
    ler_csv("CADASTRO.csv", pd)
    ler_csv("MEDICO.csv", pd)
