from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="what is your name", ln=1, align="L")
pdf.cell(200, 10, txt="my name is Elli", ln=2, align="L")
pdf.cell(200, 10, txt="Fuck you Elli", ln=3, align="L")
pdf.cell(200, 10, txt="what is your name", ln=4, align="L")
pdf.cell(200, 10, txt="my name is D", ln=5, align="L")
pdf.cell(200, 10, txt="Then fuck you D", ln=6, align="L")
pdf.output("file.pdf")