import webbrowser 
from fpdf import FPDF

import os



class PdfReport:

    def __init__(self,filename):
        self.filename = filename 

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt' , format='A4')
        
        pdf.add_page()
        pdf.image("files/house.png", w = 30, h =30)
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
        # change path directory to files, generate and open the pdf file 
        os.chdir("files")
        pdf.output(self.filename)

        webbrowser.open(self.filename)




