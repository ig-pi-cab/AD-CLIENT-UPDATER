import paramiko

class SSHManager:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        """Establish an SSH connection to the server."""
        try:
            self.ssh_client.connect(self.host, username=self.username, password=self.password)
            print(f"Connected to {self.host}")
        except Exception as e:
            print(f"Failed to connect to {self.host}: {e}")

    def run_command(self, command):
        """Run a command on the remote server."""
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            stdout_output = stdout.read().decode()
            stderr_output = stderr.read().decode()
            return stdout_output, stderr_output
        except Exception as e:
            print(f"Failed to execute command '{command}': {e}")
            return None, str(e)

    def open_sftp(self):
        """Open an SFTP session for file operations."""
        try:
            return self.ssh_client.open_sftp()
        except Exception as e:
            print(f"Failed to open SFTP session: {e}")
            return None

    def close(self):
        """Close the SSH connection."""
        self.ssh_client.close()
        print(f"Disconnected from {self.host}")
