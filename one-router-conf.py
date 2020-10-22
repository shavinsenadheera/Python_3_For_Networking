from netmiko import ConnectHandler

rios = {'device_type':'cisco_ios', 'ip':'192.168.122.211', 'username':'shavindu', 'password':'shavindu'}
conn = ConnectHandler(**rios)

for i in range(0, 11):
    print("creating int loop " + str(i))
    configs = ['int loop ' + str(i), 'ip address ' + str(i+1) + '.' + str(i+1) + '.' + str(i) + '.' + str(i) ' 255.255.255.255', 'exit']
    conn.send_config_set(configs)
saveconf = ['end', 'wr']
conn.send_config_set(saveconf)

output = conn.send_command('shoeip int br')
print(output)
