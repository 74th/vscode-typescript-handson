# copy of https://docs.microsoft.com/ja-jp/azure/developer/terraform/create-k8s-cluster-with-tf-and-aks
resource "azurerm_resource_group" "k8s" {
  name     = "vscode-typescript-handson"
  location = "japaneast"
}

resource "azurerm_kubernetes_cluster" "k8s" {
  name                = "vscode-typescript-handson"
  location            = "${azurerm_resource_group.k8s.location}"
  resource_group_name = "${azurerm_resource_group.k8s.name}"
  dns_prefix          = "vscode-typescript-handson"

  default_node_pool {
    name       = "agentpool"
    node_count = "1"
    vm_size    = "Standard_A8m_v2"
  }

  service_principal {
    client_id     = "${var.client_id}"
    client_secret = "${var.client_secret}"
  }

  tags = {
    Environment = "Development"
  }
}
output "client_key" {
  value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.client_key}"
}

output "client_certificate" {
  value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.client_certificate}"
}

output "cluster_ca_certificate" {
  value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.cluster_ca_certificate}"
}

output "cluster_username" {
  value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.username}"
}

output "cluster_password" {
  value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.password}"
}

output "kube_config" {
  value = "${azurerm_kubernetes_cluster.k8s.kube_config_raw}"
}

output "host" {
  value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.host}"
}
