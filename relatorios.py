"""Nova funcionalidade: relatório-resumo dos chamados para a gestão de Operações."""

from collections import Counter

from chamados import PRIORIDADES_VALIDAS, STATUS_VALIDOS


def resumo(gerenciador):
    """Conta os chamados por status e por prioridade."""
    chamados = gerenciador.listar()
    por_status = Counter(c.status for c in chamados)
    por_prioridade = Counter(c.prioridade for c in chamados)
    return {
        "total": len(chamados),
        "por_status": {s: por_status.get(s, 0) for s in STATUS_VALIDOS},
        "por_prioridade": {p: por_prioridade.get(p, 0) for p in PRIORIDADES_VALIDAS},
    }


def pendentes_alta_prioridade(gerenciador):
    """Chamados de prioridade alta que ainda não foram concluídos."""
    return [
        c for c in gerenciador.listar()
        if c.prioridade == "alta" and c.status != "concluido"
    ]


def formatar_relatorio(gerenciador):
    dados = resumo(gerenciador)
    linhas = [f"Total de chamados: {dados['total']}", "", "Por status:"]
    linhas += [f"  {status}: {qtd}" for status, qtd in dados["por_status"].items()]
    linhas += ["", "Por prioridade:"]
    linhas += [f"  {prioridade}: {qtd}" for prioridade, qtd in dados["por_prioridade"].items()]

    urgentes = pendentes_alta_prioridade(gerenciador)
    linhas += ["", f"Pendentes de prioridade alta: {len(urgentes)}"]
    linhas += [f"  {c}" for c in urgentes]
    return "\n".join(linhas)
