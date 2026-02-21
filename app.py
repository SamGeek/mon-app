from flask import Flask
import os

app = Flask(__name__)

# On récupère une variable d'environnement pour afficher la version
# APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")

@app.route('/')
def hello_world():
    return f"""
    <h1>CI/CD Opérationnel v2 ! Ton app tourne sur Kubernetes 🚀</h1>
    <p>Statut : En ligne et gérée par ArgoCD.</p>
    """

if __name__ == '__main__':
    # On écoute sur toutes les interfaces (0.0.0.0) pour Docker
    app.run(host='0.0.0.0', port=8000)