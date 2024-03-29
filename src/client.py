import json
import socket


class SocketClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        # Placeholder function for client thread
        pass

    def send_create_invitation(self, requester, date, recipient):
        # Send a request to create a meeting invitation
        request_data = {
            "request_type": "create_invitation",
            "email": requester,
            "date": date,
            "recipient": recipient,
        }
        request_json = json.dumps(request_data)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(request_json.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8").strip()
            print(f"Received response: {response}")

    def send_update_invitation(self, user, requester, date, recipient, status):
        # Send a request to update a meeting invitation
        request_data = {
            "request_type": "update_invitation",
            "email": user,
            "requester": requester,
            "date": date,
            "recipient": recipient,
            "status": status,
        }
        request_json = json.dumps(request_data)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(request_json.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8").strip()
            print(f"Received response: {response}")

    def send_receive_invitation(self, email):
        # Send a request to receive meeting invitations for a given email
        request_data = {
            "request_type": "receive_invitation",
            "email": email
        }
        request_json = json.dumps(request_data)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(request_json.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8").strip()
            print(f"Received response: {response}")
            return response

    def send_login_request(self, email, password):
        # Send a login request with email and password
        request_data = {
            "request_type": "login",
            "email": email,
            "password": password
        }
        request_json = json.dumps(request_data)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(request_json.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8").strip()
            print(f"Received response: {response}")
            return response

    def send_sign_in_request(self, username, email, password):
        # Send a sign-in request with username, email, and password
        request_data = {
            "request_type": "sign_in",
            "email": email,
            "password": password,
            "username": username
        }
        request_json = json.dumps(request_data)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(request_json.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8").strip()
            print(f"Received response: {response}")
            return response
