import boto3
ec2 = boto3.resource('ec2')

#code to create a new key pair
# outfile = open('ec2-keypair.pem','w')
# key = ec2.create_key_pair(KeyName = 'aws-keypair')

# KeyPairOut = str(key.key_material)
# outfile.write(KeyPairOut)


# create an instance with security group 'csc326-group39'
instances = ec2.create_instances(
     ImageId='ami-0ac019f4fcb7cb7e6',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='aws-keypair',
     SecurityGroupIds=[
            'sg-0d0466ff829eda700',
    ]
 )

