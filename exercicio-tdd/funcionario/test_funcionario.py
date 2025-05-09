"""
Testes da classe Funcionario.
"""
import unittest
from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    def setUp(self):
        self.func = Funcionario(
            nome="João",
            matricula=123,
            salario_hora=50,
            horas_trabalhadas=160,
            custo_empregador=800,
            tem_comissao=True,
            valor_comissao=200,
            contratos_fechados=5
        )

    def test_calcular_salario_bruto(self):
        self.assertEqual(self.func.calcular_salario_bruto(), 8000)

    def test_calcular_custo_total(self):
        self.assertEqual(self.func.calcular_custo_total(), 8800)

    def test_calcular_comissao(self):
        self.assertEqual(self.func.calcular_comissao(), 1000)
        self.func.tem_comissao = False
        self.assertEqual(self.func.calcular_comissao(), 0)

    def test_inicializacao_total(self):
        f = Funcionario(
            nome="Maria",
            matricula=456,
            salario_hora=60,
            horas_trabalhadas=150,
            custo_empregador=500,
            tem_comissao=False,
            valor_comissao=100,
            contratos_fechados=2
        )
        self.assertEqual(f.nome, "Maria")
