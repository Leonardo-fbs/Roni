
class User:
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage


class Users:
    def __init__(self):
        self.list_users = []
        pass

    def addUser(self, obj_user):
        assert isinstance(obj_user, User), "Tem que ser uma classe do tipo user"
        self.list_users.append(obj_user)

    def printUsers(self):
        for p in self.list_users:
            print(f'{p.name} --> {p.wage}')


# Crio cada user
user1 = User('Jon', 33)
user2 = User('Ned', 25)
user3 = User('Robb', 44)

users = Users()
# Adiciono a lista dentro da classe users
users.addUser(user1)
users.addUser(user2)
users.addUser(user3)

# Printo todas as users na tela
users.printUsers()


