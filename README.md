Particle41 DevOps Challenge Submission

Access the Application
	• Click here to access the SimpleTimeService 
http://aca1c0b74b4b94033b62f40d01de3de4-2060421100.ap-south-1.elb.amazonaws.com/ 

Pull the image from Docker Hub repository
	• docker pull amandevopsio/particle41:latest
	
Overview
This project demonstrates a comprehensive DevOps workflow, showcasing:
	• 🚀 Development of a minimal Python web service
	• 🐳 Containerization using Docker
	• ☁️ Cloud deployment on AWS EKS using Terraform
	• 🌐 Internet-accessible application via AWS Elastic Load Balancer
Table of Contents
	• Prerequisites
	• Application Overview
	• Repository Structure
	• Local Development
	• Deployment Instructions
	• Accessing the Application
	• Cleanup
	• Troubleshooting
Prerequisites
Required Tools
	• Docker 🐳
		○ Installation Guide
		○ Verify: docker --version
	• Terraform 🏗
		○ Installation Guide
		○ Verify: terraform --version
	• AWS CLI ☁️
		○ Installation Guide
		○ Configure credentials: aws configure
	• kubectl 🧩
		○ Installation Guide
		○ Verify: kubectl version --client
AWS Requirements
	• AWS Account
	• IAM User with sufficient permissions for:
		○ EKS Cluster creation
		○ VPC management
		○ Load Balancer configuration (Load balancer deployed as service)
Application Overview
SimpleTimeService
A minimalist Python Flask web service that provides:
	• Endpoint: /
	• Response Format: JSON
	• Includes current timestamp and client IP address
Example Response
{
  "timestamp": "2023-10-05T12:34:56.789Z",
  "ip": "::ffff:10.0.1.5"
}
Repository Structure
.
├── app/
│   ├── app.py              # Main application code
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Docker container definition
├── Kubernetes/
│   ├── deployment.yml      # Kubernetes Deployment manifest
│   ├── service.yml         # Kubernetes Service manifest
└── Terraform/
    ├── main.tf             # Primary Terraform configuration
    ├── variables.tf        # Input variables
    ├── terraform.tfstate   # Terraform state file
    ├── terraform.tfstate.backup # Backup state file
Local Development
Build Docker Image
# Navigate to app directory
cd app
# Build Docker image
docker build -t simpletimeservice .
# Run container
docker run -d -p 3000:3000 --name simpletimeservice simpletimeservice
# Test application
curl http://localhost:3000/

Deployment Instructions

Kubernetes Deployment
# Navigate to Kubernetes directory
cd Kubernetes
# Apply deployment and service config file
kubectl apply -f deployment.yml
kubectl apply -f service.yml
Terraform Deployment
# Navigate to terraform directory
cd Terraform
# Initialize Terraform
terraform init
# Review execution plan
terraform plan
# Apply configuration
terraform apply
# Type 'yes' when prompted

Accessing the Application
After deployment:
# Access via curl
DNS: http://aca1c0b74b4b94033b62f40d01de3de4-2060421100.ap-south-1.elb.amazonaws.com/ 

Cleanup
To avoid unnecessary AWS charges:
# Navigate to terraform directory
cd Terraform
# Destroy infrastructure
terraform destroy
# Type 'yes' when prompted

Troubleshooting
Common Issues
	• Docker Build Failures:
		○ Ensure Docker daemon is running
		○ Check network connectivity
		○ Verify Dockerfile syntax
	• Terraform Deployment Errors:
		○ Confirm AWS credentials are correctly configured
		○ Ensure sufficient IAM permissions
		○ Check AWS region settings
	• Kubernetes Connectivity:
		○ Verify kubectl is configured
		○ Check cluster status: kubectl cluster-info

This document serves as a complete DevOps guide for deploying the SimpleTimeService Python application using Docker, Kubernetes, and Terraform.
![image](https://github.com/user-attachments/assets/9780c939-732e-4299-b17e-931c7522a1b8)
