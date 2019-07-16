
import boto3, json

# Create IAM client
iam = boto3.client('iam')

path='/'
role_name='kishan_role'
description='Role for s3 access'

trust_policy={
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}


tags=[
    {
       'Key': 'name',
        'Value': 'kishan_policy'
    }
]

try:
    response = iam.create_role(
        Path=path,
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description=description,
        MaxSessionDuration=36000,
        Tags=tags
    )

    print(response)

except Exception as e:
    print(e)
Attach a role policy
iam.attach_role_policy(
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess',
    RoleName='kishan_role'
)
ec2= boto3.client('ec2')
try:
  response = ec2.associate_iam_instance_profile(
      IamInstanceProfile={
          'Arn': 'arn:aws:iam::488599217855:role/kishan_role',
          'Name': 'kishan_role'
      },
      InstanceId='i-06ea7da759ac79e4a'
  )
  print(response)
except Exception as e:
  print(e)
try:
  response = iam.create_instance_profile(
      InstanceProfileName='kishan_role_instance'
  )
  print(response)
except Exception as e:
  print(e)

try:
  response = iam.add_role_to_instance_profile(
      InstanceProfileName='kishan_role_instance',
      RoleName='kishan_role'
  )
  print(response)
except Exception as e:
  print(e)

try:
  response = ec2.associate_iam_instance_profile(
  IamInstanceProfile={
      'Arn': 'arn:aws:iam::488599217855:instance-profile/kishan_role_instance',
      'Name': 'kishan_role_instance'
  },
  InstanceId='i-06ea7da759ac79e4a'
  )
  print(response)
except Exception as e:
  print(e)
