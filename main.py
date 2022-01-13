import webbrowser 
from fpdf import FPDF

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



class PdfReport:

    def __init__(self,filename):
        self.filename = filename 

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt' , format='A4')
        
        pdf.add_page()
        pdf.image("house.png", w = 30, h =30)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=88, txt = "Flatmate Bill", border = 1, align ='C', ln = 1)


        # Insert Period label and values



        pdf.set_font(family="Times", size = 14 , style='B')

        pdf.cell(w=100, h=70, txt ="Period:", border=0)
        pdf.cell(w=100, h=70, txt = bill.period, border=0, ln=1)

        # insert name and the amount of first flatmate

        pdf.cell(w=100, h=20, txt =flatmate1.name + " Pays", border=0)
        pdf.cell(w=100, h=20, txt = "$"+str(round(flatmate1.pay(bill,flatmate2), 2)),border=0 , ln=1)
        pdf.cell(w=100, h=20, txt =flatmate2.name + " Pays", border=0)
        pdf.cell(w=100, h=20, txt = "$"+str(round(flatmate2.pay(bill,flatmate1), 2)),border=0 , ln=1)
        pdf.output(self.filename)

        webbrowser.open(self.filename)

user_amount = float(input("Please Enter Amount:"))


the_bill = Bill(amount =user_amount, period="Jan 2022")
john = Flatmates(name="John", days_in_house=20)
mary = Flatmates(name = "Mary", days_in_house=25)

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)




print("John pays:", john.pay(bill =the_bill, flatmate2=mary))
print("Mary pays:", mary.pay(bill =the_bill, flatmate2=john))

