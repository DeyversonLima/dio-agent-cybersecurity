import unittest
from contextlib import closing

from app import autenticar, criar_banco
from vulneravel import autenticar as autenticar_vulneravel


class TesteLogin(unittest.TestCase):
    def test_credenciais_validas(self):
        with closing(criar_banco()) as banco:
            self.assertTrue(autenticar(banco, "aluna", "senha-lab"))

    def test_senha_invalida(self):
        with closing(criar_banco()) as banco:
            self.assertFalse(autenticar(banco, "aluna", "errada"))

    def test_reproducao_e_mitigacao_da_injecao(self):
        with closing(criar_banco()) as banco:
            entrada = "aluna' -- "
            self.assertTrue(autenticar_vulneravel(banco, entrada, "errada"))
            self.assertFalse(autenticar(banco, entrada, "errada"))


if __name__ == "__main__":
    unittest.main()
