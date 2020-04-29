provider "azurerm" {
  version = "~>2.0"
  features {}
}

terraform {
  backend "local" {}
}
