class Playlist(list):
    def __init__(self, name, programs):
        self.name = name
        super().__init__(programs)


