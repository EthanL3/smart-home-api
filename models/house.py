class House:
    def __init__(self, house_id, address, city, state, zipcode, sqft):
        self.house_id = house_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.sqft = sqft
        self.rooms = []  # List to hold Room objects
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def to_json(self):
        return {
            'house_id': self.house_id,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zipcode': self.zipcode,
            'rooms': [room.to_json() for room in self.rooms]  # Convert rooms to dict
        }
