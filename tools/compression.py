"""
tools/compression.py
----------------------

Módulo de Compressão Semântica para o Context Engineering Framework (CEF).

Objetivo:
    Reduzir o tamanho do contexto (prompt, histórico, RAG)
    mantendo coerência e densidade semântica acima de SD ≥ 0.70.

Conceito:
    Compressão semântica ≠ sumarização textual.
    Aqui, buscamos manter o "núcleo informacional" (vetor semântico)
    mesmo com perda lexical.

Requisitos:
    pip install sentence-transformers numpy scikit-learn
"""

from typing import List, Dict, Tuple
from sentence_transformers import SentenceTransformer, util
import numpy as np
from core.context_metrics import calculate_sd

# ------------------------------------------------------------------------
# ⚙️ Modelo de Embeddings
# ------------------------------------------------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

# ------------------------------------------------------------------------
# 🧠 Funções Principais
# ------------------------------------------------------------------------

def semantic_compression(chunks: List[str], compression_rate: float = 0.5) -> List[str]:
    """
    Realiza compressão semântica por similaridade vetorial.

    Args:
        chunks (List[str]): Lista de segmentos de texto.
        compression_rate (float): Percentual de conteúdo a manter (0–1).

    Returns:
        List[str]: Subconjunto semanticamente representativo.
    """
    if not chunks:
        return []

    embeddings = model.encode(chunks, convert_to_tensor=True)
    centroid = embeddings.mean(dim=0)
    similarities = util.cos_sim(embeddings, centroid).cpu().numpy().flatten()

    # Seleciona top-k mais próximos do centro semântico
    k = max(1, int(len(chunks) * compression_rate))
    top_indices = similarities.argsort()[-k:][::-1]

    return [chunks[i] for i in top_indices]


def compress_context(context: Dict[str, any], keep_ratio: float = 0.6) -> Dict[str, any]:
    """
    Aplica compressão semântica seletiva em um contexto completo.

    Args:
        context (Dict): Estrutura contextual (system, user, history, rag)
        keep_ratio (float): Fator de retenção média do contexto.

    Returns:
        Dict[str, any]: Novo contexto comprimido.
    """
    compressed = {}

    # Campos diretos (não comprimidos)
    compressed["system"] = context.get("system", "")
    compressed["user"] = context.get("user", "")

    # Compressão seletiva
    if "history" in context:
        compressed["history"] = semantic_compression(context["history"], keep_ratio)

    if "rag" in context:
        compressed["rag"] = semantic_compression(context["rag"], keep_ratio)

    compressed["tools"] = context.get("tools", [])
    compressed["tokens"] = sum(len(x.split()) for x in compressed.get("history", [])) + \
                           sum(len(x.split()) for x in compressed.get("rag", []))

    compressed["sd"] = calculate_sd(str(compressed))
    return compressed


def summarize_context(context: Dict[str, any], max_tokens: int = 500) -> str:
    """
    Gera uma versão resumida e compacta do contexto, semântico e factual.

    Args:
        context (Dict): Estrutura contextual.
        max_tokens (int): Limite de tokens aproximado.

    Returns:
        str: Texto condensado.
    """
    core = []

    if "system" in context:
        core.append(f"System: {context['system']}")
    if "user" in context:
        core.append(f"User: {context['user']}")
    if "history" in context:
        core.append("History Summary:")
        core.extend(context["history"][:3])
    if "rag" in context:
        core.append("RAG Highlights:")
        core.extend(context["rag"][:3])

    text = "\n".join(core)
    words = text.split()

    if len(words) > max_tokens:
        text = " ".join(words[:max_tokens]) + "..."

    return text


# ------------------------------------------------------------------------
# 🧪 Teste Local
# ------------------------------------------------------------------------

if __name__ == "__main__":
    sample_context = {
        "system": "Agente de síntese semântica.",
        "user": "Resuma a arquitetura do framework de contexto.",
        "history": [
            "O framework define sete níveis de inferência.",
            "A densidade semântica mede a concentração de sentido.",
            "A pressão contextual controla a entropia cognitiva.",
            "Memória persistente usa Neo4j e embeddings.",
            "O agente deve manter SD > 0.75 para confiabilidade."
        ],
        "rag": [
            "Contexto é o metabolismo cognitivo, não a informação.",
            "A compressão semântica retém coerência estrutural.",
            "A arquitetura possui camadas dinâmicas e simbólicas."
        ]
    }

    print("💡 Compressão semântica — teste local")
    compressed = compress_context(sample_context, keep_ratio=0.5)
    print("Tokens antes:", sum(len(x.split()) for x in sample_context["history"]))
    print("Tokens depois:", sum(len(x.split()) for x in compressed["history"]))
    print("SD calculado:", compressed["sd"])

    print("\n🧱 Resumo gerado:")
    print(summarize_context(compressed))
