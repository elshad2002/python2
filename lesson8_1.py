class Date:

    def __init__(self, date):
        self.date = date


    @classmethod
    def my_method(cls,date):
        new_date = tuple(map(int, date.split("-")))
        #day, month, year = new_date.split(",")
        return  new_date#f"{day} {month} {year}"

print(Date.my_method("18-05-2002"))






