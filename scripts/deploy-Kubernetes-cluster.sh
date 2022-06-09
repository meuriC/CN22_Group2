echo "--Creating Kubernetes Cluster--" 
gcloud container clusters create cluster-steam --zone europe-west1-b --cluster-version 1.21.12-gke.1700 --release-channel rapid --num-nodes=3

sleep 10s

echo "--Connecting to Kubernetes Cluster--" 
gcloud container clusters get-credentials cluster-steam --zone europe-west1-b
cd ../deployment

echo "--Deploying Services--" 
kubectl apply -f services-deploy.yaml

sleep 10s

echo "--Deploying Ingress--" 
kubectl apply -f ingress-deploy.yaml 

echo "This might take a while. Wait a few minutes..."
sleep 1.5m

echo "--Deploying Ingress--" 
kubectl apply -f ingress-steam.yaml 

echo "\nOn another tab go to the marketplace search for 'prometheus & grafana' -> configure -> deploy -> AFTER completion -> Press enter"
read -p "Press enter to continue"

echo "--Deploying Prometheus and Grafana"
cd ../scripts
bash prometheus_grafana.sh
