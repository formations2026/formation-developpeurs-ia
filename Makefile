.PHONY: install run test check seed sandbox

install:   ## Installer les dépendances de développement
	pip install -r requirements-dev.txt

run:       ## Lancer l'API en local
	uvicorn app.main:app --reload

test:      ## Lancer les tests
	pytest

check:     ## Qualité et sécurité, comme la CI
	ruff check . && bandit -q -r app -ll && pytest

seed:      ## Remplir la base locale avec des données synthétiques
	python -m scripts.fake_data

sandbox:   ## Lancer les tests dans un conteneur sans réseau (bac à sable)
	docker run --rm --network none --user 1000:1000 -v "$$PWD":/app -w /app python:3.12-slim sh -c "echo 'Bac à sable : pas de réseau, dossier du projet uniquement' && ls"
