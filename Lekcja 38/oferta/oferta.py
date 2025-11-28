from fpdf import FPDF 

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=14)
pdf.cell(text="Oferta biura")


pdf.image("logo.png", x = 100, y = 100, w= 100, h=100)
pdf.output("oferta.pdf")