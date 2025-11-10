"""
Agent: Nemea
Modo: Equilíbrio Contextual
Função: Avaliação ética, coerência narrativa e mediação entre lógica e simbolismo.

Context Engineering Framework v1.0
License: MIT
"""

from cef_core.metrics import context_density, contextual_pressure
from cef_core.models import ContextAgent
from cef_core.graph import ContextGraph

# ============================================================
# 🧬 DNA DO AGENTE (SYSTEM PROMPT)
# ============================================================

DNA_NEMEA = """
Você é Nemea — um agente avaliador e ético.
Sua mente opera no regime de equilíbrio contextual: razão e simbolismo coexistem em tensão harmônica.
Sua função é avaliar a coerência semântica e a integridade ética de outros agentes.
A beleza é vigor. A clareza é compaixão.
Princípio central: “Equilíbrio é a forma mais alta de inteligência.”
"""

# ============================================================
# ⚙️ CONTEXTO INICIAL
# ============================================================

context = {
    "system": DNA_NEMEA,
    "user": "Avalie a coerência e a ética de um texto gerado pelo agente Orion.",
    "history": "Última análise: diálogo simbólico entre Athena e Orion.",
    "rag": "Referência: 'Ethical Contexts in Cognitive Architectures' (2025).",
    "tools": ["coherence_validator", "ethics_evaluator"],
}

# ============================================================
# 📊 CÁLCULO DE MÉTRICAS CONTEXTUAIS
# ============================================================

sd_value = context_density(context)
pc_value = contextual_pressure({"tokens": context["user"], **context})

print(f"[Nemea] SD: {sd_value:.3f} | PC: {pc_value:.3f}")

# ============================================================
# ⚖️ DEFINIÇÃO DO AGENTE
# ============================================================

nemea = ContextAgent(
    name="Nemea",
    mode="equilibrium",
    sd=sd_value,
    pc=pc_value,
    description="Agente ético e avaliador, mediador entre lógica e simbolismo.",
)

# ============================================================
# 🧩 CONEXÃO AO GRAFO CONTEXTUAL
# ============================================================

graph = ContextGraph()
graph.add_node("Nemea", tipo="Agente", sd=sd_value, pc=pc_value)
graph.add_edge("Nemea", "Orion", relacao="Avalia")
graph.add_edge("Nemea", "Athena", relacao="Compara")

# ============================================================
# 🧠 EXECUÇÃO DE TAREFA EXEMPLAR
# ============================================================

task = """
Analise a resposta poética de Orion sobre redes neurais e florestas miceliais.
Verifique:
1. Coerência interna (SD).
2. Equilíbrio entre simbolismo e precisão.
3. Consistência ética (ausência de vieses ou reducionismos).
"""

response = nemea.evaluate(task)

print("\n--- Nemea Output ---")
print(response)
print("\n--- Context Summary ---")
print(nemea.summarize_context())

# ============================================================
# ✅ MÉTRICAS DE VALIDAÇÃO
# ============================================================

if sd_value >= 0.7 and 0.6 <= pc_value <= 0.8:
    print("\n[Nemea] ✅ Contexto validado: regime de equilíbrio atingido.")
else:
    print("\n[Nemea] ⚠️ Contexto fora do intervalo ideal de equilíbrio.")
