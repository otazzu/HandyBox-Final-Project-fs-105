#!/usr/bin/env bash
# exit on error
set -o errexit

# Construir el frontend
npm install --prefix ./src
npm run build --prefix ./src

# Instalar pipenv
pip install pipenv

# Instalar dependencias con pipenv
pipenv install

# Ejecutar migraciones
pipenv run python app.py db upgrade