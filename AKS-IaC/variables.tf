variable "resource_group_name" {
  default = "rg-aks-demo"
}

variable "location" {
  default = "East US"
}

variable "aks_name" {
  default = "demo-aks-cluster"
}

variable "node_vm_size" {
  default = "Standard_DS2_v2"
}

variable "node_count" {
  default = 1
}
