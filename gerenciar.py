import streamlit as st
from contextlib import closing
from db_conect import conectar_bd

# Função para ler dados da tabela agendamentos
def ler_agendamentos():
    query = "SELECT * FROM agendamentos"
    with closing(conectar_bd()) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query)
            return cursor.fetchall()

# Função para ler dados da tabela usuarios
def ler_usuarios():
    query = "SELECT * FROM usuarios"
    with closing(conectar_bd()) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query)
            return cursor.fetchall()

# Função para deletar um agendamento
def deletar_agendamento(id):
    query = "DELETE FROM agendamentos WHERE id = %s"
    with closing(conectar_bd()) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, (id,))
            conn.commit()

# Função para deletar um usuário
def deletar_usuario(id):
    query = "DELETE FROM usuarios WHERE id = %s"
    with closing(conectar_bd()) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, (id,))
            conn.commit()

# Interface do Streamlit
st.title("Sistema de Gerenciamento de Agenda")

# Barra lateral para seleção
st.sidebar.header("Seleção")
opcao = st.sidebar.radio("Escolha uma opção", ("Agendamentos", "Usuários"))

if opcao == "Agendamentos":
    st.sidebar.subheader("Agendamentos")
    agendamentos = ler_agendamentos()
    agendamento_selecionado = st.sidebar.selectbox("Selecione um agendamento", agendamentos, format_func=lambda x: f"{x[1]} - {x[2]} {x[3]}")
    
    if agendamento_selecionado:
        st.subheader("Detalhes do Agendamento")
        st.write(f"ID: {agendamento_selecionado[0]}")
        st.write(f"Nome: {agendamento_selecionado[1]}")
        st.write(f"Data: {agendamento_selecionado[2]}")
        st.write(f"Hora: {agendamento_selecionado[3]}")
        st.write(f"Descrição: {agendamento_selecionado[4]}")
        if st.button(f"Deletar Agendamento {agendamento_selecionado[0]}"):
            deletar_agendamento(agendamento_selecionado[0])
            st.success(f"Agendamento {agendamento_selecionado[0]} deletado com sucesso!")

elif opcao == "Usuários":
    st.sidebar.subheader("Usuários")
    usuarios = ler_usuarios()
    usuario_selecionado = st.sidebar.selectbox("Selecione um usuário", usuarios, format_func=lambda x: f"{x[1]} - {x[2]}")
    
    if usuario_selecionado:
        st.subheader("Detalhes do Usuário")
        st.write(f"ID: {usuario_selecionado[0]}")
        st.write(f"Nome: {usuario_selecionado[1]}")
        st.write(f"Email: {usuario_selecionado[2]}")
        if st.button(f"Deletar Usuário {usuario_selecionado[0]}"):
            deletar_usuario(usuario_selecionado[0])
            st.success(f"Usuário {usuario_selecionado[0]} deletado com sucesso!")
