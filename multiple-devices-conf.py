from netmiko import ConnectHandler
import time

r1ios = {'device_type' : 'cisco_ios', 'ip' : '192.168.122.211', 'username' : 'shavindu', 'password' : 'shavindu'}

r2ios = {'device_type' : 'cisco_ios', 'ip' : '192.168.122.212', 'username' : 'shavindu', 'password' : 'shavindu'}

sw1ios = {'device_type' : 'cisco_ios', 'ip' : '192.168.122.213', 'username' : 'shavindu', 'password' : 'shavindu'}

devices = [r1ios, r2ios]
for device in devices:
    conn = ConnectHandler(**device)
    for i in range(0, 11):
        print('creating int loop ' + str(i) + ' on : ' + device['ip'])
        configs = ['int loop ' + str(i), 'ip address ' + str(i+1) + '.' + str(i+1) + '.' + str(i+1) + '.' + str(i+1) + ' 255.255.255.255', 'exit']
        conn.send_config_set(configs)
        time.sleep(0.5)
    saveconf = ['end', 'wr']
    conn.send_config_set(saveconf)
    output = conn.send_command('show ip int br')
    print(output)

conn = ConnectHandler(**sw1ios)

for i in range(10, 101, 10):
    print('creating vlan ' + str(i) + ' on : ' + sw1ios['ip'])
    configs = ['vlan ' + str(i), 'name v_' + str(i), 'exit']
    conn.send_config_set(configs)
    time.sleep(0.5)
output = conn.send_command('show vlan br')
print(output)
