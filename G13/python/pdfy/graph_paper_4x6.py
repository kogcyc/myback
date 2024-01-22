from fpdf import fpdf
from sys import argv

pdf = FPDF('P','in',[4.17,6.25])

pdf.add_page()

for t in range(10):
	pdf.line(1, 1+t/10, 4, 1+t/10)

pdf.output('graph_paper_4x6.pdf', 'F')