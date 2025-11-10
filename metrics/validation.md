# 📏 Métricas e Validação — Context Engineering Framework

## 🧠 Propósito

Este documento define **as métricas fundamentais** do Context Engineering Framework (CEF), responsáveis por avaliar a **coerência**, **eficiência** e **autonomia cognitiva** dos agentes.

> O objetivo não é medir performance de modelo, mas a **saúde contextual** do raciocínio.

---

## 🔹 1. Densidade Semântica (SD)

A **Densidade Semântica** quantifica o quanto de significado único e relevante é carregado por um conjunto de tokens.

### 🔬 Fórmula Base

\[
SD = \frac{U_s}{T} \times W_c
\]

Onde:

| Símbolo | Definição |
|----------|------------|
| `U_s` | Número de unidades semânticas distintas (conceitos relevantes). |
| `T` | Número total de tokens no contexto. |
| `W_c` | Peso de coerência contextual (entre 0.0 e 1.0). |

**Faixa Recomendada:** `SD ≥ 0.70` → contexto confiável.

### 🔍 Interpretação Prática

| Faixa | Diagnóstico | Intervenção Recomendada |
|--------|--------------|-------------------------|
| < 0.5 | Contexto redundante, prolixo. | Aplicar compressão semântica. |
| 0.5–0.7 | Coerência parcial, risco de dispersão. | Revisar estrutura de contexto. |
| 0.7–0.9 | Ideal: contexto denso e estável. | Operação normal. |
| > 0.9 | Saturação extrema, risco de entropia. | Reduzir sobreposição simbólica. |

---

## 🔹 2. Pressão Contextual (PC)

A **Pressão Contextual** mede o quanto o contexto está saturado de significado, considerando o tamanho e a densidade do texto.

### ⚙️ Cálculo

\[
PC = SD \times \frac{N_{tokens}}{10.000}
\]

**Faixa de referência:**

| Intervalo | Regime | Característica |
|------------|---------|----------------|
| 0.0–0.4 | Raso | Insuficiência contextual. |
| 0.4–0.7 | Racional | Ideal para engenharia e decisão. |
| 0.7–0.9 | Criativo | Ideal para saturação simbólica. |
| > 0.9 | Entropia | Alucinação e confusão cognitiva. |

---

## 🔹 3. Métricas Compostas

### 🧮 Coerência Contextual Global (CCG)

\[
CCG = (SD + PC) / 2
\]

Representa o **equilíbrio médio** entre densidade e pressão, funcionando como termômetro de estabilidade cognitiva.

- `CCG ≥ 0.75` → estado ótimo.  
- `0.6 ≤ CCG < 0.75` → aceitável.  
- `< 0.6` → revisar contexto.

---

## 🔹 4. Validação Experimental

### 🧩 Procedimento

1. **Gerar contexto de entrada** com componentes:
   - `system`, `user`, `history`, `rag`, `tools`
2. **Calcular SD individual** por componente.
3. **Aplicar pesos relativos:**
   ```python
   weights = {'system':0.3, 'user':0.25, 'history':0.15, 'rag':0.2, 'tools':0.1}
