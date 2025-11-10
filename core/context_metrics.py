"""
core/context_metrics.py
────────────────────────────────────────────
Módulo de métricas fundamentais do Context Engineering Framework (CEF).

Fornece funções para medir:
- Densidade Semântica (SD)
- Pressão Contextual (PC)
- Entropia Semântica (S_H)
- Coerência Lexical (μ)
────────────────────────────────────────────
Autor: Context Engineering Lab
Licença: MIT
Versão: 1.0.0
"""

import math
import re
from collections import Counter
from typing import Dict, List


# ============================================================
# 🔹 FUNÇÃO: calcular densidade semântica (SD)
# ============================================================

def calculate_sd(text: str) -> float:
    """
    Calcula a Densidade Semântica (SD) de um texto.
    
    SD = (vocabulário único / total de tokens) * fator de coerência
    
    Onde:
      - Fator de coerência ≈ proporção de termos significativos
      - SD varia entre 0.0 e 1.0
    """
    if not text or not isinstance(text, str):
        return 0.0

    tokens = re.findall(r"\b\w+\b", text.lower())
    if len(tokens) == 0:
        return 0.0

    unique = set(tokens)
    ratio = len(unique) / len(tokens)

    # Ponderação: reduz impacto de textos muito curtos
    coherence_factor = 1 - math.exp(-len(tokens) / 50)
    sd = min(1.0, ratio * coherence_factor)

    return round(sd, 4)


# ============================================================
# 🔹 FUNÇÃO: calcular entropia semântica (S_H)
# ============================================================

def semantic_entropy(text: str) -> float:
    """
    Mede a entropia semântica (S_H), ou dispersão lexical do texto.
    
    Base: Shannon Entropy aplicada ao vocabulário.
    """
    tokens = re.findall(r"\b\w+\b", text.lower())
    if len(tokens) <= 1:
        return 0.0

    counts = Counter(tokens)
    total = sum(counts.values())

    entropy = -sum((c / total) * math.log2(c / total) for c in counts.values())
    normalized = entropy / math.log2(len(tokens))
    return round(normalized, 4)


# ============================================================
# 🔹 FUNÇÃO: coerência lexical (μ)
# ============================================================

def lexical_coherence(text: str) -> float:
    """
    Mede a coerência lexical (μ) — regularidade semântica e repetição útil.
    μ = 1 - S_H (com ajuste para densidade)
    """
    sd = calculate_sd(text)
    sh = semantic_entropy(text)
    mu = (1 - sh) * sd
    return round(mu, 4)


# ============================================================
# 🔹 FUNÇÃO: densidade de contexto (CD)
# ============================================================

def context_density(components: Dict[str, str]) -> float:
    """
    Calcula a densidade média ponderada do contexto total.
    
    Pesos padrão:
      system: 0.30
      user: 0.25
      history: 0.15
      rag: 0.20
      tools: 0.10
    """
    weights = {
        "system": 0.30,
        "user": 0.25,
        "history": 0.15,
        "rag": 0.20,
        "tools": 0.10,
    }

    total = 0.0
    for k, w in weights.items():
        if k in components:
            total += calculate_sd(components[k]) * w

    return round(total, 4)


# ============================================================
# 🔹 FUNÇÃO: pressão contextual (PC)
# ============================================================

def contextual_pressure(context: Dict[str, any]) -> float:
    """
    Mede a Pressão Contextual (PC), que expressa a saturação semântica.
    
    PC = CD * (len(tokens) / 10_000)
    
    Classificação:
      0.0–0.4 → raso (incompleto)
      0.4–0.7 → racional (minimalismo)
      0.7–0.9 → criativo (saturação)
      >0.9   → entrópico (alucinação)
    """
    tokens = []
    for v in context.values():
        if isinstance(v, str):
            tokens += re.findall(r"\b\w+\b", v.lower())

    total_tokens = len(tokens)
    cd = context_density(context)

    if total_tokens == 0:
        return 0.0

    pc = cd * (total_tokens / 10_000)
    return round(min(pc, 1.0), 4)


# ============================================================
# 🔹 FUNÇÃO: regime contextual
# ============================================================

def classify_context_regime(sd: float, pc: float) -> str:
    """
    Classifica o regime de operação contextual com base em SD e PC.
    """
    if sd < 0.7:
        return "Incompleto"
    if pc < 0.4:
        return "Raso"
    if 0.4 <= pc < 0.7:
        return "Minimalismo"
    if 0.7 <= pc < 0.9:
        return "Saturação"
    if 0.6 <= pc <= 0.8 and 0.7 <= sd <= 0.85:
        return "Equilíbrio"
    return "Entrópico"


# ============================================================
# 🔹 TESTE RÁPIDO
# ============================================================

if __name__ == "__main__":
    sample = {
        "system": "Agente analítico especializado em síntese cognitiva e compressão semântica.",
        "user": "Explique a diferença entre contexto simbólico e contexto lógico.",
        "history": "Última sessão abordou modelos de coerência e entropia linguística.",
        "rag": "Fonte: 'Poetics of Systems', 2024.",
        "tools": "semantic_search, code_runner"
    }

    sd = context_density(sample)
    pc = contextual_pressure(sample)
    regime = classify_context_regime(sd, pc)

    print(f"SD = {sd} | PC = {pc} → Regime: {regime}")
