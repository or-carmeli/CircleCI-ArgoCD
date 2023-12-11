output "vpc_id" {
  description = "The ID of the VPC"
  value       = module.vpc.vpc_id
}

output "private_subnet_ids" {
  description = "List of IDs of private subnets"
  value       = module.vpc.private_subnets
}

output "public_subnet_ids" {
  description = "List of IDs of public subnets"
  value       = module.vpc.public_subnets
}

output "eks_security_group_id" {
  description = "The ID of the security group used by the EKS cluster"
  value       = aws_security_group.eks_security_group.id
}

output "cluster_endpoint" {
  description = "Endpoint for EKS control plane."
  value       = module.eks.cluster_endpoint
}

output "cluster_arn" {
  description = "The ARN of the EKS cluster"
  value       = module.eks.cluster_arn
}

output "cluster_certificate_authority_data" {
  description = "The certificate authority data for the EKS cluster"
  value       = module.eks.cluster_certificate_authority_data
}

output "eks_cluster_arn" {
  description = "The Amazon Resource Name (ARN) of the EKS cluster."
  value       = module.eks.cluster_arn
}

output "eks_node_group_arn" {
  description = "The Amazon Resource Name (ARN) of the EKS node group."
  value       = aws_eks_node_group.example.arn
}

output "eks_node_group_role_name" {
  description = "The name of the IAM role used by the EKS node group."
  value       = aws_iam_role.eks_node_group.name
}

output "eks_cluster_role_arn" {
  description = "The Amazon Resource Name (ARN) of the IAM role used by the EKS cluster."
  value       = aws_iam_role.eks_cluster_role.arn
}
