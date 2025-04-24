"""
Testes da classe Aluno.
"""
import unittest
from aluno import Aluno


class TestAluno(unittest.TestCase):
    def setUp(self):
        self.aluno = Aluno(nome="Ana", matricula="A01")

    def test_adicionar_nota_e_media(self):
        self.aluno.adicionar_nota("Matemática", 8.0)
        self.aluno.adicionar_nota("Matemática", 6.0)
        self.assertEqual(self.aluno.calcular_media("Matemática"), 7.0)

    def test_verificar_aprovacao(self):
        self.aluno.adicionar_nota("História", 5.0)
        self.assertFalse(self.aluno.verificar_aprovacao("História"))
        self.aluno.adicionar_nota("História", 7.0)
        self.assertTrue(self.aluno.verificar_aprovacao("História"))

    def test_registrar_falta_e_frequencia(self):
        self.aluno.registrar_falta("Português")
        self.aluno.registrar_falta("Português")
        freq = self.aluno.calcular_frequencia("Português", 10)
        self.assertEqual(freq, 80.0)


if __name__ == "__main__":
    unittest.main()
