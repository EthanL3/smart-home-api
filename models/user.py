class User:
    def __init__(self, user_id, name, username, email, phone):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'phone': self.phone
        }