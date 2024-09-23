import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from file_manager import FileManager 
from ssh_manager import SSHManager  
import json

def load_config(file_path):
    """Load JSON configuration file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def automate_adempiere_update(connection):
    host = connection["host"]
    username = connection["username"]
    password = connection["password"]
    local_file_path = r"C:\Users\Lenovo\Desktop\customization.jar"
    remote_dir = "/home/adempiere/lib"
    remote_file_path = f"{remote_dir}/customization.jar"

    if not os.path.exists(local_file_path):
        print(f"File {local_file_path} not found")
        return

    print(f"File being uploaded: {local_file_path}")

    #Initialize SSH connection
    ssh_manager = SSHManager(host, username, password)
    ssh_manager.connect()

    #Use FileManager to upload the file
    file_manager = FileManager(ssh_manager)
    file_manager.upload_file(local_file_path, remote_file_path)

    stdout, stderr = ssh_manager.run_command(f"cd {remote_dir} && ls -la")
    print(f"STDOUT: {stdout}")
    print(f"STDERR: {stderr}")

    ssh_manager.close()

if __name__ == "__main__":
    config = load_config("config.json")

    for connection in config["connections"]:
        print(f"Processing connection for {connection['host']}")
        automate_adempiere_update(connection)
