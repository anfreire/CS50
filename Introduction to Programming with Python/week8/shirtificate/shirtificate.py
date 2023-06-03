from fpdf import FPDF


name = input("Name: ")


pdf = FPDF(format=(210, 297))
pdf.add_page()
pdf.set_page_background((255,255,255))
pdf.set_font("helvetica", "B", 42) #42 school
pdf.cell(0, 60, txt='CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.image("shirtificate.png", w=pdf.epw)
pdf.set_font_size(24)
pdf.set_text_color(255, 255, 255)
pdf.text(x=74, y=148.5, txt=f"{name} took CS50")

pdf.output("shirtificate.pdf")

