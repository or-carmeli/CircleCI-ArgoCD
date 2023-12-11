variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "key_name" {
  description = "The key pair name for the EC2 instances."
  type        = string
  default     = "KeysForMachines"
}
