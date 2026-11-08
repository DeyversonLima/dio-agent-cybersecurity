"""Login didático com SQLite em memória e dados fictícios."""

import argparse
import sqlite3
from contextlib import closing
from getpass import getpass


def criar_banco():
    banco = sqlite3.connect(":memory:")
    banco.execute("CREATE TABLE usuarios (nome TEXT PRIMARY KEY, senha TEXT)")
    banco.execute("INSERT INTO usuarios VALUES (?, ?)", ("aluna", "senha-lab"))
    return banco


def autenticar(banco, nome, senha):
    consulta = "SELECT 1 FROM usuarios WHERE nome = ? AND senha = ?"
    return banco.execute(consulta, (nome, senha)).fetchone() is not None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    with closing(criar_banco()) as banco:
        acesso = autenticar(banco, input("Usuário: "), getpass("Senha: "))
    print("Acesso autorizado." if acesso else "Acesso negado.")


if __name__ == "__main__":
    main()
