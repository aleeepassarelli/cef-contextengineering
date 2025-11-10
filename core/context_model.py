"""
core/context_model.py
────────────────────────────────────────────
Estruturas e classes-base do Context Engineering Framework (CEF).

Define:
- ContextComponent: unidade semântica de contexto
- ContextState: estado cognitivo completo do agente
- ContextAgent: agente contextualizado com modos e métricas

Integra funções do módulo context_metrics.py.
────────────────────────────────────────────
Autor: Context Engineering Lab
Licença: MIT
Versão: 1.0.0
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any
import datetime
import uuid

from core.context_metrics import (
    calculate_sd,
    context_density,
    contextual_pressure,
    classify_context_regime,
)


# ============================================================
# 🔹 CONTEXT COMPONENT
# ============================================================

@dataclass
class ContextComponent:
    """Unidade de contexto (system, user, history, rag, tools)."""
    name: str
    content: str
    timestamp: str = field(default_factory=lambda: datetime.datetime.utcnow().isoformat())
    sd: float = 0.0

    def analyze(self) -> None:
        """Calcula densidade semântica da unidade."""
        self.sd = calculate_sd(self.content)

    def __repr__(self):
        return f"<{self.name.upper()} SD={self.sd:.2f}>"


# ============================================================
# 🔹 CONTEXT STATE
# ============================================================

@dataclass
class ContextState:
    """
    Representa o estado cognitivo total de um agente contextual.

    Componentes:
        - system: DNA do agente
        - user: input atual
        - history: histórico resumido
        - rag: conhecimento externo
        - tools: capacidades
    """

    system: ContextComponent
    user: ContextComponent
    history: ContextComponent
    rag: ContextComponent
    tools: ContextComponent

    sd: float = 0.0
    pc: float = 0.0
    regime: str = "Indefinido"
    tokens: int = 0

    def update_metrics(self):
        """Atualiza as métricas globais do contexto."""
        components = {
            "system": self.system.content,
            "user": self.user.content,
            "history": self.history.content,
            "rag": self.rag.content,
            "tools": self.tools.content,
        }
        self.sd = context_density(components)
        self.tokens = sum(len(v.split()) for v in components.values())
        self.pc = contextual_pressure({**components, "tokens": self.tokens})
        self.regime = classify_context_regime(self.sd, self.pc)

    def summary(self) -> Dict[str, Any]:
        """Retorna um snapshot resumido do estado contextual."""
        return {
            "sd": self.sd,
            "pc": self.pc,
            "regime": self.regime,
            "tokens": self.tokens,
        }

    def __repr__(self):
        return f"<ContextState SD={self.sd:.2f} PC={self.pc:.2f} Regime={self.regime}>"


# ============================================================
# 🔹 CONTEXT AGENT
# ============================================================

class ContextAgent:
    """
    Agente cognitivo com modo de operação contextual.

    Modos disponíveis:
        - minimal: foco inferencial (baixo PC)
        - saturation: foco criativo (alto PC)
        - equilibrium: balanço ético e avaliativo
    """

    def __init__(self, name: str, mode: str, system_prompt: str):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.mode = mode
        self.memory: List[Dict[str, str]] = []
        self.state = ContextState(
            system=ContextComponent("system", system_prompt),
            user=ContextComponent("user", ""),
            history=ContextComponent("history", ""),
            rag=ContextComponent("rag", ""),
            tools=ContextComponent("tools", "search_web, execute_code")
        )
        self.state.update_metrics()

    # ------------------------------
    # 💬 Interação
    # ------------------------------

    def update_user_input(self, text: str):
        """Atualiza input do usuário e recalcula estado."""
        self.state.user.content = text
        self.state.user.analyze()
        self.state.update_metrics()

    def recall_memory(self, k: int = 3) -> str:
        """Retorna últimos k registros de memória contextual."""
        return "\n".join([m["content"] for m in self.memory[-k:]])

    def memorize(self, role: str, content: str):
        """Armazena evento semântico na memória curta."""
        self.memory.append({
            "role": role,
            "content": content,
            "timestamp": datetime.datetime.utcnow().isoformat()
        })
        if len(self.memory) > 20:
            self.memory.pop(0)  # compressão leve

    def describe_state(self) -> str:
        """Retorna descrição semântica do estado atual."""
        s = self.state.summary()
        return (f"Agente: {self.name} ({self.mode})\n"
                f"SD: {s['sd']} | PC: {s['pc']} | Regime: {s['regime']} | Tokens: {s['tokens']}")

    # ------------------------------
    # ⚙️ Modo de operação
    # ------------------------------

    def adjust_mode(self):
        """Adapta comportamento com base em SD/PC."""
        sd, pc = self.state.sd, self.state.pc

        if pc < 0.4:
            self.mode = "minimal"
        elif 0.7 <= pc < 0.9:
            self.mode = "saturation"
        elif 0.6 <= pc <= 0.8 and 0.7 <= sd <= 0.85:
            self.mode = "equilibrium"
        else:
            self.mode = "adaptive"

    # ------------------------------
    # 🧠 Ciclo de raciocínio (simplificado)
    # ------------------------------

    def think(self, input_text: str) -> Dict[str, Any]:
        """
        Simula o ciclo cognitivo básico do agente:
        1. Recebe input
        2. Atualiza contexto
        3. Reavalia modo
        4. Retorna estado contextual
        """
        self.update_user_input(input_text)
        self.memorize("user", input_text)
        self.adjust_mode()

        return {
            "agent": self.name,
            "mode": self.mode,
            "context": self.state.summary(),
        }

    def __repr__(self):
        return f"<ContextAgent {self.name} Mode={self.mode} SD={self.state.sd:.2f} PC={self.state.pc:.2f}>"



# ============================================================
# 🔹 TESTE RÁPIDO
# ============================================================

if __name__ == "__main__":
    agent = ContextAgent(
        name="Athena",
        mode="minimal",
        system_prompt="Agente analítico especializado em síntese racional e compressão semântica."
    )

    print(agent.describe_state())

    result = agent.think("Analise as implicações da pressão contextual em IA criativa.")
    print(result)
