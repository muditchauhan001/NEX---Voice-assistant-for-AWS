import boto3
from botocore.exceptions import ClientError

class AWSServices:
    def __init__(self, region_name):
        self.region_name = region_name
        self.ec2_client = boto3.client('ec2', region_name=self.region_name)
        print("AWS Region:", self.region_name)
        print("EC2 Endpoint URL:", self.ec2_client._endpoint.host)

    def create_ec2_instance(self, image_id="ami-04e5276ebb8451442", instance_type="t2.micro", key_name="EC2 Tutorial"):
        response = self.ec2_client.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MinCount=1,
            MaxCount=1
        )
        instance_id = response['Instances'][0]['InstanceId']
        print("EC2 instance created with ID:", instance_id)


