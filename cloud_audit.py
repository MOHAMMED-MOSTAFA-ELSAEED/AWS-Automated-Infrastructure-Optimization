import boto3
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def audit_and_upload():
    # Initialize AWS Clients (Using IAM Role attached to EC2)
    ec2 = boto3.client('ec2', region_name='us-east-1')
    s3 = boto3.client('s3', region_name='us-east-1')
    
    # Bucket name (Update to match your specific S3 bucket)
    bucket_name = "aws-audit-reports-mohammed"
    report_file = "aws_cost_audit_report.json"
    
    report = {
        "instances": [],
        "orphaned_volumes": []
    }

    logging.info("Starting AWS Infrastructure & Cost Audit...")

    # 1. Audit EC2 Instances
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            report["instances"].append({
                "InstanceId": instance['InstanceId'],
                "State": instance['State']['Name'],
                "Type": instance['InstanceType'],
                "PublicIp": instance.get('PublicIpAddress', 'N/A')
            })

    # 2. Audit Orphaned EBS Volumes (Cost Waste Detection)
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    for volume in volumes['Volumes']:
        report["orphaned_volumes"].append({
            "VolumeId": volume['VolumeId'],
            "Size_GB": volume['Size']
        })

    # 3. Save Report Locally
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=4)
    logging.info(f"Local report generated: {report_file}")

    # 4. Upload Report to S3 Bucket
    try:
        s3.upload_file(report_file, bucket_name, report_file)
        logging.info(f"[✔] SUCCESS: Report uploaded to S3 Bucket: s3://{bucket_name}/{report_file}")
    except Exception as e:
        logging.error(f"[❌] Error uploading to S3: {e}")

if __name__ == "__main__":
    audit_and_upload()
