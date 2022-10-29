import json


class Client:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return json.dumps(self.__dict__)