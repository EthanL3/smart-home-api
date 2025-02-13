class Room:
    def __init__(self, room_id, name, area):
        self.room_id = room_id
        self.name = name
        self.area = area
        self.devices = []  # List to hold Device objects
    
    def add_device(self, device):
        self.devices.append(device)

    def to_json(self):
        return {
            'room_id': self.room_id,
            'name': self.name,
            'area': self.area,
            'devices': [device.to_json() for device in self.devices]
        }