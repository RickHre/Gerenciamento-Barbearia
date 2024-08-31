import streamlit as st
from contextlib import closing
from db_conect import conectar_bd
from datetime import time

# Função para verificar se o horário já está agendado
def horario_disponivel(data, hora):
    query = "SELECT COUNT(*) FROM agendamentos WHERE data = %s AND hora = %s"
    values = (data, hora)
    with closing(conectar_bd()) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, values)
            result = cursor.fetchone()
            return result[0] == 0

# Função para adicionar agendamento
def adicionar_agendamento(nome, data, hora, descricao):
    if horario_disponivel(data, hora):
        query = "INSERT INTO agendamentos (nome, data, hora, descricao) VALUES (%s, %s, %s, %s)"
        values = (nome, data, hora, descricao)
        with closing(conectar_bd()) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, values)
                conn.commit()
        return True
    else:
        return False

# Função para exibir a página de agendamentos
def mostrar_agendamentos():
    st.title("Sistema de Agendamento")

    nome = st.text_input("Nome")
    data = st.date_input("Data")

    # Configurar horário para intervalos de uma em uma hora das 08:00 às 21:00
    horas_disponiveis = [time(hour=h) for h in range(8, 22)]
    hora = st.selectbox("Hora", horas_disponiveis, format_func=lambda t: t.strftime("%H:%M"))
    descricao = st.text_area("Descrição")

    if st.button("Adicionar Agendamento"):
        try:
            if adicionar_agendamento(nome, data, hora.strftime("%H:%M"), descricao):
                st.success("Agendamento adicionado com sucesso!")
            else:
                st.warning("Já existe um agendamento para este horário.")
        except Exception as e:
            st.error(f"Erro ao adicionar agendamento: {e}")
            
    if st.button("Voltar para Login"):
        st.session_state.pagina = "login"

# Chamada da função para exibir a página de agendamentos
#if __name__ == "__main__":
    #mostrar_agendamentos()