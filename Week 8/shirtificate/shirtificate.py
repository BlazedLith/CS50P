from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 24)
        self.cell(0, 15, "CS50 Shirtificate", ln=True, align="C")

def main():
    name = input("Name: ")

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.image("shirtificate.png", x=15, y=60, w=180)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)  
    pdf.set_xy(0, 125)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
