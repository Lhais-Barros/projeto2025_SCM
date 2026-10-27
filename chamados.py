"""Regras de negócio do Sistema de Chamados do time de Operações."""

from dataclasses import dataclass, field
from datetime import datetime

STATUS_VALIDOS = ("aberto", "em andamento", "concluido")
PRIORIDADES_VALIDAS = ("baixa", "media", "alta")


@dataclass
class Chamado:
    id: int
    titulo: str
    solicitante: str
    prioridade: str = "media"
    status: str = "aberto"
    criado_em: datetime = field(default_factory=datetime.now)

    def __str__(self):
        return (
            f"#{self.id} [{self.status}] ({self.prioridade}) "
            f"{self.titulo} - {self.solicitante}"
        )


class GerenciadorChamados:
    """Guarda os chamados em memória e controla o ciclo de vida de cada um."""

    def __init__(self):
        self._chamados = {}
        self._proximo_id = 1

    def abrir(self, titulo, solicitante, prioridade="media"):
        if not titulo.strip():
            raise ValueError("O título do chamado é obrigatório.")
        if prioridade not in PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridade inválida: {prioridade}")

        chamado = Chamado(self._proximo_id, titulo.strip(), solicitante.strip(), prioridade)
        self._chamados[chamado.id] = chamado
        self._proximo_id += 1
        return chamado

    def buscar(self, id_chamado):
        if id_chamado not in self._chamados:
            raise KeyError(f"Chamado #{id_chamado} não encontrado.")
        return self._chamados[id_chamado]

    def alterar_status(self, id_chamado, novo_status):
        if novo_status not in STATUS_VALIDOS:
            raise ValueError(f"Status inválido: {novo_status}")
        chamado = self.buscar(id_chamado)
        chamado.status = novo_status
        return chamado

    def listar(self, status=None):
        chamados = list(self._chamados.values())
        if status:
            chamados = [c for c in chamados if c.status == status]
        return chamados
