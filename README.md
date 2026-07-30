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
    %% Define Styles and Colors
    classDef awsStyle fill:#232F3E,stroke:#FF9900,stroke-width:2px,color:#FFFFFF,font-weight:bold;
    classDef vpcStyle fill:#001E2B,stroke:#00A4E4,stroke-width:2px,color:#FFFFFF,font-weight:bold;
    classDef pubSubnetStyle fill:#0A2F1D,stroke:#3B82F6,stroke-width:1.5px,color:#FFFFFF;
    classDef privSubnetStyle fill:#1F2937,stroke:#6B7280,stroke-width:1.5px,stroke-dasharray: 5 5,color:#9CA3AF;
    classDef ec2Style fill:#FF9900,stroke:#232F3E,stroke-width:2px,color:#000000,font-weight:bold;
    classDef s3Style fill:#569A31,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF,font-weight:bold;
    classDef iamStyle fill:#DD344C,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF,font-weight:bold;
    classDef netStyle fill:#161E2E,stroke:#00A4E4,stroke-width:1px,color:#FFFFFF;

    subgraph AWS_Cloud ["☁️ AWS Cloud Region (us-east-1)"]
        subgraph VPC ["🌐 Prod-VPC (10.0.0.0/16)"]
            IGW["🌐 Internet Gateway (IGW)"]
            
            subgraph Public_Subnet ["🔓 Public Subnet (10.0.1.0/24)"]
                EC2["🖥️ EC2 Instance (Linux)"]
                SG["🛡️ Security Group (SSH :22)"]
            end
            
            subgraph Private_Subnet ["🔒 Private Subnet (10.0.2.0/24)"]
                PRIV_EMPTY["📦 Reserved for Isolated Workloads"]
            end
        end
        
        IAM["🔑 IAM Role (S3 & EC2 Read)"]
        S3[("🪣 S3 Bucket (Audit Central Storage)")]
    end

    %% Flow Connections
    IGW <===>|"🌍 Public Traffic"| Public_Subnet
    EC2 <--->|"🔒 Protected By"| SG
    IAM -.->|"🛡️ Attached Instance Profile"| EC2
    EC2 ==>|"📊 Automated Python Boto3 Report"| S3

    %% Assign Classes to Elements
    class AWS_Cloud awsStyle;
    class VPC vpcStyle;
    class Public_Subnet pubSubnetStyle;
    class Private_Subnet privSubnetStyle;
    class EC2 ec2Style;
    class S3 s3Style;
    class IAM iamStyle;
    class IGW,SG,PRIV_EMPTY netStyle;

## 🔥 Key Technical Highlights

* **Isolated Network Architecture:** Fully automated setup of custom **VPC**, **Public/Private Subnets**, **Internet Gateway**, and **Route Tables** for structured ingress/egress management.
* **IAM Role Security (Zero Hardcoded Keys):** Utilizes **AWS IAM Instance Profiles** attached directly to EC2. Eliminates hardcoded `AWS_ACCESS_KEY` or secret credentials inside scripts, following the **Principle of Least Privilege**.
* **Automated Cost Optimization:** Features a **Python (Boto3)** script that queries the AWS API to identify running EC2 instances and detect orphaned/unattached **EBS Volumes** running up costs unnecessarily.
* **Centralized Storage Pipeline:** Audit logs and JSON reports are generated dynamically and securely pushed to a dedicated **Amazon S3 Bucket**.
