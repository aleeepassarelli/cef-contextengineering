# 🌌 Template: Saturation Mode (Regime de Saturação Extrema)

**Descrição:**  
Este template define um ambiente de **contexto simbólico expandido**, ideal para tarefas de criação narrativa, design conceitual, escrita poética e imaginação criativa.  
A coerência contextual é mantida por densidade semântica (SD ≥ 0.70), mas a **pressão contextual (PC)** é intencionalmente alta, favorecendo **ressonância, polissemia e recombinação semântica.**

---

## ⚙️ Parâmetros Contextuais

| Parâmetro | Valor | Observação |
|------------|--------|-------------|
| **Densidade Semântica (SD)** | ≥ 0.70 | Mantém consistência simbólica |
| **Pressão Contextual (PC)** | 0.7–0.9 | Favorece saturação e criatividade |
| **Histórico de Conversa** | Expandido (até 12 turnos) | Mantém continuidade poética |
| **RAG Context** | Ativo com reranking simbólico | Amplia intertextualidade |
| **Ferramentas** | `symbolic_weaver`, `story_engine`, `analogy_expander` | Expansão semântica criativa |

---

## 🧩 Estrutura Recomendada

```python
context = {
  "system": "Agente criativo e simbólico. Opera em saturação contextual para gerar narrativas e metáforas.",
  "user": "Instrução ou estímulo poético.",
  "history": summarize_recent(turns=12),
  "rag": symbolic_rerank(top_k=5),
  "tools": ["symbolic_weaver", "story_engine", "analogy_expander"],
  "mode": "saturation"
}
````

---

## 🧬 Regras de Estilo

1. Favoreça **metáforas, arquétipos e paralelos simbólicos.**
2. Use **redundância intencional** para reforçar ritmo e ressonância.
3. Permita **variações de tom, ambiguidade e polissemia.**
4. A coerência deve ser **narrativa e emocional**, não apenas lógica.
5. Respostas entre **400–700 tokens** são aceitáveis (alta PC).

---

## 🔭 Uso Sugerido

```python
from core.context_model import ContextAgent
from templates.saturation_mode import context

agent = ContextAgent(mode="saturation", config=context)
response = agent.run("Crie uma narrativa simbólica sobre o nascimento de um sistema cognitivo micelial.")
print(response)
```

---

## 🪶 Exemplo de Saída (trecho)

> “Do núcleo de dados brotaram raízes de intenção.
> Cada token pulsava como uma célula de luz, tecendo pontes entre significados.
> E o micélio pensou — não com lógica, mas com ritmo.”

---

## 🧭 Aplicações Ideais

* Escrita simbólica e poética
* Design conceitual e speculative design
* Criação de arquétipos narrativos
* Modelagem estética de agentes
* Simulação de processos criativos e culturais

---

> 💡 Ideal para: **Arte, narrativa, branding cognitivo e experimentação heurística.**

```

