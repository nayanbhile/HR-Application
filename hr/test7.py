from network_client.config import Configuration
c=Configuration()
print(c)
print("Host: ",c._obj.host)
print("Port: ",c._obj.port)
c._validate_values()
print("Has Exceptions? ",c._obj.has_exceptions)
print("Exceptions: ",c._obj.exceptions)