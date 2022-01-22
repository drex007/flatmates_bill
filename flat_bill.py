
class Bill:
    def __init__(self, amount,period):
        self.period = period
        self.amount = amount



class Flatmates:

    def __init__(self, name, days_in_house ):
        self.days_in_house = days_in_house
        self.name = name

    def pay(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        topay = bill.amount * weight
        return topay




