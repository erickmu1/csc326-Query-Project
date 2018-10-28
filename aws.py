import boto3
ec2 = boto3.resource('ec2')

# outfile = open('ec2-keypair.pem','w')
# key = ec2.create_key_pair(KeyName = 'aws-keypair')

# KeyPairOut = str(key.key_material)
# print(KeyPairOut)
# outfile.write(KeyPairOut)

# create a new EC2 instance


instances = ec2.create_instances(
     ImageId='ami-0922553b7b0369273',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='aws-keypair',
     SecurityGroupIds=[
            'sg-0d0466ff829eda700',
    ]
 )

