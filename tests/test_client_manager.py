from client_manager import ClientManager

def main():
    cm = ClientManager()

    cm.add_client('TestClient', 'admin', '10', '/path/to/target', '/path/to/adempiere')
    
    # Retrieve and print all clients
    clients = cm.get_clients()
    print('Clients:', clients)

    # Update the test client
    cm.update_client(clients[0][0], 'UpdatedClient', 'admin', '192.168.1.20', '/new/path/target', '/new/path/adempiere')

    # Retrieve and print updated clients
    clients = cm.get_clients()
    print('Updated Clients:', clients)

    # Delete the test client
    cm.delete_client(clients[0][0])

    # Retrieve and print remaining clients
    clients = cm.get_clients()
    print('Remaining Clients:', clients)

if __name__ == "__main__":
    main()
