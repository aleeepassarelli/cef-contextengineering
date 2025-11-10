# 📊 Context Metrics — Validação e Medição de Coerência Contextual

Parte integrante do **Context Engineering Framework (CEF)**  
Licença: MIT  
Versão: v1.0.0  

---

## 🧩 Propósito

O módulo **`metrics/`** define e valida as métricas fundamentais de **densidade semântica (SD)** e **pressão contextual (PC)**, que são os pilares quantitativos da **engenharia de contexto**.

Essas métricas permitem avaliar se um agente está operando em **regime racional (minimalismo)**, **simbólico (saturação)** ou **avaliativo (equilíbrio)**.

---

## ⚙️ Principais Componentes

| Arquivo | Função | Descrição |
|----------|--------|-----------|
| `coherence_tests.py` | Validação automática | Executa testes de coerência e classifica o regime contextual |
| `__init__.py` | Integração de métricas | Exposição de funções principais |
| `validation.md` | Documento de referência | Fundamentos teóricos e metodológicos da validação |

---

## 🧠 Métricas Principais

### 1️⃣ Densidade Semântica (SD)

**Definição:**  
Mede a **proporção de tokens semanticamente informativos** em relação ao total do contexto.

```python
from core.context_metrics import calculate_sd

sd = calculate_sd(context)
if sd >= 0.7:
    print("✅ Contexto coerente e informativo")
````

**Faixas de operação:**

| Faixa     | Interpretação                                                 |
| --------- | ------------------------------------------------------------- |
| `< 0.5`   | Contexto raso — provável ambiguidade ou redundância           |
| `0.5–0.7` | Contexto funcional — aceitável para instruções diretas        |
| `≥ 0.7`   | Contexto coerente e confiável — ideal para agentes cognitivos |

---

### 2️⃣ Pressão Contextual (PC)

**Definição:**
Indica o **grau de saturação semântica**, considerando densidade e volume textual.

```python
from core.context_metrics import contextual_pressure

pc = contextual_pressure(context)
```

**Faixas de Pressão:**

| PC        | Regime                  | Uso Ideal                     |
| --------- | ----------------------- | ----------------------------- |
| `0.0–0.4` | **Raso**                | Pré-análise, setup inicial    |
| `0.4–0.7` | **Minimalismo Extremo** | Engenharia, decisão lógica    |
| `0.7–0.9` | **Saturação Extrema**   | Criação simbólica, narrativa  |
| `>0.9`    | **Entropia**            | Risco de alucinação semântica |

---

## 🧪 Validação de Contexto

```python
from metrics import validate_context, print_report

context = {
    "system": "...",
    "user": "...",
    "history": "...",
    "rag": "...",
    "tools": "..."
}

report = validate_context(context)
print_report(report)
```

Saída esperada:

```
✅ SD = 0.78 | PC = 0.63 | Regime: Equilíbrio Contextual
```

---

## 🔬 Regimes Operacionais

| Regime          | SD    | PC      | Descrição                             |
| --------------- | ----- | ------- | ------------------------------------- |
| **Minimalismo** | ≥0.70 | 0.4–0.7 | Precisão lógica e inferencial         |
| **Saturação**   | ≥0.70 | 0.7–0.9 | Criatividade simbólica                |
| **Equilíbrio**  | ≥0.70 | 0.6–0.8 | Avaliação ética e coerência narrativa |

---

## 🧭 Exemplos de Aplicação

**Em um agente de raciocínio (Athena):**

```python
from metrics import infer_regime

regime = infer_regime(sd=0.75, pc=0.58)
# → "Minimalismo Extremo"
```

**Em um agente de criação (Orion):**

```python
regime = infer_regime(sd=0.74, pc=0.82)
# → "Saturação Extrema"
```

**Em um agente avaliador (Nemea):**

```python
regime = infer_regime(sd=0.79, pc=0.68)
# → "Equilíbrio Contextual"
```

---

## 🧱 Integração com o Framework

As funções do pacote `metrics` são utilizadas por:

* `core/context_metrics.py` (cálculo base)
* `context_model.py` (avaliação do agente)
* `usage_demo.ipynb` (demonstração interativa)
* `coherence_tests.py` (testes automatizados)

---

## 📈 Critério de Aprovação

Um contexto é **válido para produção** quando:

```text
SD ≥ 0.70
0.4 ≤ PC ≤ 0.9
Sem inconsistências heurísticas detectadas
```

---

## 🧩 Créditos

**Autor:** Deep Systems Lab
**Conceito:** Engenharia de Contexto e Densidade Semântica
**Versão:** v1.0.0
**Licença:** MIT License

---

⭐ Se este módulo ajudou a calibrar seus agentes cognitivos, dê uma estrela no repositório!

```
