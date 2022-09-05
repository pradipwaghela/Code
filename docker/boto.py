import boto3
#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIA44CV5NVM7SEOITVP',
aws_secret_access_key='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'
)
#Creating S3 Resource From the Session.
s3 = session.resource('s3')
object = s3.Object('lets-test-this-loki', 'file_name.txt')
txt_data = b'This is the content of the file uploaded from python boto3'
result = object.put(Body=txt_data)
res = result.get('ResponseMetadata')
if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')