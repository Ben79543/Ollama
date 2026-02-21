# Configuration globale pour les agents
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

# Clés API ou autres paramètres sensibles (à externaliser dans un .env en production)
API_KEYS = {
    "ollama": None  # Pas besoin pour une instance locale d'Ollama
}
