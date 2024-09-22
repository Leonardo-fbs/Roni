import user
from spent import Spent
from user import User
from user import Users


class Menu:
    @staticmethod
    def Inicializar():
        pass


Menu.Inicializar()
while (True):
    esc = int(input("Menu escolhas as opções:\n[0] mostrar teste\n[1] cad users\n[2] cad spent\n[4] list user\n[5] list spent\n[9] exit\n"))

    if (esc == 0):
        Users.printUsers()
    elif (esc == 1):
        name = input("digite seu name:\n")
        wage = input("digite seu salario:\n")

        spent1 = User(name, wage)
        print(f"ok {spent1.name}")
        numberUser = +1
    elif (esc == 2):
        description = input("digite a descrição de gasto previamente:\n")
        type = input("digite seu tipo de gasto:\n")
        value = input("digite seu o valor:\n")
        month = input("digite o mes:\n")
        spent = Spent(description, type, value, month)
        Spent.listSpent.append(spent)
        # Call the vars() on Object
        obj_vars = vars(spent)
        # Print the properties
        print(obj_vars)
    elif esc == 4:
        User.mostrarUser()
    elif (esc == 5):
        User.mostrarUser()
    elif (esc == 9):
        break
    else:
        print("você digitou um valor invalido")