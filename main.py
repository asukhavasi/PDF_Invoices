import pandas as pd
import glob
import fpdf
from pathlib import Path

filepath = glob.glob("Data/*.xlsx")
print(filepath)

for file in filepath:
    df = pd.read_excel(file,sheet_name="Sheet 1")
    # print(df)

    filename = Path(file).stem
    invoice_nr = filename.split("-")
    invoice_name = invoice_nr[0]
    date = invoice_nr[1]

    pdf = fpdf.FPDF(orientation='P',unit='mm',format='A4')
    pdf.add_page()

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50, h=8, txt=f'Invoice # {invoice_name}',align="L",border=0,
             ln=1)

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50, h=8, txt=f'Date: {date}',align="L",border=0,ln=1)






    pdf.output(f"Data/PDFs/{filename}.pdf")

