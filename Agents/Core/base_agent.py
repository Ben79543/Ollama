from abc import ABC, abstractmethod
import requests
from Config.settings import OLLAMA_API_URL, MODEL_NAME



class BaseAgent(ABC):
    """Classe de base pour tous les agents."""

    def __init__(self, name: str):
        self.name = name
        self.api_url = OLLAMA_API_URL
        self.model = MODEL_NAME

    def query_model(self, prompt: str) -> str:
        """Interroge le modèle Mistral via l'API Ollama."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(self.api_url, json=payload)
        response.raise_for_status()
        return response.json()["response"]

    @abstractmethod
    def execute(self, task: str) -> str:
        """Méthode à implémenter pour chaque agent."""
        pass
