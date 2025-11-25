import sqlite3
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def criar_tabela():
    con = sqlite3.connect("usuarios.db")
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            usuario TEXT PRIMARY KEY,
            senha TEXT
        )
    """)
    con.commit()
    con.close()

def verificar_login(usuario, senha):
    con = sqlite3.connect("usuarios.db")
    cursor = con.cursor()
    cursor.execute("SELECT senha FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    con.close()

    if resultado:
        senha_hash = resultado[0]
        try:
            ph.verify(senha_hash, senha)
            return True
        except VerifyMismatchError:
            return False
    return False

criar_tabela()
