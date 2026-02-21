Build l'image : docker build -t mon-app:local .

Lance le conteneur : docker run -p 8000:8000 mon-app:local

Vérifie : Va sur http://localhost:8000.


git add .github/workflows/main.yml
git commit -m "Add GitHub Actions workflow"
git push origin main


settings/secrets and variables/New repository secret
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN


minikube start --driver=docker
kubectl cluster-info

# 1. Créer le namespace dédié
kubectl create namespace argocd

# 2. Installer ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml



kubectl get pods -n argocd


kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
# BwBEF3IOG8g64NqA


1. Connexion à l'interface
Si ce n'est pas déjà fait :

Lance le tunnel : kubectl port-forward svc/argocd-server -n argocd 8080:443

Va sur https://localhost:8080 (Login: admin / Password: récupéré via le secret).



5. Truc de pro : Activer l'Ingress sur Minikube
Plus tard, pour voir ton application Flask sans faire de port-forward à chaque fois, tu auras besoin de l'Ingress. Active-le déjà avec cette commande :

Bash
minikube addons enable ingress



Lance cette commande pour permettre à ArgoCD de surveiller Docker Hub :
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj-labs/argocd-image-updater/stable/config/install.yaml