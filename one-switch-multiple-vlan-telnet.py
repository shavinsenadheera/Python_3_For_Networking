#!/usr/bin/env python3

import telnetlib as tel
import getpass as pas

hostname ="ip_address_of_switch"
username = input("Enter the telnet account name: ")
password = pas.getpass()

telnetconnection = tel.Telnet(hostname)

telnetconnection.read_until(b"Username: ")
telnetconnection.write(username.encode('ascii') + b"\n")
if password:
    telnetconnection.read_until(b"Password: ")
    telnetconnection.write(password.encode('ascii') + b"\n")

print("Starting to configure " + str(hostname))

telnetconnection.write(b"enable\n")
telnetconnection.write(password.encode('ascii') + "\n")
telnetconnection.write(b"configure terminal\n")

for i in range(10, 101, 10): # i = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    telnetconnection.write(b"vlan " + str(i).enocde('ascii') + b"\n")
    telnetconnection.write(b"name vlan_" + str(i) + b"\n")

telnetconnection.write(b"end\n")
telnetconnection.write(b"write\n")
telnetconnection.write(b"exit\n")

print(telnetconnection.read_all().decode('ascii'))
print("Congratulations! configurations have finished!")
