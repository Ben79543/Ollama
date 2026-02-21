# Utilise une image de base légère avec support GPU si nécessaire
FROM ubuntu:22.04

# Installe les dépendances
RUN apt-get update && \
    apt-get install -y curl wget git && \
    rm -rf /var/lib/apt/lists/*

# Télécharge et installe Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Pull the Mistral model during the build process
RUN ollama pull mistral

# Expose le port par défaut d'Ollama (11434)
EXPOSE 11434

# Lance Ollama au démarrage du conteneur
CMD ["ollama", "serve"]
