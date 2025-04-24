"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta
from produto import Produto


class TestProduto(unittest.TestCase):
    def setUp(self):
        self.produto = Produto(
            codigo="001",
            nome="Arroz",
            preco=5.0,
            quantidade=20,
            data_validade=datetime.now() + timedelta(days=30),
            estoque_minimo=10
        )

    def test_inicializacao(self):
        self.assertEqual(self.produto.codigo, "001")
        self.assertEqual(self.produto.nome, "Arroz")
        self.assertEqual(self.produto.preco, 5.0)
        self.assertEqual(self.produto.quantidade, 20)
        self.assertGreater(self.produto.data_validade, datetime.now())
        self.assertEqual(self.produto.estoque_minimo, 10)

    def test_adicionar_estoque(self):
        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.quantidade, 30)

        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-5)

    def test_remover_estoque(self):
        sucesso = self.produto.remover_estoque(5)
        self.assertTrue(sucesso)
        self.assertEqual(self.produto.quantidade, 15)

        sucesso = self.produto.remover_estoque(50)
        self.assertFalse(sucesso)

        with self.assertRaises(ValueError):
            self.produto.remover_estoque(-1)

    def test_verificar_estoque_baixo(self):
        self.assertFalse(self.produto.verificar_estoque_baixo())
        self.produto.quantidade = 5
        self.assertTrue(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        self.assertEqual(self.produto.calcular_valor_total(), 100.0)

    def test_verificar_validade(self):
        self.assertTrue(self.produto.verificar_validade())
        self.produto.data_validade = datetime.now() - timedelta(days=1)
        self.assertFalse(self.produto.verificar_validade())
        self.produto.data_validade = None
        self.assertTrue(self.produto.verificar_validade())


if __name__ == "__main__":
    unittest.main()
