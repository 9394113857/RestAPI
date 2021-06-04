# Python Program to Get IP Address and Device name:-
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)





"""
elif not re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                  userip):
msg = 'Invalid ip address format !'

"""