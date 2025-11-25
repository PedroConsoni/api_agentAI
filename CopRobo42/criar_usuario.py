import sqlite3
from argon2 import PasswordHasher

ph = PasswordHasher()

def criar_usuario(usuario, senha):
    con = sqlite3.connect("usuarios.db")
    cursor = con.cursor()

    senha_hash = ph.hash(senha)

    cursor.execute("""
        INSERT OR REPLACE INTO usuarios (usuario, senha)
        VALUES (?, ?)
    """, (usuario, senha_hash))

    con.commit()
    con.close()

    print("Usuário cadastrado!")

criar_usuario("Maria Eduarda", "CopRobo42")
