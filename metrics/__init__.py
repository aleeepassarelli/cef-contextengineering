"""
📦 metrics
Módulo de métricas e validação de coerência contextual
Parte do Context Engineering Framework (CEF)
Autor: Deep Systems Lab
Licença: MIT
"""

from core.context_metrics import calculate_sd, contextual_pressure
from metrics.coherence_tests import validate_context, infer_regime, print_report, THRESHOLDS

__all__ = [
    "calculate_sd",
    "contextual_pressure",
    "validate_context",
    "infer_regime",
    "print_report",
    "THRESHOLDS"
]

# 🔧 Metadados do pacote
__version__ = "1.0.0"
__description__ = "Módulos de métricas e validação do Context Engineering Framework"
__author__ = "Deep Systems Lab"
__license__ = "MIT"
