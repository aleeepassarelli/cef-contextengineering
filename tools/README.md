# 🧠 Tools — Módulos Funcionais do Context Engineering Framework

## 📘 Visão Geral

A pasta **`tools/`** contém os módulos responsáveis por **operar o metabolismo cognitivo** do agente — isto é, os processos que permitem ao sistema contextual acessar, comprimir, recuperar e otimizar conhecimento.

Essas ferramentas são os **órgãos funcionais** do agente: cada uma estende uma dimensão cognitiva da arquitetura micelial.

---

## 🧩 Estrutura dos Módulos

| Módulo | Função | Papel no Framework |
|--------|--------|--------------------|
| `rag_manager.py` | Recuperação de conhecimento externo e reranking semântico (RAG). | Amplia o contexto com conhecimento relevante, mantendo alta Densidade Semântica (SD). |
| `compression.py` | Compressão semântica e síntese de contexto. | Reduz redundância textual mantendo coerência e alta densidade. |
| `memory_neo4j.py` | Persistência simbólica e continuidade identitária. | Conecta agentes e memórias no grafo semântico (Neo4j). |
| `context_optimizer.py` *(opcional)* | Ajuste dinâmico de SD e PC durante a execução. | Mantém equilíbrio entre minimalismo e saturação. |
| `__init__.py` | Registro de exportações e namespace unificado. | Permite importação direta dos utilitários (`from tools import rag_manager`). |

---

## ⚙️ Exemplo de Uso

```python
from tools import rag_manager, compression
from core.context_metrics import calculate_sd, contextual_pressure

# Recupera documentos relevantes (RAG)
context = rag_manager.retrieve(query="sistemas de IA simbólicos")

# Calcula densidade e pressão do contexto
sd = calculate_sd(context)
pc = contextual_pressure(context)

# Aplica compressão se houver entropia contextual
if pc > 0.9:
    context = compression.semantic_compress(context)
````

---

## 🧭 Integração com o Framework

Essas ferramentas são utilizadas pelos **agentes cognitivos (Athena, Orion, Nemea)** para ajustar o metabolismo semântico conforme o modo de operação:

| Modo                     | Estratégia de Uso                               | Ferramentas Ativas                 |
| ------------------------ | ----------------------------------------------- | ---------------------------------- |
| **Minimalismo (Athena)** | Contexto enxuto, precisão inferencial.          | `compression`, `memory_neo4j`      |
| **Saturação (Orion)**    | Contexto simbólico e redundante, foco criativo. | `rag_manager`, `context_optimizer` |
| **Equilíbrio (Nemea)**   | Avaliação ética e coerência narrativa.          | Todos os módulos                   |

---

## 🔬 Foco de Desenvolvimento Futuro

* [ ] Integração com **LangGraph** para controle adaptativo de SD/PC.
* [ ] Camada de observabilidade via **Langfuse**.
* [ ] Aprendizado autônomo de pesos semânticos no RAG.
* [ ] Monitor de entropia simbólica.

---

> *“As ferramentas são órgãos: cada função técnica é também uma função cognitiva.”*
> — *Manifesto da Engenharia de Contexto, 2025*

```
