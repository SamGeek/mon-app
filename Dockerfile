# On utilise une image légère
FROM python:3.9-slim

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie le fichier des dépendances et on les installe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie le reste du code
COPY app.py .

# On expose le port 8000 (celui de Flask)
EXPOSE 8000

# On lance l'application
CMD ["python", "app.py"]