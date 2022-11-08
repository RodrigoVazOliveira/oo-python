class Playlist():
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    @property
    def listing(self):
        return self._programs

    def __len__(self):
        return len(self._programs)

    def __getitem__(self, item):
        return self._programs[item]