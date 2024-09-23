class FileManager:
    def __init__(self, ssh_manager):
        """Initialize with an SSHManager instance for handling file uploads."""
        self.ssh_manager = ssh_manager

    def upload_file(self, local_path, remote_path):
        """Upload a file to the remote server using the provided SSHManager's SFTP session."""
        try:
            sftp = self.ssh_manager.open_sftp()
            if sftp:
                sftp.put(local_path, remote_path)   # Upload the file
                sftp.close()  # Close the SFTP session
                print(f"Uploaded {local_path} to {remote_path}")
            else:
                print("SFTP session could not be established.")
        except Exception as e:
            print(f"Failed to upload {local_path}: {e}")
