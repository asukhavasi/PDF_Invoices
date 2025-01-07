import pandas as pd
import glob
import fpdf
from pathlib import Path

filepath = glob.glob("Data/*.xlsx")
print(filepath)

for file in filepath:

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

    df = pd.read_excel(file,sheet_name="Sheet 1")
    df_header = list(df.columns)
    columns = [item.replace("_"," ").title() for item in df_header]


    # add header
    pdf.set_font(family="Times", size=12,style="B")
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=50, h=8, txt=columns[1], border=1)
    pdf.cell(w=40, h=8, txt=columns[2], border=1,)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    for  index,row in df.iterrows():
        # Add Rows
        pdf.set_font(family="Times",size=10)
        pdf.cell(w=30,h=8,txt=str(row["product_id"]),border=1)
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40,h=8,txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30,h=8,txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1,ln=1)

    total = df["total_price"].sum()
    pdf.set_font(family="Times",size=10,style="B")
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total), border=1, ln=1)

    pdf.set_font(family="Times", size=10)
    pdf.cell(w=30, h=8, txt=f"The total price is: {str(total)}",  ln=1)

    pdf.cell(w=30, h=8, txt=f"PythonLearning")
    pdf.image("Data/pythonhow.png",w=10)


    pdf.output(f"Data/PDFs/{filename}.pdf")

