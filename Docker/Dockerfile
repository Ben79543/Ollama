# Utilise une image de base légère avec support GPU si nécessaire
FROM ubuntu:22.04

# Installe les dépendances nécessaires, y compris zstd
RUN apt-get update && \
    apt-get install -y curl wget git zstd && \
    rm -rf /var/lib/apt/lists/*

# Télécharge et installe Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Expose le port par défaut d'Ollama (11434)
EXPOSE 11434


CMD ["ollama", "serve"]
