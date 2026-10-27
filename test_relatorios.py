import unittest

from chamados import GerenciadorChamados
from relatorios import formatar_relatorio, pendentes_alta_prioridade, resumo


class TestRelatorios(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorChamados()
        self.gerenciador.abrir("Servidor fora do ar", "Ana", "alta")
        self.gerenciador.abrir("Rede lenta", "Bruno", "alta")
        self.gerenciador.abrir("Trocar mouse", "Carla", "baixa")
        self.gerenciador.alterar_status(2, "concluido")

    def test_resumo(self):
        dados = resumo(self.gerenciador)
        self.assertEqual(dados["total"], 3)
        self.assertEqual(dados["por_status"]["aberto"], 2)
        self.assertEqual(dados["por_status"]["concluido"], 1)
        self.assertEqual(dados["por_prioridade"]["alta"], 2)

    def test_pendentes_alta_prioridade(self):
        urgentes = pendentes_alta_prioridade(self.gerenciador)
        self.assertEqual([c.id for c in urgentes], [1])

    def test_formatar_relatorio(self):
        texto = formatar_relatorio(self.gerenciador)
        self.assertIn("Total de chamados: 3", texto)
        self.assertIn("Servidor fora do ar", texto)


if __name__ == "__main__":
    unittest.main()
