# Image d'exécution. Aucun secret en ARG ni en ENV : la configuration arrive à l'exécution.
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

# Utilisateur sans privilèges
RUN useradd --create-home --uid 1000 meetroom && mkdir /data && chown meetroom /data
USER meetroom
ENV MEETROOM_DB=/data/meetroom.db

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
