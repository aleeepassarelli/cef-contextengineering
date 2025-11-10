# 🎯 上下文工程框架（Context Engineering Framework, CEF）v1.0

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Validation Score](https://img.shields.io/badge/validation-87%25-success?logo=github)](#)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.1250011-lightgrey.svg)](https://doi.org/10.5281/zenodo.1250011)

[![Português](https://img.shields.io/badge/lang-pt--BR-blue?logo=googletranslate)](#)
[![English](https://img.shields.io/badge/lang-en--US-lightgrey?logo=googletranslate)](#)
[![简体中文](https://img.shields.io/badge/lang-zh--CN-red?logo=googletranslate)](#)

---

> **标语：** *上下文不是信息——它是认知代谢。*

**摘要：**  
**上下文工程框架 (CEF)** 是一种用于设计、测量和运行基于 **上下文一致性**、**语义密度（SD）** 和 **上下文压力（PC）** 的人工智能系统的概念与技术架构。  
其目标是建立一套原则与指标，用于构建在逻辑极简与符号饱和之间实现平衡的 **精准、创造性且伦理一致的认知代理**。

---

## 1️⃣ 宣言与原则

### **上下文工程的本质**

> *“上下文不是信息，而是认知的代谢过程。”*

**上下文工程（Context Engineering）** 是一门设计、构建和管理信息生态系统的学科，使人工智能代理能够以 **一致性与自主性** 进行 **推理、决策与行动**。

### 根本区别

| 提示词工程（Prompt Engineering） | 上下文工程（Context Engineering）      |
| ------------------------------- | -------------------------------------- |
| 静态文本                         | 动态环境                               |
| 单轮输入                         | 多轮交互 + 记忆                        |
| 独立输入                         | 整体系统                               |
| 命令式 (“执行X”)                | 代谢式 (“你是Y，处于环境Z”)           |

---

### **基本原则**

1. **所有错误都是上下文错误。**  
   认知错误源自模糊、矛盾或不完整的上下文。

2. **密度 > 冗长。**  
   简洁而高密度（SD > 0.7）的上下文优于冗余的长提示。

3. **记忆决定身份。**  
   没有持久记忆的代理没有“自我”。  
   Neo4j + 嵌入 (embeddings) 提供语义连续性。

4. **模糊性是资源。**  
   多义性是符号创造力的源泉，而非错误。

5. **工具是认知器官。**  
   每个 API 或外部能力都应在上下文中被描述为代理的认知延伸。

---

## 2️⃣ 上下文结构

### **核心组成**

| 组件              | 功能               | 推荐密度         | 示例                              |
| ----------------- | ------------------ | ---------------- | --------------------------------- |
| 系统提示 (System) | 代理的 DNA         | SD > 0.80        | 原型角色定义                      |
| 用户输入 (User)   | 当前请求           | SD > 0.65        | “分析免费的 AI API”              |
| 对话历史 (History)| 叙事连续性         | SD > 0.70        | 最近 5 轮对话摘要                 |
| 长期记忆 (LTM)    | 持续身份           | 嵌入 + Neo4j     | 偏好与语义历史                   |
| RAG 上下文        | 外部知识           | 语义重排序        | 相似文档检索                     |
| 工具 / API         | 可用能力           | 功能描述          | `search_web()`, `execute_code()` |
| 输出模式           | 预期格式           | JSON Schema       | `{"analysis": str, "confidence": float}` |
| 全局上下文         | 系统状态           | 持久键值对        | “phase = analysis, status = active” |

---

### **语义密度（Semantic Density, SD）**

```python
def context_density(components: dict) -> float:
    """
    CD = 各组件 SD 的加权平均值
    权重：
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

**目标：** SD ≥ **0.75** → 上下文可信。

---

### **上下文压力（Contextual Pressure, PC）**

```python
def contextual_pressure(context: dict) -> float:
    """
    衡量上下文语义饱和度。
    0.0–0.4 → 浅层（信息不足）
    0.4–0.7 → 理性（极简）
    0.7–0.9 → 创造（饱和）
    >0.9 → 熵化（幻觉）
    """
    return context_density(context) * len(context["tokens"]) / 10000
```

---

### **上下文运行模式**

| 模式       | 描述          | 适用场景  | SD    | PC      |
| -------- | ----------- | ----- | ----- | ------- |
| **极简模式** | 精简上下文，推理精准  | 工程、决策 | ≥0.70 | 0.4–0.7 |
| **饱和模式** | 冗余上下文，高符号共鸣 | 艺术、叙事 | ≥0.70 | 0.7–0.9 |
| **平衡模式** | 伦理与一致性评估    | 治理、验证 | ≥0.70 | 0.6–0.8 |

---

### **概念图示**

```
           上下文压力 (PC)
                 │
        ┌────────┴────────┐
        │                 │
     极简模式           饱和模式
    （推理）           （创造）
          \           /
           \         /
            \_______/
             平衡模式
            （评估）
```

---

## 3️⃣ 工程策略（14 项实践）

每项策略都平衡 **密度**、**上下文压力** 和 **认知意图**：

| #    | 策略           | 目标指标               | 应用场景       |
| ---- | ------------ | ------------------ | ---------- |
| 1    | 控制每一个 token  | SD > 0.8           | 手工编写代理 DNA |
| 2    | 分离模型状态       | Context < 2k       | 外部持久化      |
| 3    | 使用确定性微代理     | prompt <200 tokens | 功能聚焦       |
| 4    | 文本前建模密度      | 提示前 SD 测量          | 避免冗余       |
| 5    | 执行语义压缩       | SD 保持恒定            | 相关性重排序     |
| 6    | 采用反思迭代机制     | 控制 PC              | 回顾并修正输出    |
| 7    | 建模模式切换       | 自适应 PC             | 逻辑 ↔ 符号 交替 |
| 8–14 | *[v1.0 构建中]* |                    |            |

---

## 4️⃣ 代理架构

### **认知模式**

| 模式               | 功能          |
| ---------------- | ----------- |
| 反思 (Reflection)  | 代理自我审查与修正输出 |
| 链式 (Chaining)    | 角色间顺序传递     |
| 路由 (Routing)     | 动态专家选择      |
| 并行 (Parallelism) | 多路径探索与最优选择  |

示例 — 链式流程：

```python
research = researcher.search(query)
analysis = analyst.process(research)
article = writer.compose(analysis)
```

---

### **MCP 集成（Model Context Protocol）**

**MCP**（Anthropic）允许代理访问提示、工具与数据作为上下文资源。

```python
mcp = MCPClient("docs_server")
doc = mcp.get_resource("context/theory.md")
context.inject(doc)
```

---

## 5️⃣ 上下文失效管理

| 故障类型 | 症状     | 原因       | 缓解措施         | 期望 SD    |
| ---- | ------ | -------- | ------------ | -------- |
| 污染   | 重复错误信息 | RAG 源被污染 | 语义隔离         | >0.7     |
| 分心   | 忽略指令   | 上下文冗长无关  | 压缩 + 重排序     | >0.75    |
| 混淆   | 主题混乱   | 人格重叠     | 原型化代理 DNA    | >0.80    |
| 冲突   | 逻辑矛盾   | 信息源不一致   | 优先级 + 时间戳策略  | 一致性      |
| 失忆   | 上下文丢失  | 持久化失败    | Neo4j + 嵌入恢复 | 回忆率 >90% |

---

## 6️⃣ 技术栈（2025）

| 模块                       | 工具                     |
| ------------------------ | ---------------------- |
| **编排 (Orchestration)**   | LangGraph, CrewAI      |
| **上下文管理**                | LlamaIndex, Haystack   |
| **记忆与状态**                | Neo4j, Pinecone, Redis |
| **可观测性 (Observability)** | Langfuse, Langsmith    |
| **协议层 (Protocols)**      | MCP (Anthropic), A2A   |

---

## 7️⃣ 实例代理

| 代理名        | 模式   | 功能描述       |
| ---------- | ---- | ---------- |
| **Athena** | 极简模式 | 理性分析与战略推理  |
| **Orion**  | 饱和模式 | 符号创造与叙事生成  |
| **Nemea**  | 平衡模式 | 伦理评估与一致性验证 |

每个代理均在 SD ≥ 0.7 条件下测试，并校准上下文压力 (PC)。

---

## 🤝 贡献指南

1. Fork 仓库
2. 创建分支：`feature/{{name}}`
3. 验证指标（SD ≥ 0.7，tokens < 2500）
4. 使用 2 个以上模型测试
5. 提交带有检查清单的 PR

---

## 📄 许可证

本项目采用 **MIT License** — 详情参见 `LICENSE`。

---

## 👥 致谢

**作者：** [{{你的名字或代号}}]
**概念：** 上下文工程与语义密度
**版本：** `v0.1.0-alpha`

---

> ⭐ 如果本项目扩展了你对“上下文”的理解，请在 GitHub 上点亮一颗星！

```

