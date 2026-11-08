"""Reprodução intencional da falha. Execute somente no laboratório local."""


def autenticar(banco, nome, senha):
    consulta = f"SELECT 1 FROM usuarios WHERE nome = '{nome}' AND senha = '{senha}'"
    return banco.execute(consulta).fetchone() is not None
