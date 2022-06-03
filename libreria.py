class Library:
    def __init__(self,):
        self.__list_books = []
        self.__list_clients = []
        self.__assigned_books = []

    def set_list_books(self,book):
        self.__list_books.append(book)

    def set_list_clients(self,client):
        self.__list_clients.append(client)

    def show_books(self):
        return self.__list_books

    def show_clients(self):
        return self.__list_clients

    def assing(self,book,client):
        assing = "The client: "+client+", has the book: " + book
        self.__assigned_books.append(assing)

#    def show_assigned(self):
        