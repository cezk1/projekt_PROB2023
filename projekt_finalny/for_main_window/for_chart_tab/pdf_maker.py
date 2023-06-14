import getpass
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas


class PdfMaker:
    def __init__(self):
        self.__user = getpass.getuser()
        self.__title = "Number of passengers by country report"
        self.__date = date.today()

    def generate_pdf(self, filename, img, min_year=0, max_year=0, countries=None):
        len_fname = len(filename)
        if filename[(len_fname-4):len_fname].strip() != ".pdf":
            filepath = filename.strip() + ".pdf"
        else:
            filepath = filename

        pdf_template = self.__create_pdf(filepath, img, min_year, max_year, countries, pagesize=A4)
        pdf_template.setAuthor(self.__user)
        pdf_template.setTitle(self.__title)
        pdf_template.save()

    def __create_pdf(self, filepath, img, min_year, max_year, countries, pagesize):
        canvas = Canvas(filepath, pagesize=pagesize)
        pwidth, pheight = A4
        canvas.setFont("Times-Roman", 30)
        title = "Number of passengers by country"

        title_offset, img_offset = 100, 600
        title_x, title_y = pwidth/2, pheight - title_offset
        img_x, img_y = 10, pheight - img_offset
        bottom_text_x, bottom_text_y = img_x+30, img_y-20

        canvas.drawCentredString(title_x, title_y, title)
        canvas.drawImage(img, img_x, img_y, width=982*0.6, height=680*0.6)  # 982 i 680 to rozmiar wykresu wyswietlanego
        canvas.setFont("Times-Roman", 12)
        canvas.drawString(bottom_text_x, bottom_text_y, f"Years: {min_year} - {max_year}")
        canvas.drawString(bottom_text_x, bottom_text_y-20, f"Countries:")
        for i, country in enumerate(countries, 2):
            canvas.drawString(bottom_text_x, bottom_text_y-20*i, f"{country}")

        return canvas
