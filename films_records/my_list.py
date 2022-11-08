from collections.abc import Sized

class MyList(Sized):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description


my_list = MyList("Nova Lista")
print(my_list)