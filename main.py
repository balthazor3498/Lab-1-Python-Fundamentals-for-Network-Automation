import logging
from src.network_device import NetworkDevice
from src.parser_utils import parse_json, parse_yaml, parse_xml, parse_csv

logging.basicConfig(filename='logs/lab.log', level=logging.INFO)

#message print and report logging
def report(message, snip):
    print(message)
    logging.info(f"{snip.upper()}_MSG: {message}")

def main():
#lab log start
    logging.info("[LAB1-START]")

#naming each segment based on the filename so i dont get confused
    devices = parse_json('data/devices.json') 
    interfaces = parse_yaml('data/interfaces.yaml')
    vlans = parse_xml('data/vlans.xml')
    inventory = parse_csv('data/inventory.csv')

#parsing json files / create network objects
    devices_list = devices.get("devices", []) if isinstance(devices, dict) else devices
    network_devices = []
    for device in devices_list:
        network_device = NetworkDevice(device['hostname'], device['ip'], device['type'])
        network_devices.append(network_device)
        
#network device summary
    for device in network_devices:
        device.summarize()

#parsing yaml files
    if isinstance(interfaces, dict) and "interfaces" in interfaces:
        for interface in interfaces["interfaces"]:
            message = f"Interface {interface['name']} is {interface['status']}"
            report(message, "interface")

#parsing xml files
    for child in vlans:
        message = (f"{child.tag.upper()} {child[0].text} is the {child[1].text}")
        report(message, "vlan")

#parsing csv files
    for device in inventory:
        message = (f"Device {device['hostname']} is a {device['location']} {device['role']}")
        report(message, "device")

#lab log end
    logging.info("[LAB1-END]")

if __name__ == "__main__":
    main()