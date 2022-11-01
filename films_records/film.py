from films_records.program import Program


class Film(Program):
    def __init__(self, title, year, duration):
        super().__init__(title, year)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration
