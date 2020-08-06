from netmiko import ConnectHandler

rios = {'device_type':'cisco_ios','ip':'192.168.1.6', 'username':'shavindu','password':'shavindu'}
conn = ConnectHandler(**rios)

conn.send_enable()
conn.send_command('show ip int br')
print(output)

configs = ['conf t','int loop 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'end']
conn.send_config_set(configs)
