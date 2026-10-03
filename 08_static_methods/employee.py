class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance Methods
    def get_info(self):
        return f"{self.name} = {self.position}"

    # Static Method
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions