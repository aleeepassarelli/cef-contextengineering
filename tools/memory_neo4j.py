"""
tools/memory_neo4j.py
----------------------

Módulo de Memória Semântica para o Context Engineering Framework (CEF).

Integração com Neo4j para armazenar:
    - Contextos anteriores
    - Relações semânticas entre tokens, ideias e agentes
    - Histórico e identidade cognitiva do sistema

Objetivo:
    Garantir persistência de coerência e continuidade semântica
    em fluxos cognitivos de longo prazo.

Requisitos:
    pip install neo4j
"""

from typing import Dict, List, Any, Tuple
from neo4j import GraphDatabase
import json
import uuid
from core.context_metrics import calculate_sd

# ------------------------------------------------------------------------
# ⚙️ Classe Principal
# ------------------------------------------------------------------------

class MemoryNeo4j:
    """
    Interface de Memória Semântica baseada em Grafo (Neo4j).
    Cada nó representa um conceito, contexto ou agente.
    """

    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # --------------------------------------------------------------------
    # 🧩 Operações de Escrita
    # --------------------------------------------------------------------

    def store_context(self, agent_name: str, context: Dict[str, Any]) -> str:
        """
        Armazena um contexto completo na memória semântica.

        Args:
            agent_name (str): Nome do agente.
            context (Dict[str, Any]): Estrutura contextual (system, user, rag, etc.)

        Returns:
            str: ID único do nó criado.
        """
        context_id = str(uuid.uuid4())
        sd_value = calculate_sd(str(context))

        with self.driver.session() as session:
            session.run(
                """
                CREATE (c:Context {
                    id: $id,
                    agent: $agent,
                    system: $system,
                    user: $user,
                    sd: $sd,
                    rag: $rag,
                    tokens: $tokens,
                    created_at: datetime()
                })
                """,
                id=context_id,
                agent=agent_name,
                system=context.get("system", ""),
                user=context.get("user", ""),
                rag=json.dumps(context.get("rag", [])),
                tokens=len(context.get("tokens", [])),
                sd=sd_value,
            )
        return context_id

    # --------------------------------------------------------------------
    # 🔍 Recuperação de Memória
    # --------------------------------------------------------------------

    def recall_recent_contexts(self, agent_name: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Recupera os últimos contextos de um agente.

        Args:
            agent_name (str): Nome do agente.
            limit (int): Quantos contextos retornar.

        Returns:
            List[Dict[str, Any]]: Lista de contextos recentes.
        """
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (c:Context {agent: $agent})
                RETURN c ORDER BY c.created_at DESC LIMIT $limit
                """,
                agent=agent_name,
                limit=limit
            )
            return [dict(r["c"]) for r in result]

    # --------------------------------------------------------------------
    # 🔗 Relações Semânticas
    # --------------------------------------------------------------------

    def link_contexts(self, id_a: str, id_b: str, rel_type: str = "RELATED_TO"):
        """
        Cria uma relação semântica entre dois contextos.

        Args:
            id_a (str): ID do contexto origem.
            id_b (str): ID do contexto destino.
            rel_type (str): Tipo de relação semântica.
        """
        with self.driver.session() as session:
            session.run(
                f"""
                MATCH (a:Context {{id: $a}}), (b:Context {{id: $b}})
                MERGE (a)-[r:{rel_type}]->(b)
                SET r.created_at = datetime()
                """,
                a=id_a,
                b=id_b,
            )

    # --------------------------------------------------------------------
    # 🧬 Consulta Semântica
    # --------------------------------------------------------------------

    def query_semantic_links(self, concept: str, limit: int = 5) -> List[Tuple[str, float]]:
        """
        Busca contextos semanticamente conectados a um conceito textual.

        Args:
            concept (str): Palavra ou ideia-chave.
            limit (int): Máximo de resultados.

        Returns:
            List[Tuple[str, float]]: Lista de contextos e SD estimada.
        """
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (c:Context)
                WHERE c.system CONTAINS $concept OR c.user CONTAINS $concept
                RETURN c.id AS id, c.sd AS sd
                ORDER BY c.sd DESC LIMIT $limit
                """,
                concept=concept
            )
            return [(r["id"], r["sd"]) for r in result]


# ------------------------------------------------------------------------
# 🧪 Teste Local
# ------------------------------------------------------------------------

if __name__ == "__main__":
    # Exemplo de inicialização
    mem = MemoryNeo4j("bolt://localhost:7687", "neo4j", "password")

    # Criar e armazenar contexto
    ctx = {
        "system": "Agente de teste de memória semântica",
        "user": "Descreva o papel da memória no raciocínio contextual.",
        "tokens": ["memória", "contexto", "agente"],
        "rag": ["A memória conecta percepções ao longo do tempo."]
    }

    print("💾 Armazenando contexto...")
    cid = mem.store_context("Athena", ctx)
    print("🆔 Contexto salvo com ID:", cid)

    # Recuperar histórico
    print("\n📜 Últimos contextos:")
    for c in mem.recall_recent_contexts("Athena"):
        print(c["id"], c["system"][:50])

    mem.close()
