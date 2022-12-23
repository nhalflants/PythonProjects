from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("texts/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()

    title = Path(filepath).stem.capitalize()

    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=16, txt=title, ln=1)

    pdf.set_font(family="Times", size=12, style="")
    pdf.multi_cell(w=0, h=8, txt=content)

pdf.output(f"pdf/output.pdf")
