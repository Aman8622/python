# configuration variables
server_name = "my_server"
port = 80
is_https_enabled = True
maxConnections = 1000

# print configuration data
print(f"Server name: {server_name}")
print(f"Port: {port}")
print(f"is_https_enabled: {is_https_enabled}")
print(f"Max connections: {maxConnections}")

# update configuration data
port = 443
maxConnections = 500
print("\n")
# print updated data 
print(f"Server name: {server_name}")
print(f"port: {port}")
print(f"is_https_enabled: {is_https_enabled}")
print(f"Max connections: {maxConnections}")
