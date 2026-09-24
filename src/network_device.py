import logging

class NetworkDevice:
    def __init__(self, hostname, ip, device_type):
        self.hostname = hostname
        self.ip = ip
        self.type = device_type

    def summarize(self):
        message = f"[DEVICE_SUMMARY]: {self.hostname} ({self.type}) - {self.ip}"
        print(message)
        logging.info(message)
        return message

#testing

# device = NetworkDevice("core-sw01", "192.168.1.1", "Switch")
# device.summarize()


