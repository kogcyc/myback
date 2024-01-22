from fpdf import FPDF
from sys import argv

pdf = FPDF('P','in',[4.17,6.25])

pdf.add_page()

mm5 = 5.0 / 25.4 
mm10 = 10.0 / 25.4 

pdf.set_line_width(.005)

# blue

pdf.set_draw_color(200,200,200)

for t in range(50):
	pdf.line(-1, -1+t*mm10, 6, -1+t*mm10)

for t in range(50):
	pdf.line(-1+t*mm10, -1, -1+t*mm10, 7)

# red

pdf.set_draw_color(222,222,222)

for t in range(50):
	pdf.line(-1, -1+mm5+t*mm10, 6, -1+mm5+t*mm10)

for t in range(50):
	pdf.line(-1+mm5+t*mm10, -1, -1+mm5+t*mm10, 7)


pdf.output('graph_paper_4x6_red_blue.pdf', 'F')