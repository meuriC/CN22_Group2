echo "--Creating Kubernetes Cluster--"
{
	gcloud container clusters create cluster-steam --zone europe-west1-b --cluster-version 1.22.8-gke.200 --release-channel rapid --num-nodes=1
}
echo "--Connecting to  Kubernetes Cluster--"
{
	gcloud container clusters get-credentials cluster-steam --zone europe-west1-b
}
echo "--Moving to Deployment folder--"
{
	cd /deployment
}
echo "--Deploying Services--"
{
	kubectl apply -f services-deploy.yaml 
}
echo "--Deploying Ingress--"
{
	kubectl apply -f ingress-deploy.yaml 
}