 
import mysql.connector
from mysql.connector import Error
import streamlit as st

# Função para conectar ao banco de dados MySQL
def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='agenda_db',
            user='root',
            password= ''
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None