from flat_bill import Bill, Flatmates
from reports import PdfReport


users_amount = float(input("Please Enter Amount:"))
users_period = input("Please Enter Period:")

name1 = input("Flatmate1:")
days_in_house1 = int(input(f"Days in whic {name1} stay in the house? :"))

name2 = input("Flatmate2:")
days_in_house2 = int(input(f"Days in whic {name2} stay in the house?:"))


the_bill = Bill(amount =users_amount, period=users_period)
flatmate1 = Flatmates(name1, days_in_house1)
flatmate2 = Flatmates(name2, days_in_house2)

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)




print(f"{name1} pays:", flatmate1.pay(the_bill, flatmate2))
print(f"{name2} pays:", flatmate2.pay(the_bill, flatmate1))


