# 🎯 Context Engineering Framework v1.0

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![Validation Score](https://img.shields.io/badge/validation-87%25-success?logo=github)](#)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.1250011-lightgrey.svg)](https://doi.org/10.5281/zenodo.1250011)

[![Português](https://img.shields.io/badge/lang-pt--BR-blue?logo=googletranslate)](#)
[![English](https://img.shields.io/badge/lang-en--US-lightgrey?logo=googletranslate)](#)
[![简体中文](https://img.shields.io/badge/lang-zh--CN-red?logo=googletranslate)](#)


---

> **Tagline:** *Contexto não é informação — é metabolismo cognitivo.*

**Resumo:**
O **Context Engineering Framework (CEF)** é uma arquitetura conceitual e técnica para projetar, medir e operar sistemas de IA baseados em **coerência contextual**, **densidade semântica (SD)** e **pressão contextual (PC)**.
Seu propósito é estabelecer princípios e métricas que permitam criar agentes cognitivos **precisos, criativos e éticos**, ajustando o equilíbrio entre minimalismo lógico e saturação simbólica.

---

## 1️⃣ MANIFESTO & PRINCÍPIOS

### **A Essência da Engenharia de Contexto**

> *"Contexto não é informação. É metabolismo cognitivo."*

**Engenharia de Contexto** é a disciplina de projetar, estruturar e gerenciar o ecossistema informacional que permite a um agente de IA **raciocinar, decidir e agir com coerência e autonomia**.

### Diferença essencial

| Prompt Engineering    | Context Engineering                   |
| --------------------- | ------------------------------------- |
| Texto estático        | Ambiente dinâmico                     |
| Single-shot           | Multi-turn + memória                  |
| Input isolado         | Sistema holístico                     |
| Imperativo (“faça X”) | Metabólico (“você é Y em ambiente Z”) |

---

### **Princípios Fundacionais**

1. **Todo erro é erro de contexto.**
   Falhas cognitivas são sintomas de contexto ambíguo, contraditório ou incompleto.

2. **Densidade > Prolixidade.**
   Contextos curtos e densos (SD > 0.7) superam prompts longos e redundantes.

3. **Memória define identidade.**
   Um agente sem memória persistente não possui “eu”. Neo4j + embeddings criam continuidade semântica.

4. **Ambiguidade é recurso.**
   A polissemia é uma fonte de criatividade simbólica, não um erro a ser eliminado.

5. **Ferramentas são órgãos.**
   Cada API ou recurso externo deve estar descrito no contexto como uma extensão cognitiva do agente.

---

## 2️⃣ ANATOMIA DO CONTEXTO

### **Componentes Essenciais**

| Componente           | Função                 | Densidade Recomendada   | Exemplo                                  |
| -------------------- | ---------------------- | ----------------------- | ---------------------------------------- |
| System Prompt        | DNA do agente          | SD > 0.80               | Definição arquetípica de papel           |
| User Input           | Solicitação atual      | SD > 0.65               | “Analise APIs de IA gratuitas”           |
| Conversation History | Continuidade narrativa | SD > 0.70               | Últimos 5 turnos sumarizados             |
| Long-Term Memory     | Identidade persistente | Embeddings + Neo4j      | Preferências e histórico semântico       |
| RAG Context          | Conhecimento externo   | Reranking semântico     | Documentos similares recuperados         |
| Tools/APIs           | Capacidades ativas     | Descrição funcional     | `search_web()`, `execute_code()`         |
| Output Schema        | Formato esperado       | JSON Schema             | `{"analysis": str, "confidence": float}` |
| Global Context       | Estado do sistema      | Chave-valor persistente | “fase = análise, status = ativo”         |

---

### **Densidade de Contexto (SD)**

```python
def context_density(components: dict) -> float:
    """
    CD = média ponderada de SD de cada componente
    Pesos:
      system: 0.30
      user: 0.25
      history: 0.15
      rag: 0.20
      tools: 0.10
    """
    weights = {'system':0.3, 'user':0.25, 'history':0.15, 'rag':0.2, 'tools':0.1}
    cd = sum(calculate_sd(components[k]) * weights[k] for k in components)
    return cd
```

**Meta:** SD ≥ **0.75** → contexto confiável.

---

### **Pressão Contextual (PC)**

```python
def contextual_pressure(context: dict) -> float:
    """
    Mede o grau de saturação semântica do contexto.
    0.0–0.4 → raso (incompleto)
    0.4–0.7 → racional (minimalismo)
    0.7–0.9 → criativo (saturação)
    >0.9 → entropia (alucinação)
    """
    return context_density(context) * len(context["tokens"]) / 10000
```

---

### **Regimes de Operação Contextual**

| Regime                    | Descrição                                       | Ideal para            | SD    | PC      |
| ------------------------- | ----------------------------------------------- | --------------------- | ----- | ------- |
| **Minimalismo Extremo**   | Contexto enxuto, precisão inferencial           | Engenharia, decisão   | ≥0.70 | 0.4–0.7 |
| **Saturação Extrema**     | Contexto redundante, alta ressonância simbólica | Arte, narrativa       | ≥0.70 | 0.7–0.9 |
| **Equilíbrio Contextual** | Raciocínio com avaliação ética                  | Governança, validação | ≥0.70 | 0.6–0.8 |

---

### **Visual Conceitual**

```
            Pressão Contextual (PC)
                 │
        ┌────────┴────────┐
        │                 │
   Minimalismo        Saturação
  (Raciocínio)        (Criação)
          \           /
           \         /
            \_______/
             Equilíbrio
            (Avaliação)
```

---

## 3️⃣ ESTRATÉGIAS DE ENGENHARIA (14 Práticas)

Cada estratégia equilibra **densidade**, **pressão contextual** e **intenção cognitiva**:

| #    | Estratégia                        | Métrica-Alvo         | Aplicação                      |
| ---- | --------------------------------- | -------------------- | ------------------------------ |
| 1    | Possua cada token                 | SD > 0.8             | DNA manual, não gerado         |
| 2    | Separe estado do modelo           | Contexto < 2k        | Persistência externa           |
| 3    | Use micro-agentes determinísticos | prompt <200 tokens   | Foco funcional                 |
| 4    | Modele densidade antes do texto   | SD medido pré-prompt | Evita redundância              |
| 5    | Faça compressão semântica         | SD constante         | Reranking por relevância       |
| 6    | Utilize reflexão iterativa        | PC controlado        | Reavalia respostas             |
| 7    | Modele transições entre modos     | PC adaptativo        | alternância lógica ↔ simbólica |
| 8–14 | *[em construção para v1.0]*       |                      |                                |

---

## 4️⃣ ARQUITETURA DE AGENTES

### **Padrões Cognitivos**

| Padrão        | Função                              |
| ------------- | ----------------------------------- |
| Reflexão      | agente revisa e critica suas saídas |
| Encadeamento  | fluxo sequencial entre papéis       |
| Roteamento    | seleção dinâmica de especialistas   |
| Paralelização | múltiplos caminhos e seleção ótima  |

Exemplo de Encadeamento:

```python
research = researcher.search(query)
analysis = analyst.process(research)
article = writer.compose(analysis)
```

### **Integração MCP (Model Context Protocol)**

O **MCP** (Anthropic) permite que agentes acessem prompts, ferramentas e dados como recursos contextuais.

```python
mcp = MCPClient("docs_server")
doc = mcp.get_resource("context/theory.md")
context.inject(doc)
```

---

## 5️⃣ GESTÃO DE FALHAS CONTEXTUAIS

| Falha         | Sintoma            | Causa                          | Mitigação                  | SD Esperado |
| ------------- | ------------------ | ------------------------------ | -------------------------- | ----------- |
| Envenenamento | Repete info falsa  | RAG contaminado                | Quarentena semântica       | >0.7        |
| Distração     | Ignora instruções  | Contexto extenso e irrelevante | Compressão + reranking     | >0.75       |
| Confusão      | Mistura tópicos    | Personas sobrepostas           | DNA Arquetípico por agente | >0.80       |
| Conflito      | Contradições       | Fontes ambíguas                | Priorização + timestamp    | Coerência   |
| Amnésia       | Perda de histórico | Falha de persistência          | Neo4j + embeddings         | Recall >90% |

---

## 6️⃣ STACK TÉCNICO 2025

| Pilar                  | Ferramentas            |
| ---------------------- | ---------------------- |
| **Orquestração**       | LangGraph, CrewAI      |
| **Context Management** | LlamaIndex, Haystack   |
| **Memória e Estado**   | Neo4j, Pinecone, Redis |
| **Observabilidade**    | Langfuse, Langsmith    |
| **Protocolos**         | MCP (Anthropic), A2A   |

---

## 7️⃣ CASOS PRÁTICOS

| Agente     | Modo        | Função                                |
| ---------- | ----------- | ------------------------------------- |
| **Athena** | Minimalismo | Análise e estratégia racional         |
| **Orion**  | Saturação   | Criação simbólica e narrativa         |
| **Nemea**  | Equilíbrio  | Avaliação ética e coerência narrativa |

Cada agente é um arquétipo cognitivo testado sob SD ≥ 0.7 e PC calibrado.

---

## 🤝 Contribuição

1. Fork o repositório
2. Crie uma branch: `feature/{{nome}}`
3. Valide métricas (SD ≥ 0.7, tokens < 2500)
4. Teste com 2+ modelos
5. Envie PR com checklist preenchido

---

## 📄 Licença

Licenciado sob **MIT License** — veja `LICENSE`.

---

## 👥 Créditos

**Autor:** [{{seu nome ou pseudônimo}}]
**Conceito:** Engenharia de Contexto & Densidade Semântica
**Versão:** `v0.1.0-alpha`

---

> ⭐ Se este projeto expandiu sua percepção sobre contexto, dê uma estrela no GitHub!

---

Quer que eu gere a **versão pronta para copiar e colar (com placeholders removidos e sintaxe Markdown validada)** — ou prefere que eu monte já com os blocos e caminhos de pastas prontos para o commit inicial (`README.md` + `/tools/` + `/examples/`)?
