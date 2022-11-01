class Program:
    def __init__(self, title, year):
        self.__title = title.title()
        self.__year = year
        self.__like = 0

    def give_like(self):
        self.__like += 1

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @property
    def like(self):
        return self.__like