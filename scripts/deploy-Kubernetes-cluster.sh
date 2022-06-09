#git clone https://github.com/meuriC/CN22_Group2.git

echo "--Creating Kubernetes Cluster--" 
gcloud container clusters create cluster-steam --zone europe-west1-b --cluster-version 1.21.12-gke.1700 --release-channel rapid --num-nodes=3

sleep 1m

echo "--Connecting to Kubernetes Cluster--" 
gcloud container clusters get-credentials cluster-steam --zone europe-west1-b

echo "--Moving to Deployment folder--" 
cd deployment

echo "--Deploying Services--" 
kubectl apply -f services-deploy.yaml

sleep 5m

echo "--Deploying Ingress--" 
kubectl apply -f ingress-deploy.yaml 

#echo "--Deploying Ingress--" 
#kubectl apply -f ingress-steam.yaml 
