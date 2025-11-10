### Agora, o conteúdo inicial de `templates/minimal_mode.md` 🧩


# 🧱 Template: Minimal Mode (Regime de Minimalismo Extremo)

**Descrição:**  
Este template define um ambiente de contexto minimalista, ideal para tarefas de raciocínio técnico, inferência lógica e análise estruturada.

---

## ⚙️ Parâmetros Contextuais

| Parâmetro | Valor | Observação |
|------------|--------|-------------|
| **Densidade Semântica (SD)** | ≥ 0.70 | Mantém coerência e precisão |
| **Pressão Contextual (PC)** | 0.4–0.7 | Evita saturação simbólica |
| **Histórico de Conversa** | Reduzido a 3 turnos | Minimiza ruído inferencial |
| **RAG Context** | Desativado ou restrito | Operação puramente inferencial |
| **Ferramentas** | `analysis_engine`, `logic_unit` | Foco racional |

---

## 🧩 Estrutura Recomendada

```python
context = {
  "system": "Agente lógico de análise e decisão.",
  "user": "Pergunta ou problema atual.",
  "history": summarize_recent(turns=3),
  "tools": ["analysis_engine", "logic_unit"],
  "mode": "minimal"
}
````

---

## 🔍 Regras de Estilo

1. Use **frases curtas**, **precisas** e **sem redundância**.
2. Evite metáforas, ironia e polissemia.
3. Cada sentença deve **transmitir uma relação causal ou lógica clara**.
4. A resposta final deve conter **no máximo 200 tokens**.

---

## 🧭 Uso Sugerido

```python
from core.context_model import ContextAgent
from templates.minimal_mode import context

agent = ContextAgent(mode="minimal", config=context)
response = agent.run("Analise a viabilidade de um modelo RAG para dados financeiros.")
print(response)
```

---

> 💡 Ideal para: **Engenharia**, **validação lógica**, **auditoria semântica** e **decisão algorítmica.**

```

```
