from fpdf import FPDF

class PDF:
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 40)
        self._pdf.cell(0, 60, text="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        text_width = self._pdf.get_string_width(f"{name} took CS50") / 2
        centered_x_position = (210 / 2) - text_width
        self._pdf.text(x=centered_x_position, y=140, text=f"{name} took CS50")

    def save(self, name):
        self._pdf.output(name)

name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")c
