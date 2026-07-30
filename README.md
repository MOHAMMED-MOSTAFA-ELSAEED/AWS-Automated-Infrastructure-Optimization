# 🚀 AWS Automated Infrastructure Provisioning & Cost Optimization Engine

[![AWS](https://img.shields.io/badge/AWS-VPC%20%7C%20EC2%20%7C%20S3%20%7C%20IAM-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-Boto3%20SDK-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Security](https://img.shields.io/badge/Security-IAM%20Role%20Driven-success?style=for-the-badge)](https://aws.amazon.com/iam/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

> An automated, production-grade cloud solution designed to provision multi-tier isolated network infrastructure on AWS, run programmatic resource audits, detect cost waste (orphaned resources), and export centralized reports to Amazon S3 using Python and IAM Role-based security.

---

## 📐 Architecture Overview

The system provisions a secure, multi-tier cloud environment and executes an automated audit pipeline leveraging natively attached IAM Instance Profiles for zero-credential security.

```mermaid
graph TD
    subgraph AWS Cloud [us-east-1]
        subgraph VPC [Prod-VPC: 10.0.0.0/16]
            IGW[Internet Gateway]
            subgraph Public_Subnet [Public Subnet: 10.0.1.0/24]
                EC2[EC2 Instance / Linux]
                SG[Security Group: Port 22 SSH]
            end
            subgraph Private_Subnet [Private Subnet: 10.0.2.0/24]
            end
        end
        
        IAM[IAM Role: S3 & EC2 Read]
        S3[(S3 Bucket: Audit Central Storage)]
    end

    IGW <--> Public_Subnet
    EC2 <--> SG
    IAM -.->|Assigned Instance Profile| EC2
    EC2 -->|Python Boto3 Audit| S3
