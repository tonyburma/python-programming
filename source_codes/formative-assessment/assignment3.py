class SmartDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
    
    def turn_off(self):
        self.status = "OFF"

    def perform_diagnostic(self):
        return f"Checking device {self.device_id}..."

class SmartLight(SmartDevice):
    def __init__(self, device_id, color):
        super().__init__(device_id)
        self.color = color

    def perform_diagnostic(self):
        return f"Light {self.device_id}: Checking bulb filament and {self.color} LED status."

class SecurityCamera(SmartDevice):
    def __init__(self, device_id, storage_gb):
        super().__init__(device_id)
        self.storage_gb = storage_gb

    def perform_diagnostic(self):
        return f"Camera {self.device_id}: Checking Wi-Fi signal and {self.storage_gb}GB storage space."

# Master Shutdown Function
def master_shutdown(device_list):
    print("\n--- Initiating Master Shutdown ---")
    for device in device_list:
        device.turn_off()
        print(f"Device {device.device_id} is now {device.status}.")

# Implementation
home_devices = [
    SmartLight("LIVING_ROOM_01", "Warm White"),
    SecurityCamera("FRONT_DOOR_CAM", 128)
]

for d in home_devices:
    print(d.perform_diagnostic())

master_shutdown(home_devices)