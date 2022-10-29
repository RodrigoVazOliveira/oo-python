from client import Client

if __name__ == "__main__":
    client = Client("rodrigo")
    print(client.name)
    client.name = "jorge"
    print(client.name)