from reportlab.pdfgen import canvas

def create_pdf_file(path):
    c = canvas.Canvas(path)

    # The coordinates (100, 750) here are from the bottom left of the document.
    c.drawString(100, 750, "Hello, World!")

    # Complete and save the document
    c.save()

create_pdf_file("hello.pdf")
