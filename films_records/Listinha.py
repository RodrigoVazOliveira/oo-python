class Listinha:

    def __init__(self, items):
        self.__items = items

    def __getitem__(self, item):
        return self.__items[item]

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return self.__items


if __name__ == "__main__":
    meu_objeto = Listinha([0, 1, 2, 3, 4, 5, 6])
    contador = 0

    for item in meu_objeto:
        contador += 1

    if len(meu_objeto) == contador:
        print('São iguais!')
    else:
        print('Não são iguais!')