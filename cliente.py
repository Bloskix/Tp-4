class Client:
    def __init__(self,name,age,adress):
        self.__name = name
        self.__age = age
        self.__address = adress

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
            self.__age = age

    def set_address(self, address):
        self.__address = address

    def complete_client(self):
        add = "Name:",self.__name,"Age:",self.__age,"Address:",self.__address
        return add

    def view(self):
        return print("Name:", self.__name, "\nAge:", self.__age, "\nAdress:", self.__address)

