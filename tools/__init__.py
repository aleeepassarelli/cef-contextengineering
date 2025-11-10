"""
tools/__init__.py
-----------------

Pacote: tools
Parte integrante do Context Engineering Framework (CEF)

Descrição:
    Este pacote contém utilitários semânticos e funcionais que ampliam
    as capacidades cognitivas dos agentes de IA — atuando como “órgãos”
    do sistema contextual.

Módulos:
    rag_manager      – Recuperação e reranking semântico (RAG)
    compression      – Compressão e sumarização semântica
    context_optimizer – (opcional) Regulação dinâmica de SD/PC
    memory_neo4j     – Persistência e continuidade identitária
"""

from .rag_manager import *
from .compression import *

__all__ = [
    "rag_manager",
    "compression"
]
