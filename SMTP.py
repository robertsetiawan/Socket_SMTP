# Skeleton Python Code for the Mail Client
from socket import *
import ssl
import base64
import getpass

# Choose a mail server (e.g.Googlemailserver) and call it mailserver
# Fill in start
mailserver = ("smtp.gmail.com", 465)
# Fill in End

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket, ssl_version = ssl.PROTOCOL_SSLv23)
clientSocket.connect(mailserver)
# Fill in end

recv = clientSocket.recv(1024)
print("[recv] " + recv.decode())
if recv[:3] != '220':
	print("[recv] 220 reply not received from server.\n")

# Send HELO command and print server response.
heloCommand = "HELO Alice\r\n"
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print("[recv1] " + recv1.decode())
if recv1[:3] != '250':
	print("[recv1] 250 reply not received from server.\n")
	
# Info for username and password
username = input("Insert username: ")
userEmail = username + "@gmail.com"
password = getpass.getpass(prompt= "\nInsert Password: ")
base64_str = ("\000" + userEmail + "\000" + password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print("\n[AUTH] " + recv_auth.decode())

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = "MAIL FROM: <"+ userEmail +">\r\n"
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024)
print("[recv2] After MAIL FROM command: " + recv2.decode())
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
receiver = input("Send email to: ")
rcptToCommand = "RCPT TO: <"+ receiver +">\r\n"
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024)
print("\n[recv3] After RCPT TO command: " + recv3.decode())
if recv3[:3] != '250':
	print("[recv3] 250 reply not received from server.\n")
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024)
print("[recv4] After DATA command: " + recv4.decode())
# Fill in end

# Send message data.
# Fill in start
subject = input("Subject: ")
endmsg = "\r\n.\r\n"
msg = input("Message: ")

clientSocket.send(("Subject: "+ subject + "\r\n\r\n"+ msg +"\r\n").encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024)
print("\n[recv5] Response after sending message body: " + recv5.decode())
# Fill in end

# Send QUIT command and get server response.
# Fill start
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv6 = clientSocket.recv(1024)
print("[recv6] " + recv6.decode())
clientSocket.close()
# Fill in end
