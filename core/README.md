
# 🧩 Núcleo — `core/`

O diretório **`core/`** contém os módulos fundamentais do **Context Engineering Framework (CEF)**.  
Aqui estão definidas as funções métricas, estruturas de dados e classes base que sustentam o funcionamento de todos os agentes e modos operacionais.

---

## 📂 Estrutura

```

core/
│
├── **init**.py              # Inicializa o pacote e exporta funções-chave
├── context_metrics.py       # Métricas: SD (densidade), PC (pressão), regimes contextuais
├── context_model.py         # Classes: ContextComponent, ContextState, ContextAgent
└── context_memory.py        # (em construção) Mecanismo de memória semântica persistente

````

---

## ⚙️ Módulos e Funções

### 🔹 `context_metrics.py`

Define as funções que medem **qualidade e comportamento contextual**:

| Função | Descrição |
|--------|------------|
| `calculate_sd(text)` | Calcula a densidade semântica de um trecho textual |
| `context_density(components)` | Média ponderada da coerência entre blocos contextuais |
| `contextual_pressure(context)` | Mede o grau de saturação semântica (foco ↔ criatividade) |
| `classify_context_regime(cd, pc)` | Retorna se o contexto está em modo Minimalista, Saturado ou Equilibrado |

📈 *Objetivo:* Quantificar o metabolismo cognitivo de um agente.

---

### 🔹 `context_model.py`

Define as **estruturas cognitivas** básicas para modelar um contexto:

| Classe | Função |
|--------|--------|
| `ContextComponent` | Representa um elemento do contexto (system, user, RAG, tools, etc.) |
| `ContextState` | Estrutura que agrega todos os componentes e suas métricas |
| `ContextAgent` | Entidade cognitiva que pensa e reage com base no estado contextual |

🧠 *Objetivo:* Fornecer abstrações para raciocínio baseado em densidade e pressão.

---

### 🔹 `context_memory.py` (opcional)

Integra mecanismos de **memória semântica persistente**:

- Suporte a **Neo4j**, **Pinecone** e **Redis**
- Armazena embeddings de contexto
- Recupera e injeta histórico relevante (RAG semântico)
- Base para funções como `recall()`, `store_context()`, `link_memory_graph()`

📘 *Objetivo:* Dar identidade e continuidade cognitiva aos agentes.

---

## 🔬 Exemplo de Uso

```python
from core import (
    calculate_sd,
    contextual_pressure,
    ContextAgent
)

text = "A engenharia de contexto busca otimizar coerência semântica e foco inferencial."
sd = calculate_sd(text)
pc = contextual_pressure({"tokens": text.split(), "density": sd})

agent = ContextAgent("Athena", mode="minimal", description="Agente analítico racional.")
result = agent.think("Explique a diferença entre contexto e informação.")

print(f"Densidade: {sd:.2f}, Pressão: {pc:.2f}")
print("Saída:", result)
````

---

## 🧪 Testes e Validação

Testes unitários e métricos podem ser executados via:

```bash
pytest tests/core/
```

Critérios de validação mínima:

* `SD ≥ 0.70`
* `0.4 ≤ PC ≤ 0.9`
* `Tokens ≤ 2500`

---

## 📄 Licença

MIT License © 2025 — Context Engineering Lab
“**Todo erro é erro de contexto.**”

---

## 🧭 Próximos passos

* [ ] Adicionar `context_memory.py` com persistência Neo4j mock
* [ ] Implementar medição de entropia vetorial
* [ ] Integrar métricas com observabilidade (Langfuse / Langsmith)
* [ ] Publicar pacote `cef-core` no PyPI

---

> *"Densidade é estrutura. Coerência é energia."*
> — Context Engineering Framework

```

