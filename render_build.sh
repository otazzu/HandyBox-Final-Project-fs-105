#!/usr/bin/env bash
# exit on error
set -o errexit

# Construir el frontend
npm install
npm run build

# Instalar pipenv
pip install pipenv

# Instalar dependencias con pipenv
pipenv install

# Ejecutar migraciones
pipenv run python manage.py db upgrade