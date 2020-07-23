import telnetlib as tel
import getpass as pas

HOST = input("Enter the host name: ")
user = input("Enter telnet account name: ")
password = pas.getpass()

ts = tel.Telnet(HOST)

ts.read_until(b"Username: ")
ts.write(user.encode('ascii') + b"\n")
if password:
    ts.read_until(b"Password: ")
    ts.write(password.encode('ascii') + b"\n")
    
print("Connection is estabilished!")
print("Staring to configure the " + str(HOST))
ts.write(b"conf t\n")
for i in range(0, 5):
    ts.write(b"int loop " + str(i).encode('ascii') + b"\n")
    ts.write(b"ip address 1.1." + str(i+2).encode('ascii') + b"." +str(i+1).encode('ascii') + b" 255.255.255.0\n")
ts.write(b"end\n")
ts.write(b"wr\n")
ts.write(b"exit\n")

print(ts.read_all().decode('ascii'))
print("Hey Admin, all configurations has finished!")
