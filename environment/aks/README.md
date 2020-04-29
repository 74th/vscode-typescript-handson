# AKS

## Prepare

https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest

```
az ad sp create-for-rbac --name ServicePrincipalName
```

.envrc

```
export TF_VAR_client_id=<client_id>
export TF_VAR_client_secret=<client_password>
```

## Create and Destroy

```
# create
terraform init
terraform apply

# destroy
terraform destroy
```
