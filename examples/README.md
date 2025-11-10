# 🧪 Exemplos — Context Engineering Framework (CEF)

O diretório **`examples/`** contém agentes de demonstração que implementam os **três regimes contextuais fundamentais** do CEF:

- **Minimalismo (Athena)** — Raciocínio lógico, foco e precisão.  
- **Saturação (Orion)** — Criação simbólica e divergência criativa.  
- **Equilíbrio (Nemea)** — Julgamento ético e coerência integrativa.

Cada agente foi calibrado para operar com **densidade semântica (SD)** ≥ 0.70 e **pressão contextual (PC)** ajustada ao seu modo.

---

## ⚙️ Estrutura

```

examples/
│
├── agent_athena.py   # Agente racional e minimalista
├── agent_orion.py    # Agente criativo e simbólico
├── agent_nemea.py    # Agente avaliador e ético
└── README.md          # Este guia

````

---

## 🧠 Modos de Operação

| Agente | Modo | Faixa de Pressão (PC) | Descrição |
|--------|------|------------------------|------------|
| **Athena** | Minimalismo | 0.4–0.7 | Busca máxima precisão e clareza lógica. Ideal para análise, síntese e decisão. |
| **Orion** | Saturação | 0.7–0.9 | Explora campos simbólicos, metáforas e deriva criativa. Ideal para ideação e narrativa. |
| **Nemea** | Equilíbrio | 0.6–0.8 | Pondera coerência, estética e ética. Ideal para validação e avaliação contextual. |

---

## 🧩 Estrutura Básica de um Agente

Cada exemplo segue uma estrutura comum:

```python
from core import calculate_sd, contextual_pressure, ContextAgent

# Definição do agente
agent = ContextAgent(
    name="Athena",
    mode="minimal",
    description="Agente racional, focado em análise e síntese lógica."
)

# Entrada do usuário
query = "Explique como medir densidade semântica em contextos curtos."

# Execução do raciocínio
response = agent.think(query)

# Cálculo de métricas contextuais
sd = calculate_sd(query)
pc = contextual_pressure({"tokens": query.split(), "density": sd})

print(f"Athena → SD: {sd:.2f}, PC: {pc:.2f}")
print("Saída:", response)
````

---

## 🔍 Métricas de Validação

| Métrica                      | Descrição                                                         | Faixa Ideal |
| ---------------------------- | ----------------------------------------------------------------- | ----------- |
| **SD (Semantic Density)**    | Coerência informacional interna do texto.                         | ≥ 0.70      |
| **PC (Contextual Pressure)** | Grau de saturação cognitiva (tensão entre lógica e criatividade). | 0.4–0.9     |
| **Tokens**                   | Tamanho total do contexto ativo.                                  | ≤ 2500      |

As métricas são calculadas automaticamente a partir do módulo `core/context_metrics.py`.

---

## 🧭 Casos de Uso

### 🩵 Athena — Raciocínio Analítico

```bash
python examples/agent_athena.py
```

> Resultado: análise concisa e coerente, SD elevado, PC controlado (~0.5)

### 🔥 Orion — Criação Simbólica

```bash
python examples/agent_orion.py
```

> Resultado: discurso imaginativo, alta entropia criativa, PC ~0.8

### ⚖️ Nemea — Avaliação Ética

```bash
python examples/agent_nemea.py
```

> Resultado: balanço lógico-estético, autoavaliação do contexto, PC ~0.7

---

## 🧬 Dica Avançada

Você pode **combinar modos** encadeando agentes:

```python
athena_output = athena.think("Analise os fatores éticos da IA generativa.")
nemea_output = nemea.think(f"Avalie criticamente a análise de Athena: {athena_output}")
```

📎 Essa abordagem cria **metacognição artificial**, onde agentes refletem sobre o raciocínio uns dos outros.

---

## 🧠 Recomendado Ler Antes

* [`docs/theory.md`](../docs/theory.md) → Fundamentos teóricos da Engenharia de Contexto
* [`core/context_metrics.py`](../core/context_metrics.py) → Fórmulas de densidade e pressão
* [`usage_demo.ipynb`](../usage_demo.ipynb) → Notebook interativo de exploração

---

## 📄 Licença

MIT License © 2025 — Context Engineering Framework

> *“Densidade é estrutura; coerência é energia.”*

```
