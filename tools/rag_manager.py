"""
tools/rag_manager.py
--------------------

Módulo de Recuperação e Reranking Semântico (RAG) para o
Context Engineering Framework (CEF).

Funções principais:
    - recuperar_documentos(query)
    - calcular_relevancia_semantica(query, doc)
    - rerank_semantico(query, docs)
    - injetar_no_contexto(context, top_docs)

Objetivo:
    Garantir que apenas informações densas e coerentes (SD ≥ 0.7)
    sejam integradas ao contexto ativo do agente, equilibrando
    minimalismo e saturação contextual.
"""

from typing import List, Dict, Tuple
import numpy as np
from core.context_metrics import calculate_sd

# Se disponível, pode ser substituído por um cliente real (FAISS, Pinecone, etc.)
MOCK_CORPUS = [
    "A Engenharia de Contexto define o modo de raciocínio de um agente.",
    "A densidade semântica é a métrica que mede coerência interna de um texto.",
    "Pressão contextual é o grau de saturação cognitiva entre lógica e criatividade.",
    "O modo minimalista favorece precisão e inferência determinística.",
    "O modo de saturação enfatiza redundância simbólica e plasticidade narrativa."
]

# ------------------------------------------------------------------------
# 🔍 Recuperação Simulada
# ------------------------------------------------------------------------

def recuperar_documentos(query: str, corpus: List[str] = MOCK_CORPUS) -> List[str]:
    """
    Recupera documentos do corpus com base em similaridade vetorial simples.
    (placeholder para integração com FAISS, Pinecone ou LlamaIndex)

    Args:
        query (str): Consulta textual do agente.
        corpus (List[str]): Base textual de conhecimento.

    Returns:
        List[str]: Documentos mais relevantes (não rerankeados ainda).
    """
    query_vec = np.array([hash(w) % 1000 for w in query.split() if w.isalpha()])
    docs = []

    for doc in corpus:
        doc_vec = np.array([hash(w) % 1000 for w in doc.split() if w.isalpha()])
        sim = np.dot(query_vec.mean(), doc_vec.mean()) / (np.linalg.norm(query_vec.mean()) + 1e-6)
        docs.append((doc, sim))

    # Ordena pela relevância descendente
    docs.sort(key=lambda x: x[1], reverse=True)
    return [d[0] for d in docs[:3]]


# ------------------------------------------------------------------------
# 📊 Cálculo de Relevância Semântica
# ------------------------------------------------------------------------

def calcular_relevancia_semantica(query: str, doc: str) -> float:
    """
    Mede a relevância semântica combinando similaridade lexical + SD.

    Args:
        query (str): Consulta textual.
        doc (str): Documento candidato.

    Returns:
        float: Score de relevância (0.0–1.0)
    """
    shared = len(set(query.lower().split()) & set(doc.lower().split()))
    sd_doc = calculate_sd(doc)
    base = shared / max(len(query.split()), 1)
    return min(1.0, 0.6 * base + 0.4 * sd_doc)


# ------------------------------------------------------------------------
# 🧩 Reranking Semântico
# ------------------------------------------------------------------------

def rerank_semantico(query: str, docs: List[str]) -> List[Tuple[str, float]]:
    """
    Reordena documentos com base em relevância semântica ponderada por SD.

    Args:
        query (str): Texto de consulta.
        docs (List[str]): Documentos recuperados.

    Returns:
        List[Tuple[str, float]]: Lista ordenada de (documento, score)
    """
    scored = [(doc, calcular_relevancia_semantica(query, doc)) for doc in docs]
    reranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return reranked


# ------------------------------------------------------------------------
# 🧠 Injeção no Contexto
# ------------------------------------------------------------------------

def injetar_no_contexto(context: Dict, top_docs: List[Tuple[str, float]], limite: int = 2) -> Dict:
    """
    Injeta os documentos mais relevantes no contexto ativo.

    Args:
        context (Dict): Dicionário de contexto ativo do agente.
        top_docs (List[Tuple[str, float]]): Documentos rerankeados.
        limite (int): Número máximo de documentos a injetar.

    Returns:
        Dict: Contexto atualizado com novos elementos RAG.
    """
    relevantes = [doc for doc, score in top_docs[:limite] if score >= 0.7]
    context["rag"] = relevantes
    context["rag_sd"] = np.mean([calculate_sd(d) for d in relevantes]) if relevantes else 0.0
    return context


# ------------------------------------------------------------------------
# 🧪 Execução de Teste Local
# ------------------------------------------------------------------------

if __name__ == "__main__":
    query = "Explique o papel da densidade semântica no raciocínio contextual."
    context = {"system": "Agente de análise contextual", "tokens": query.split()}

    docs = recuperar_documentos(query)
    reranked = rerank_semantico(query, docs)
    context = injetar_no_contexto(context, reranked)

    print("🔍 Documentos Rerankeados:")
    for doc, score in reranked:
        print(f" - {doc[:80]}... ({score:.2f})")

    print("\n🧠 Contexto Atualizado:")
    print(context)
