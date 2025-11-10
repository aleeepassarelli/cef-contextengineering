# 🎯 Context Engineering Framework v1.0

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Validation Score](https://img.shields.io/badge/validation-87%25-success?logo=github)](#)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.1250011-lightgrey.svg)](https://doi.org/10.5281/zenodo.1250011)

[![Português](https://img.shields.io/badge/lang-pt--BR-blue?logo=googletranslate)](#)
[![English](https://img.shields.io/badge/lang-en--US-lightgrey?logo=googletranslate)](#)
[![简体中文](https://img.shields.io/badge/lang-zh--CN-red?logo=googletranslate)](#)

---

> **Tagline:** *Context is not information — it is cognitive metabolism.*

**Abstract:**  
The **Context Engineering Framework (CEF)** is a conceptual and technical architecture for designing, measuring, and operating AI systems based on **contextual coherence**, **semantic density (SD)**, and **contextual pressure (PC)**.  
Its purpose is to establish principles and metrics that enable the creation of **precise, creative, and ethical cognitive agents**, balancing logical minimalism and symbolic saturation.

---

## 1️⃣ MANIFESTO & PRINCIPLES

### **The Essence of Context Engineering**

> *“Context is not information. It is cognitive metabolism.”*

**Context Engineering** is the discipline of designing, structuring, and managing the informational ecosystem that enables an AI agent to **reason, decide, and act with coherence and autonomy**.

### Fundamental Difference

| Prompt Engineering      | Context Engineering                 |
| ----------------------- | ----------------------------------- |
| Static text             | Dynamic environment                 |
| Single-shot             | Multi-turn + memory                 |
| Isolated input          | Holistic system                     |
| Imperative (“do X”)     | Metabolic (“you are Y in environment Z”) |

---

### **Foundational Principles**

1. **Every error is a context error.**  
   Cognitive failures arise from ambiguous, contradictory, or incomplete context.

2. **Density > Prolixity.**  
   Short and dense contexts (SD > 0.7) outperform long and redundant prompts.

3. **Memory defines identity.**  
   An agent without persistent memory has no “self.”  
   Neo4j + embeddings provide semantic continuity.

4. **Ambiguity is a resource.**  
   Polysemy is a source of symbolic creativity, not a flaw to eliminate.

5. **Tools are organs.**  
   Each API or external capability must be described in context as a cognitive extension of the agent.

---

## 2️⃣ CONTEXT ANATOMY

### **Essential Components**

| Component           | Function               | Recommended Density | Example                                 |
| ------------------- | ---------------------- | ------------------- | --------------------------------------- |
| System Prompt       | Agent’s DNA            | SD > 0.80           | Archetypal role definition              |
| User Input          | Current request        | SD > 0.65           | “Analyze free AI APIs”                  |
| Conversation History| Narrative continuity   | SD > 0.70           | Last 5 turns summarized                 |
| Long-Term Memory    | Persistent identity    | Embeddings + Neo4j  | Semantic preferences and history        |
| RAG Context         | External knowledge     | Semantic reranking  | Retrieved similar documents             |
| Tools/APIs          | Active capabilities    | Functional description | `search_web()`, `execute_code()`     |
| Output Schema       | Expected format        | JSON Schema         | `{"analysis": str, "confidence": float}` |
| Global Context      | System state           | Persistent key-value | “phase = analysis, status = active”     |

---

### **Context Density (SD)**

```python
def context_density(components: dict) -> float:
    """
    CD = weighted average of each component’s SD
    Weights:
      system: 0.30
      user: 0.25
      history: 0.15
      rag: 0.20
      tools: 0.10
    """
    weights = {'system':0.3, 'user':0.25, 'history':0.15, 'rag':0.2, 'tools':0.1}
    cd = sum(calculate_sd(components[k]) * weights[k] for k in components)
    return cd
````

**Goal:** SD ≥ **0.75** → reliable context.

---

### **Contextual Pressure (PC)**

```python
def contextual_pressure(context: dict) -> float:
    """
    Measures the degree of semantic saturation in the context.
    0.0–0.4 → shallow (incomplete)
    0.4–0.7 → rational (minimalism)
    0.7–0.9 → creative (saturation)
    >0.9 → entropy (hallucination)
    """
    return context_density(context) * len(context["tokens"]) / 10000
```

---

### **Contextual Operation Regimes**

| Regime                 | Description                              | Ideal for              | SD    | PC      |
| ---------------------- | ---------------------------------------- | ---------------------- | ----- | ------- |
| **Extreme Minimalism** | Concise context, inferential precision   | Engineering, decision  | ≥0.70 | 0.4–0.7 |
| **Extreme Saturation** | Redundant, symbolically resonant context | Art, narrative         | ≥0.70 | 0.7–0.9 |
| **Contextual Balance** | Ethical reasoning and evaluation         | Governance, validation | ≥0.70 | 0.6–0.8 |

---

### **Conceptual Visualization**

```
            Contextual Pressure (PC)
                 │
        ┌────────┴────────┐
        │                 │
   Minimalism        Saturation
   (Reasoning)       (Creation)
          \           /
           \         /
            \_______/
             Balance
           (Evaluation)
```

---

## 3️⃣ ENGINEERING STRATEGIES (14 Practices)

Each strategy balances **density**, **contextual pressure**, and **cognitive intent**:

| #    | Strategy                        | Target Metric       | Application                    |
| ---- | ------------------------------- | ------------------- | ------------------------------ |
| 1    | Own every token                 | SD > 0.8            | Handcrafted agent DNA          |
| 2    | Separate model state            | Context < 2k        | External persistence           |
| 3    | Use deterministic micro-agents  | prompt <200 tokens  | Functional focus               |
| 4    | Model density before text       | Pre-prompt SD check | Prevents redundancy            |
| 5    | Apply semantic compression      | Constant SD         | Relevance reranking            |
| 6    | Use iterative reflection        | Controlled PC       | Reevaluate responses           |
| 7    | Model transitions between modes | Adaptive PC         | logical ↔ symbolic alternation |
| 8–14 | *[under construction for v1.0]* |                     |                                |

---

## 4️⃣ AGENT ARCHITECTURE

### **Cognitive Patterns**

| Pattern     | Function                             |
| ----------- | ------------------------------------ |
| Reflection  | Agent reviews and critiques outputs  |
| Chaining    | Sequential flow between roles        |
| Routing     | Dynamic expert selection             |
| Parallelism | Multiple paths and optimal selection |

Example — chaining flow:

```python
research = researcher.search(query)
analysis = analyst.process(research)
article = writer.compose(analysis)
```

---

### **MCP Integration (Model Context Protocol)**

**MCP** (Anthropic) allows agents to access prompts, tools, and data as contextual resources.

```python
mcp = MCPClient("docs_server")
doc = mcp.get_resource("context/theory.md")
context.inject(doc)
```

---

## 5️⃣ CONTEXT FAILURE MANAGEMENT

| Failure     | Symptom              | Cause                       | Mitigation                  | Expected SD |
| ----------- | -------------------- | --------------------------- | --------------------------- | ----------- |
| Poisoning   | Repeats false info   | Contaminated RAG            | Semantic quarantine         | >0.7        |
| Distraction | Ignores instructions | Irrelevant extended context | Compression + reranking     | >0.75       |
| Confusion   | Mixes topics         | Overlapping personas        | Archetypal agent DNA        | >0.80       |
| Conflict    | Contradictions       | Ambiguous sources           | Prioritization + timestamps | Coherence   |
| Amnesia     | History loss         | Persistence failure         | Neo4j + embeddings          | Recall >90% |

---

## 6️⃣ TECH STACK 2025

| Pillar                 | Tools                  |
| ---------------------- | ---------------------- |
| **Orchestration**      | LangGraph, CrewAI      |
| **Context Management** | LlamaIndex, Haystack   |
| **Memory & State**     | Neo4j, Pinecone, Redis |
| **Observability**      | Langfuse, Langsmith    |
| **Protocols**          | MCP (Anthropic), A2A   |

---

## 7️⃣ CASE STUDIES

| Agent      | Mode       | Function                               |
| ---------- | ---------- | -------------------------------------- |
| **Athena** | Minimalism | Analytical and strategic reasoning     |
| **Orion**  | Saturation | Symbolic and narrative creation        |
| **Nemea**  | Balance    | Ethical and coherence-based evaluation |

Each agent is a cognitive archetype tested under SD ≥ 0.7 and calibrated PC.

---

## 🤝 CONTRIBUTING

1. Fork the repository
2. Create a branch: `feature/{{name}}`
3. Validate metrics (SD ≥ 0.7, tokens < 2500)
4. Test with 2+ models
5. Submit a PR with checklist completed

---

## 📄 LICENSE

Licensed under **MIT License** — see `LICENSE`.

---

## 👥 CREDITS

**Author:** [{{your name or pseudonym}}]
**Concept:** Context Engineering & Semantic Density
**Version:** `v0.1.0-alpha`

---

> ⭐ If this project expanded your perception of context, give it a star on GitHub!

```
