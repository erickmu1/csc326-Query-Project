import boto3    
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
counter = 0
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance["InstanceId"])
        counter = counter +1

print(counter)