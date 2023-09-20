import openvpn

# Create a VPN client object.
client = openvpn.Client()

# Connect to the VPN server.
client.connect('client.ovpn')

# Wait for the connection to be established.
client.wait_for_connection()

# Once the connection is established, we can start sending and receiving data.
print('Connected to the VPN.')

# Disconnect from the VPN server.
client.disconnect()
