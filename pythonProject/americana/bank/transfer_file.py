from ftplib import FTP


def transfer_file_ftp(host, username, password, local_file_path, remote_file_path):
    try:
        ftp = FTP(host)
        ftp.login(username, password)

        with open(local_file_path, 'rb') as local_file:
            ftp.storbinary(f'STOR {remote_file_path}', local_file)

        ftp.quit()
        print(f"File '{local_file_path}' transferred to '{remote_file_path}' successfully via FTP.")
    except Exception as e:
        print(f"Error transferring file: {str(e)}")
