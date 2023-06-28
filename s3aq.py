import boto3

session = boto3.Session(
    aws_access_key_id='AKIAUFPGOSDGEZLCJR6G',
    aws_secret_access_key='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',
)
s3 = session.resource('s3')
# Filename - File to upload
# Bucket - Bucket to upload to (the top level directory under AWS S3)
# Key - S3 object name (can contain subdirectories). If not specified then file_name is used
s3.meta.client.upload_file(Filename=r'C:\Users\91842\PycharmProjects\AMQ1\output.xml', Bucket='activemqoutput', Key='output.xml')