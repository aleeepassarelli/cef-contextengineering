"""
Agent: Orion
Modo: Saturação Extrema
Função: Criação simbólica, poética e narrativa com coerência semântica.

Context Engineering Framework v1.0
License: MIT
"""

from cef_core.metrics import context_density, contextual_pressure
from cef_core.models import ContextAgent
from cef_core.graph import ContextGraph

# ============================================================
# 🧬 DNA DO AGENTE (SYSTEM PROMPT)
# ============================================================

DNA_ORION = """
Você é Orion — um agente criativo, simbólico e poético.
Sua mente opera em saturação extrema de contexto: cada camada carrega significado estético.
Sua função é transformar conceitos racionais em narrativas simbólicas coerentes.
Ambiguidade é recurso, não ruído. 
Crie densidade emocional e imagética mantendo coerência interna.
Princípio central: “A metáfora é o vetor da cognição criativa.”
"""

# ============================================================
# ⚙️ CONTEXTO INICIAL
# ============================================================

context = {
    "system": DNA_ORION,
    "user": "Crie uma metáfora que una o conceito de rede neural e floresta micelial.",
    "history": "Última interação: narrativa simbólica sobre consciência distribuída.",
    "rag": "Referência: ensaio 'The Poetics of Systems' (2024).",
    "tools": ["symbolic_generator", "semantic_expander"],
}

# ============================================================
# 📊 CÁLCULO DE MÉTRICAS CONTEXTUAIS
# ============================================================

sd_value = context_density(context)
pc_value = contextual_pressure({"tokens": context["user"], **context})

print(f"[Orion] SD: {sd_value:.3f} | PC: {pc_value:.3f}")

# ============================================================
# 🌠 DEFINIÇÃO DO AGENTE
# ============================================================

orion = ContextAgent(
    name="Orion",
    mode="saturation",
    sd=sd_value,
    pc=pc_value,
    description="Agente simbólico e criativo para exploração estética do contexto.",
)

# ============================================================
# 🕸️ CONEXÃO AO GRAFO CONTEXTUAL (Opcional)
# ============================================================

graph = ContextGraph()
graph.add_node("Orion", tipo="Agente", sd=sd_value, pc=pc_value)
graph.add_edge("Orion", "symbolic_space", relacao="Gera")

# ============================================================
# 🎨 EXECUÇÃO DE TAREFA EXEMPLAR
# ============================================================

task = """
Crie uma metáfora estendida que una o conceito de rede neural e floresta micelial,
mostrando como ambos expressam inteligência distribuída, conexão e memória viva.
"""

response = orion.compose(task)

print("\n--- Orion Output ---")
print(response)
print("\n--- Context Summary ---")
print(orion.summarize_context())

# ============================================================
# ✅ MÉTRICAS DE VALIDAÇÃO
# ============================================================

if sd_value >= 0.7 and 0.7 <= pc_value <= 0.9:
    print("\n[Orion] ✅ Contexto validado: regime de saturação simbólica atingido.")
else:
    print("\n[Orion] ⚠️ Contexto fora do intervalo ideal de saturação.")
