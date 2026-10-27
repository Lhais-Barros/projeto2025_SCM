import unittest

from chamados import GerenciadorChamados


class TestGerenciadorChamados(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorChamados()

    def test_abrir_chamado(self):
        chamado = self.gerenciador.abrir("Servidor fora do ar", "Ana", "alta")
        self.assertEqual(chamado.id, 1)
        self.assertEqual(chamado.status, "aberto")

    def test_titulo_obrigatorio(self):
        with self.assertRaises(ValueError):
            self.gerenciador.abrir("   ", "Ana")

    def test_alterar_status(self):
        self.gerenciador.abrir("Trocar teclado", "Bruno", "baixa")
        chamado = self.gerenciador.alterar_status(1, "concluido")
        self.assertEqual(chamado.status, "concluido")

    def test_listar_por_status(self):
        self.gerenciador.abrir("Chamado A", "Ana")
        self.gerenciador.abrir("Chamado B", "Bruno")
        self.gerenciador.alterar_status(2, "em andamento")
        self.assertEqual(len(self.gerenciador.listar("aberto")), 1)

    def test_chamado_inexistente(self):
        with self.assertRaises(KeyError):
            self.gerenciador.buscar(99)


if __name__ == "__main__":
    unittest.main()
