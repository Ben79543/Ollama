from core.base_agent import BaseAgent
from config.settings import RAG_DOCUMENTS_PATH

class RagAgent(BaseAgent):
    """Agent spécialisé dans le RAG (Retrieval-Augmented Generation)."""

    def __init__(self):
        super().__init__(name="rag_agent")
        self.documents_path = RAG_DOCUMENTS_PATH

    def retrieve_documents(self, query: str) -> str:
        """Simule la récupération de documents pertinents (à implémenter)."""
        # Ici, vous implémenteriez une logique pour récupérer des documents
        # en fonction de la requête (par exemple, avec FAISS ou ChromaDB).
        return f"Documents pertinents pour: {query}"

    def execute(self, task: str) -> str:
        """Exécute une tâche en utilisant le RAG."""
        documents = self.retrieve_documents(task)
        prompt = f"""
        Tu es un assistant utilisant le RAG. Voici des documents pertinents:
        {documents}

        Réponds à la question suivante en t'appuyant sur ces documents:
        {task}
        """
        return self.query_model(prompt)
