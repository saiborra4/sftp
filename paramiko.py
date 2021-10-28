import math
import time
import io
import boto3
import paramiko

S3_BUCKET_NAME = "example-bucket"

FTP_HOST = "ftp.example.com"
FTP_PORT = 22
FTP_USERNAME = "john.doe"
FTP_PASSWORD = "XXXX"


def open_ftp_connection(ftp_host, ftp_port, ftp_username, ftp_password):
    """
    Opens ftp connection and returns connection object
    """
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    try:
        transport = paramiko.Transport(ftp_host, ftp_port)
    except Exception as e:
        return "conn_error"
    try:
        transport.connect(username=ftp_username, password=ftp_password)
    except Exception as identifier:
        return "auth_error"
    sftp = paramiko.SFTPClient.from_transport(transport)
    return ftp_connection
	
	
def transfer_file_from_ftp_to_s3():

      with sftp.open('/sftp/path/filename', 'wb', 32768) as f:
      s3.download_fileobj('mybucket', 'mykey', f)

if __name__ == "__main__":
    ftp_username = FTP_USERNAME
    ftp_password = FTP_PASSWORD
    ftp_file_path = str(input("Enter file path located on FTP server: "))
    s3_file_path = str(input("Enter file path to upload to s3: "))
    ftp_connection = open_ftp_connection(
        FTP_HOST, int(FTP_PORT), ftp_username, ftp_password
    )
    if ftp_connection == "conn_error":
        print("Failed to connect FTP Server!")
    elif ftp_connection == "auth_error":
        print("Incorrect username or password!")
    else:
        try:
            ftp_file = ftp_connection.file(ftp_file_path, "r")
        except Exception as e:
            print("File does not exists on FTP Server!")
			
		transfer_file_from_ftp_to_s3()
		
		