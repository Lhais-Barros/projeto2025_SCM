# projeto2025_SCM – Sistema de Chamados

Projeto da aula prática **Gerenciamento de Configuração** (Projeto de Software – U4/A1).

Sistema simples, em Python, para o time de Operações abrir e acompanhar chamados
(solicitações). O repositório no GitHub é o local único onde ficam as versões
atualizadas de todos os artefatos do projeto.

## Artefatos

| Arquivo | Descrição |
|---|---|
| `chamados.py` | Regras de negócio: abrir, buscar, listar e alterar status de chamados |
| `main.py` | Menu de terminal para usar o sistema |
| `relatorios.py` | Relatório-resumo por status e prioridade, com os chamados urgentes pendentes |
| `test_chamados.py` | Testes automatizados (unittest) |
| `test_relatorios.py` | Testes do relatório |

## Histórico de mudanças

- **v1.0** – Cadastro, listagem e alteração de status de chamados.
- **v1.1** – Nova funcionalidade: relatório-resumo (opção 4 do menu), solicitada pela gestão de Operações.

## Como executar

Requer Python 3.8 ou superior, sem bibliotecas externas.

```bash
python main.py
```

## Como testar

```bash
python -m unittest -v
```

## Fluxo de trabalho com Git

```bash
git clone https://github.com/Lhais-Barros/projeto2025_SCM.git
git status
git add .
git commit -m "mensagem descrevendo a alteração"
git push
```
