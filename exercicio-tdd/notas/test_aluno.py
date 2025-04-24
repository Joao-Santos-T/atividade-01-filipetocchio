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

    def test_inicializacao_com_none(self):
        aluno = Aluno(nome="Carlos", matricula="C02", notas=None, faltas=None)
        self.assertEqual(aluno.notas, {})
        self.assertEqual(aluno.faltas, {})

    def test_media_sem_notas(self):
        self.assertEqual(self.aluno.calcular_media("Inglês"), 0.0)

    def test_frequencia_sem_faltas(self):
        freq = self.aluno.calcular_frequencia("Química", 20)
        self.assertEqual(freq, 100.0)
