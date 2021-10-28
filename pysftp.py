import pysftp
import boto3

# get clients
s3_gl = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

# parameters
bucket_gl = ''
gl_data = ''
gl_script = ''

source_response = s3_gl.get_object(Bucket=bucket_gl,Key=gl_script+'file.csv')

#---------------------------------

srv = pysftp.Connection(host="", username="", password="")

with srv.cd('relevant folder in sftp'): 
    srv.put(source_response['Body'].read().decode('utf-8')) 



	
	
# Closes the connection
srv.close()