from cliente import Client
from libreria import Library
from libro import Book

print("======================", "\n1. Add Client", "\n2. Add Book", "\n3. Show Clients", "\n4. Show Books", "\n5. Assing Book","\n6. Show Assigned Books", "\n7. Exit", "\n======================")
library = Library
client = Client
book = Book
option = 0
#while (option != 7):
option = int(input("-"))
if (option == 1):
    print("Name:")
    name = str(input())
    client.set_name(name)
    print("Age:")
    age = int(input())
    client.set_age()
    print("Address:")
    address = str(input())
    client.set_address(address)
    library.set_list_clients(client.complete_client())
