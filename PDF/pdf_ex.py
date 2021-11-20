#!/usr/bin/python3
from fpdf import FPDF

import segno
import os


pdf = FPDF(orientation = 'P', format = 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')


# Create qr and store into file :(
qr = segno.make_qr("This is a qrcode", error='Q')
qr.save("/tmp/myqr.png", scale=2, kind='png')
pdf.image("/tmp/myqr.png", x = 10, y = 40, w = 0, h = 0, type = 'png', link = '')
os.unlink("/tmp/myqr.png")


# Export to file
pdf.output('tuto1.pdf', 'F')