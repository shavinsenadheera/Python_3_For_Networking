import paramiko
import getpass
import time

sshclient = paramiko.SSHClient()
def runcommands(hostname, username, password):
    try:
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshclient.connect(hostname=hostname,username=username,password=password)
        print("The SSH connection is established!")
        rconn = sshclient.invoke_shell()
        rconn.send("conf t\n")
        for i in range(10,301,10):
            print("Creating VLAN " + str(i))
            rconn.send("vlan " + str(i) + "\n")
            rconn.send("name vlan_" + str(i) + "\n")
            rconn.send("exit\n")
            time.sleep(0.5)

        rconn.send("end\n")
        rconn.send("wr\n")

        print("Congratulations Admin! Configurations has successfully done!")
        sshclient.close()

    except Exception as er:
        print("Admin ! Check the North Bound !")
        print(er)

hostname = input("IP ADDRESS: ")
username = input("SSH ACCOUNT NAME: ")
password = getpass.getpass()

runcommands(hostname,username,password)

