import boto3
from datetime import datetime, timedelta, timezone
from moto import mock_aws
from lambda_function import lambda_handler


@mock_aws
def run_local_simulation():
    print("Initializing Fake Cloud Environment...")

    # 1. Connect to our fake AWS setup
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    ec2_resource = boto3.resource('ec2', region_name='us-east-1')

    # 2. Create an AMI (Operating System image) required to launch fake instances
    ami_response = ec2_client.describe_images()
    image_id = ami_response['Images'][0]['ImageId'] if 'Images' in ami_response and ami_response['Images'] else 'ami-12345678'

    # 3. Create Server A: Has Backup=True tag (Should be backed up!)
    server_target = ec2_resource.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Backup', 'Value': 'True'}, {'Key': 'Name', 'Value': 'Production-DB'}]
        }]
    )[0]

    # 4. Create Server B: Missing the tag (Should be ignored!)
    server_ignored = ec2_resource.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'Testing-Sandbox'}]
        }]
    )[0]

    # 5. Create a fake EXPIRED snapshot (Simulating a snapshot created 10 days ago)
    # NOTE: Moto does not support backdating a snapshot's StartTime, so we cannot
    # set the creation time to 10 days ago directly. Instead, the Lambda function
    # detects this snapshot by its Name tag ('CloudGuardian-Backup-OldData') and
    # treats it as expired. This is the correct workaround for local moto testing.
    dummy_volume = ec2_client.create_volume(AvailabilityZone='us-east-1a', Size=10)
    vol_id = dummy_volume['VolumeId']

    expired_snapshot = ec2_client.create_snapshot(
        VolumeId=vol_id,
        Description="Old backup",
        TagSpecifications=[{
            'ResourceType': 'snapshot',
            'Tags': [
                {'Key': 'CreatedBy', 'Value': 'CloudGuardian-Automation'},
                {'Key': 'Name', 'Value': 'CloudGuardian-Backup-OldData'}
            ]
        }]
    )

    print("Fake cloud environment successfully configured.")
    print(f"  -> Simulated Server to Backup : {server_target.id} (Production-DB)")
    print(f"  -> Simulated Server to Ignore : {server_ignored.id} (Testing-Sandbox)")
    print(f"  -> Simulated Expired Snapshot : {expired_snapshot['SnapshotId']} (10 days old)\n")

    # 6. Run our actual Lambda function inside the mock cloud environment
    lambda_handler(event={}, context=None)


if __name__ == '__main__':
    run_local_simulation()