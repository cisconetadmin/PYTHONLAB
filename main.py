from contextlib import nullcontext
from netmiko import ConnectHandler
from pprint import pprint
import yaml

def get_interface_count_clear_on_device(device):

    net_connect = ConnectHandler(**device)

    output = net_connect.send_command('show int', use_textfsm=True)

    i = 0
    for item in output:
        if (item['hardware_type'] == 'AmdP2') and (item['last_input'] == 'never'):
            i = i+1
    return i


def get_cout():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    count = 0

    for device in devices:
        count += get_interface_count_clear_on_device(device)

    return {'interfaces_count': str(count)}


def get_device(hostname):

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for device in devices:
        if device['host'] == hostname:
            return device
    
    return None

def get_devices():

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for device in devices:
        device.pop('password')
        device.pop('secret')
        device.pop('username')

    return devices