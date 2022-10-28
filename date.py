class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def format_date(self):
        print("{}/{}/{}".format(self.day, self.month, self.year))