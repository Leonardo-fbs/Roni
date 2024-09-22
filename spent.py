
class Spent:
    listSpent = []
    def __init__(self, type, description, value, month):
        self.description = description
        self.type = type
        self.value = value
        self.month = month

spent = Spent('conta', 'puta', '200', 6)


