import glob
from pathlib import Path
import fpdf

# Create a list for text files
filepaths = glob.glob("Data/*.txt")

# create one PDF
pdf = fpdf.FPDF(orientation="P",unit="mm",format="A4")

# loop for number of files to add pdf pages
for filename in filepaths:
    # print(filename)
    filename = (Path(filename).stem)
    new_filename = filename.title()

    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=30)
    pdf.cell(w=20,h=20,border=0,txt=new_filename)

# write output to pdf
pdf.output(f"Data/PDFs/Animals.pdf")
