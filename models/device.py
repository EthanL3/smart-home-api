class Device:
    def __init__(self, device_id, name, type, status):
        self.device_id = device_id
        self.name = name
        self.type = type
        self.status = status
    
    def to_json(self):
        return {
            'device_id': self.device_id,
            'name': self.name,
            'type': self.type,
            'status': self.status
        }