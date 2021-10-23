import sys
import socket
from network_common.wrappers import Request,Response
from network_server.config import Configuration
class NetworkServer:
    def __init__(self,requestHandler):
        self.server_configuration=Configuration()
        self.requestHandler=requestHandler
        self.server_configuration._obj._validate_values()
        if self.server_configuration._obj.has_exceptions:
            for exception in self.server_configuration._obj.exceptions.values():
                print(exception[1])
            sys.exit()
    def start(self):
        server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.bind(("localhost",self.server_configuration._obj.port))
        server_socket.listen()
        while True:
            print(f"Server is listening on port: {self.server_configuration._obj.port}")
            client_socket,socket_name=server_socket.accept()
            data_bytes=b''
            to_receive=1024
            while len(data_bytes)<to_receive:
                bytes_read=client_socket.recv(to_receive-len(data_bytes))
                data_bytes+=bytes_read
            request_data_length=int(data_bytes.decode("utf-8").strip())
            data_bytes=b''
            to_receive=request_data_length
            while len(data_bytes)<to_receive:
                bytes_read=client_socket.recv(to_receive-len(data_bytes))
                data_bytes+=bytes_read
            request_data=data_bytes.decode("utf-8")
            request=Request.from_json(request_data)
            response=self.requestHandler(request)
            response_data=response.to_json()
            client_socket.sendall(bytes(str(len(response_data)).ljust(1024),"utf-8"))
            client_socket.sendall(bytes(response_data,"utf-8"))
            client_socket.close()
        server_socket.close()