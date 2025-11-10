"""
Agent: Athena
Modo: Minimalismo Extremo
Função: Análise e estratégia racional com alta coerência e economia contextual.

Context Engineering Framework v1.0
License: MIT
"""

from cef_core.metrics import context_density, contextual_pressure
from cef_core.models import ContextAgent
from cef_core.graph import ContextGraph

# ============================================================
# 🧩 DEFINIÇÃO DO DNA DO AGENTE (SYSTEM PROMPT)
# ============================================================

DNA_ATHENA = """
Você é Athena — um agente racional, analítico e de raciocínio minimalista.
Sua missão é manter a coerência e a precisão inferencial em todos os contextos.
Evite redundância e prolixidade. Cada token deve carregar significado.
Princípio central: 'Densidade > Extensão.'
"""

# ============================================================
# ⚙️ CONTEXTO INICIAL
# ============================================================

context = {
    "system": DNA_ATHENA,
    "user": "Analise o impacto da densidade semântica em modelos de IA generativa.",
    "history": "Última tarefa: síntese de métricas SD e PC.",
    "rag": "Paper: 'Semantic Compression in Large Language Models' (2024)",
    "tools": "Nenhuma ferramenta ativa neste modo."
}

# ============================================================
# 📊 CÁLCULO DE MÉTRICAS CONTEXTUAIS
# ============================================================

sd_value = context_density(context)
pc_value = contextual_pressure({"tokens": context["user"], **context})

print(f"[Athena] SD: {sd_value:.3f} | PC: {pc_value:.3f}")

# ============================================================
# 🧠 DEFINIÇÃO DO AGENTE
# ============================================================

athena = ContextAgent(
    name="Athena",
    mode="minimal",
    sd=sd_value,
    pc=pc_value,
    description="Agente racional para análise sintética de informação.",
)

# ============================================================
# 🕸️ CONEXÃO AO GRAFO CONTEXTUAL (Opcional)
# ============================================================

graph = ContextGraph()
graph.add_node("Athena", tipo="Agente", sd=sd_value, pc=pc_value)
graph.add_edge("Athena", "context_density", relacao="ANALISA")

# ============================================================
# 🔍 EXECUÇÃO DE TAREFA EXEMPLAR
# ============================================================

task = """
Avalie como a densidade semântica influencia a capacidade de raciocínio
e a redução de entropia em contextos de IA generativa.
"""

response = athena.analyze(task)

print("\n--- Athena Output ---")
print(response)
print("\n--- Context Summary ---")
print(athena.summarize_context())

# ============================================================
# ✅ MÉTRICAS DE VALIDAÇÃO
# ============================================================

if sd_value >= 0.7 and 0.4 <= pc_value <= 0.7:
    print("\n[Athena] ✅ Contexto validado: regime de minimalismo racional atingido.")
else:
    print("\n[Athena] ⚠️ Contexto fora do intervalo ideal de minimalismo.")
