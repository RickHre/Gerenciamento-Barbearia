import streamlit as st
from autent import autenticar
from conta import criar_conta
from agendamento import mostrar_agendamentos
from datetime import date
from datetime import time

# Função para exibir a página de login
def mostrar_login():
    st.title("Home page")
    
    login = st.text_input("Login")
    senha = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        if autenticar(login, senha):
            st.success("Login bem-sucedido!")
            st.session_state.pagina = "mostrar_agendamentos"
        else:
            st.error("Login ou senha incorretos. Tente novamente.")
    
    if st.button("Cadastrar"):
        st.session_state.pagina = "criar_conta"

# Função para exibir a página de criação de conta
def mostrar_criar_conta():
    st.title("Criar Conta")
    
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    data_nascimento = st.date_input("Data de Nascimento", min_value=date(1900, 1, 1), max_value=date.today())  # Permitir datas até hoje
    login = st.text_input("Login")
    senha = st.text_input("Senha", type="password")
    
    if st.button("Registrar"):
        criar_conta(nome, email, data_nascimento, login, senha)
    
    if st.button("Voltar para Login"):
        st.session_state.pagina = "login"

# Inicializar a página
if 'pagina' not in st.session_state:
    st.session_state.pagina = "login"

# Exibir a página correta com base no estado
if st.session_state.pagina == "login":    
    mostrar_login()
elif st.session_state.pagina == "criar_conta":    
    mostrar_criar_conta()
elif st.session_state.pagina == "mostrar_agendamentos":    
    mostrar_agendamentos()
