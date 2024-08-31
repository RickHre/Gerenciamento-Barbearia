import streamlit as st
from db_conect import conectar_bd
import bcrypt

# Função para criar uma nova conta
def criar_conta(nome, email, data_nascimento, login, senha):
    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email, data_nascimento, login, senha) VALUES (%s, %s, %s, %s, %s)",
                       (nome, email, data_nascimento, login, senha))
        conexao.commit()
        conexao.close()
        st.success("Conta criada com sucesso!")
        st.session_state.pagina = "login"

#Função para criar uma nova conta e salvar senha com biblioteca criptografada
'''def criar_conta(nome, email, data_nascimento, login, senha):
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    with conectar_bd() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios (nome, email, data_nascimento, login, senha) VALUES (%s, %s, %s, %s, %s)",
                           (nome, email, data_nascimento, login, hashed_senha))
            conexao.commit()
    st.success("Conta criada com sucesso!")
    st.session_state.pagina = "login"

def autenticar(login, senha):
    with conectar_bd() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT senha FROM usuarios WHERE login=%(login)s", {'login': login})
            stored_senha = cursor.fetchone()
            if stored_senha and bcrypt.checkpw(senha.encode('utf-8'), stored_senha[0].encode('utf-8')):
                return True
    return False'''
