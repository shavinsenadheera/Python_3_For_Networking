import paramiko
import getpass
import time

hostname = input("IP ADDRESS : ")
username = input("SSH ACCOUNT NAME: ")
password = getpass.getpass()

sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclient.connect(hostname=hostname,username=username,password=password)
print("The connection is established ! ")

rconn = sshclient.invoke_shell()

rconn.send("conf t\n")
for i in range(1,10):
    print("Creating the loop no: "+ str(i))
    rconn.send("int loop "+ str(i) + "\n")
    rconn.send("ip address "+str(i+1)+"."+str(i+1)+"."+str(i+1)+"."+str(i+1)+" 255.255.255.255\n")
    rconn.send("exit\n")
    time.sleep(0.5)

rconn.send("end\n")
rconn.send("wr\n")
time.sleep(1)
output = rconn.recv(65535)
print("Sucessfully done the configurations!")
sshclient.close()

