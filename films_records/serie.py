from films_records.program import Program


class Serie(Program):

    def __init__(self, title, year, session):
        super().__init__(title, year)
        self.__session = session

    @property
    def session(self):
        return self.__session

    @classmethod
    def get_likes(cls):
        return f"Essa e a quantidade de likes {cls.like}"