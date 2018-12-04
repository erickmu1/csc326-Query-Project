import boto3
import urllib.request
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2',
                 aws_access_key_id = 'AKIAJUHTJVF55A6B3TYA',
                 aws_secret_access_key='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',
                 region_name ='us-east-1')
client = boto3.client('ec2')


instance_running = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

instanceID = input ("Enter instance ID to be terminated: ")

print("\nTerminating instance...")
        
instance_list = []

for instance in instance_running:
    instance_list.append(instance.instance_id)


if (len(instance_list) > 0 and instance_list[0] == instanceID):
        try:
                response = client.terminate_instances(InstanceIds=instance_list)
                print(response)
                print ("\nInstance termination complete!")

        except ClientError as e:
                print(e)
else:
        print ("Error: instance ID does not exist!")



