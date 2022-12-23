from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(20, 20, 20)
    pdf.set_draw_color(20, 20, 20)
    pdf.cell(w=0, h=16, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 24, 200, 24)

    pdf.set_draw_color(232, 232, 232)
    for i in range(34, 288, 10):
        pdf.line(10, i, 200, i)

    # Add breaking lines
    pdf.ln(258)

    # Footer
    pdf.set_font(family="Times", style="I", size=9)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=9, txt=row["Topic"], align="R")

pdf.output("output.pdf")
