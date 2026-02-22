# Image minimale Ubuntu LTS
FROM ubuntu:22.04

# Variables d'environnement
ENV DEBIAN_FRONTEND=noninteractive \
    OLLAMA_HOST=0.0.0.0 \
    PATH="/usr/local/bin:${PATH}"

# Création d’un utilisateur non-root dédié
ARG APP_UID=10001
ARG APP_GID=10001

RUN groupadd -g ${APP_GID} ollama && \
    useradd -m -u ${APP_UID} -g ollama -s /usr/sbin/nologin ollama

# Installation minimale des dépendances
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        zstd \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Installation d’Ollama
RUN curl -fsSL https://ollama.com/install.sh -o /tmp/install.sh && \
    chmod +x /tmp/install.sh && \
    /tmp/install.sh && \
    rm /tmp/install.sh

# Création du dossier de travail
WORKDIR /home/ollama

# Attribution des permissions strictes
RUN chown -R ollama:ollama /home/ollama

# Passage en utilisateur non-root
USER ${APP_UID}:${APP_GID}

# Port exposé
EXPOSE 11434

# Commande par défaut
CMD ["ollama", "serve"]