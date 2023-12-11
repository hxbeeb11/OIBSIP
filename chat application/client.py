import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break

            print(message)

        except Exception as e:
            print(f"Error: {e}")
            break

def send_messages(client_socket, username):
    while True:
        message = input()
        if message.lower() == "exit":
            break

        full_message = f"{username}: {message}"
        client_socket.send(full_message.encode("utf-8"))

    client_socket.close()

def start_client():
    host = "127.0.0.1"
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    username = input("Enter your username: ")
    client.send(username.encode("utf-8"))

    welcome_message = client.recv(1024).decode("utf-8")
    print(welcome_message)

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client, username))
    send_thread.start()

if __name__ == "__main__":
    start_client()
