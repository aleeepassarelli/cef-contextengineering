"""
📏 coherence_tests.py
Validação automática de coerência contextual (SD ≥ 0.7 e PC dentro de regime saudável).

Parte do Context Engineering Framework (CEF)
Autor: Deep Systems Lab
Licença: MIT
"""

from core.context_metrics import calculate_sd, contextual_pressure

# ---------------------------
# ⚙️ Configurações
# ---------------------------

THRESHOLDS = {
    "sd_min": 0.70,
    "pc_min": 0.40,
    "pc_max": 0.90
}


# ---------------------------
# 🧪 Funções de Validação
# ---------------------------

def validate_context(context: dict) -> dict:
    """
    Valida um contexto completo segundo as métricas SD e PC.

    Retorna um relatório com status, métricas e recomendações.
    """
    sd = calculate_sd(context)
    pc = contextual_pressure(context)

    status = []
    if sd < THRESHOLDS["sd_min"]:
        status.append("⚠️ Baixa densidade semântica (SD < 0.7)")
    if pc < THRESHOLDS["pc_min"]:
        status.append("⚠️ Contexto insuficiente (PC < 0.4)")
    elif pc > THRESHOLDS["pc_max"]:
        status.append("⚠️ Contexto saturado (PC > 0.9)")

    if not status:
        status = ["✅ Contexto dentro dos parâmetros ideais."]

    return {
        "SD": round(sd, 3),
        "PC": round(pc, 3),
        "status": status,
        "regime": infer_regime(sd, pc)
    }


def infer_regime(sd: float, pc: float) -> str:
    """
    Determina o regime contextual baseado em SD e PC.
    """
    if sd < THRESHOLDS["sd_min"]:
        return "Contexto degradado"

    if 0.4 <= pc <= 0.7:
        return "Minimalismo (racional)"
    elif 0.7 < pc <= 0.9:
        return "Saturação (criativa)"
    elif 0.6 <= pc <= 0.8:
        return "Equilíbrio (avaliativo)"
    else:
        return "Entropia (instável)"


def print_report(report: dict):
    """
    Exibe o relatório de coerência contextual de forma amigável.
    """
    print("=== Coherence Test Report ===")
    print(f"🧩 Densidade Semântica (SD): {report['SD']}")
    print(f"🌡️ Pressão Contextual (PC): {report['PC']}")
    print(f"⚙️ Regime: {report['regime']}")
    print("📋 Status:")
    for s in report["status"]:
        print(f"  - {s}")


# ---------------------------
# 🚀 Execução direta
# ---------------------------

if __name__ == "__main__":
    # Exemplo de teste rápido
    context_example = {
        "system": "Você é um analista lógico especializado em arquitetura de agentes.",
        "user": "Analise o impacto da densidade semântica na coerência cognitiva.",
        "history": "Usuário e modelo discutiram SD e PC em interações anteriores.",
        "rag": "Artigos sobre context engineering e cognitive coherence.",
        "tools": "search_web(), summarize_docs()"
    }

    report = validate_context(context_example)
    print_report(report)
