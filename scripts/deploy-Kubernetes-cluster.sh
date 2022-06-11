echo -e "\n--Creating Kubernetes Cluster--" 
gcloud container clusters create cluster-steam --zone europe-west1-b --cluster-version 1.21.12-gke.1700 --release-channel rapid --num-nodes=3

sleep 10s
echo -e "\n--Create a global static IP address--"
gcloud compute addresses create steam-reviews-ip --global

echo -e "\n--Find the static IP address you created--"
gcloud compute addresses describe steam-reviews-ip --global

sleep 10s
echo -e "\n--Connecting to Kubernetes Cluster--" 
gcloud container clusters get-credentials cluster-steam --zone europe-west1-b
helm repo add bitnami https://charts.bitnami.com/bitnami

cd ../deployment
helm install "steamreviews-externaldns" --values gcp-external-dns.values.yaml bitnami/external-dns

echo -e "\n--Deploying Services--" 
kubectl apply -f services-deploy.yaml

sleep 10s
echo -e "\n--Deploying Ingress--" 
kubectl apply -f ingress-deploy.yaml 

echo "This might take a while. Wait a few minutes..."
sleep 1.5m

echo -e "\n--Deploying Ingress--" 
kubectl apply -f ingress-steam.yaml 

echo -e "\nLink --> https://console.cloud.google.com/marketplace/product/google/prometheus"
echo -e "On another tab go to the marketplace search for 'prometheus & grafana' or use the link above -> configure -> deploy -> AFTER completion -> Press enter"
read -p "Press enter to continue"

echo -e "\n--Deploying Prometheus and Grafana"
cd ../scripts
bash prometheus_grafana.sh

echo -e "\n--Configuring domain name records--"
gcloud dns --project=cloud-computing-345718 managed-zones create steam-reviews-zone --description="" --dns-name="steamreviews.sytes.net." --visibility="public" --dnssec-state="off"

echo -e "\n--See the reserve IP address associated with the load balancer--"
kubectl get ingress

echo -e "\nTo access our API click on this link --> http://steamreviews.sytes.net./ui/"
