import glob
from pathlib import Path
import fpdf

# Create a list for text files
filepaths = glob.glob("Data/*.txt")

# create one PDF
pdf = fpdf.FPDF(orientation="P",unit="mm",format="A4")

# loop for number of files to add pdf pages
for filename in filepaths:

    # extract only filename to copy as a header
    filename = (Path(filename).stem)
    new_filename = filename.title()

    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=30)
    pdf.cell(w=20,h=20,border=0,txt=new_filename,ln=1)

    # Open text file
    with open(filename,'r') as file:
        text = file.read()

    pdf.set_font(family="Times",size=10)
    pdf.multi_cell(w=0,h=8,txt=text,align='J')

# write output to pdf
pdf.output(f"Data/PDFs/Animals.pdf")
