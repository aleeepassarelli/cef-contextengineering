"""
core package — Context Engineering Framework (CEF)
────────────────────────────────────────────
Núcleo de funções e estruturas responsáveis pela
engenharia de contexto, métricas e agentes cognitivos.

Importa e expõe:
- Métricas de contexto (SD, PC)
- Modelos de agente e estado contextual

────────────────────────────────────────────
Autor: Context Engineering Lab
Licença: MIT
Versão: 1.0.0
"""

from core.context_metrics import (
    calculate_sd,
    context_density,
    contextual_pressure,
    classify_context_regime
)

from core.context_model import (
    ContextComponent,
    ContextState,
    ContextAgent
)

__all__ = [
    # Métricas
    "calculate_sd",
    "context_density",
    "contextual_pressure",
    "classify_context_regime",
    
    # Estruturas
    "ContextComponent",
    "ContextState",
    "ContextAgent",
]

__version__ = "1.0.0"
__author__ = "Context Engineering Lab"
__license__ = "MIT"
__description__ = "Core do Context Engineering Framework — métricas, modelos e agentes contextuais."


def framework_info() -> str:
    """Retorna metadados resumidos sobre o framework."""
    return (
        f"Context Engineering Framework (CEF)\n"
        f"Versão: {__version__}\n"
        f"Autor: {__author__}\n"
        f"Licença: {__license__}\n"
        f"Componentes disponíveis: {', '.join(__all__)}"
    )


if __name__ == "__main__":
    print(framework_info())
