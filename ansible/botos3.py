import boto3
s3 = boto3.client('s3',region_name='us-east-1')
s3.create_bucket(Bucket='my-bucket-qwqw007sant0007us')
#import boto3
#ec2 = boto3.resource('ec2')
# create VPC
#vpc = ec2.create_vpc(CidrBlock='10.30.0.0/24')
# assign a name to our VPC
#vpc.create_tags(Tags=[{"Key": "Name", "Value": "my_vpc2"}])
#vpc.wait_until_available()

