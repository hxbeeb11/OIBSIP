import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break

            print(f"{username}: {message}")

        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"{username} has left the chat.")
    client_socket.close()

def start_server():
    host = "127.0.0.1"
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client, addr = server.accept()
        username = client.recv(1024).decode("utf-8")
        print(f"{username} has joined the chat.")

        client.send("Welcome to the chat!".encode("utf-8"))

        client_handler = threading.Thread(target=handle_client, args=(client, username))
        client_handler.start()

if __name__ == "__main__":
    start_server()
