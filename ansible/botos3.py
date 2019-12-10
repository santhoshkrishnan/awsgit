import boto3
#s3 = boto3.client('s3',region_name='ap-southeast-1')
#s3.create_bucket(Bucket='my-bucket-qwqw007sant0007us')
#import boto3
ec2 = boto3.resource('ec2')
# create VPC
vpc = ec2.create_vpc(CidrBlock='172.16.0.0/16',region_name='ap-southeast-1')
# assign a name to our VPC
vpc.create_tags(Tags=[{"Key": "Name", "Value": "my_vpc"}])
vpc.wait_until_available()

