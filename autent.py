from db_conect import conectar_bd

# Função para autenticar usuário
def autenticar(login, senha):
    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE login=%s AND senha=%s", (login, senha))
        usuario = cursor.fetchone()
        cursor.close()
        conexao.close()
        if usuario:
            return True
    return False
