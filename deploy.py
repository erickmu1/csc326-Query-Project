from time import sleep
import sys 
import csv
import boto3
import urllib.request
from botocore.exceptions import ClientError

aws_access_file = input ("Enter the name of the AWS .csv file in this directory (with the extension): ")

aws_access_key_id = ""
aws_secret_access_key = ""

ip = "18.211.236.148"
alloc_id = "eipalloc-0f4559fa79c509a74"


# Used to read the AWS credentials from the .csv file 
with open(aws_access_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        row = next(csv_reader)
        aws_access_key_id = row[2]
        aws_secret_access_key = row[3]

ec2 = boto3.resource('ec2',
                 aws_access_key_id = aws_access_key_id,
                 aws_secret_access_key=aws_secret_access_key,
                 region_name ='us-east-1')
client = boto3.client('ec2')

#code to create a new key pair
# outfile = open('ec2-keypair.pem','w')
# key = ec2.create_key_pair(KeyName = 'ec2-keypair')

# KeyPairOut = str(key.key_material)
# outfile.write(KeyPairOut)


# create an UBUNTU instance with security group 'csc326-group39'()
print ("Creating new instance...")

new_instance = ec2.create_instances(
     ImageId='ami-0ac019f4fcb7cb7e6',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='ec2-keypair',
     SecurityGroupIds=[
            'sg-0d0466ff829eda700',
    ]
 )

new_instance[0].wait_until_running()

print ("Done!\n")

# Database to hold all the running instances
instanceID_list = []

instance_running = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Iterate through all of the running instances and adding them to database
for instance in instance_running:
        if len(instanceID_list) == 0:
                instanceID_list.append(instance.instance_id)
        else:
                # Have just one instance running for now. Additional instances for future implementation
                print ("An instance is already running")
try:
        # Attach elastic IP to instance
        response = client.associate_address(AllocationId=alloc_id,
                                InstanceId=instanceID_list[0])
                                
        print(response)

        # Have a .csv that keeps track of all running instances with their IP and Allocation ID
        with open('current_instances.csv', mode='w', newline = '') as current_instances:
                instance_writer = csv.writer(current_instances, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                instance_writer.writerow(['Instance ID', 'IP Address', 'Allocation ID'])
                instance_writer.writerow([instanceID_list[0], ip, alloc_id])

except ClientError as e:
        print(e)
