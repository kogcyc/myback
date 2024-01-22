from fpdf import FPDF
from sys import argv

pdf = FPDF('P','in',[4.17,6.25])

pdf.add_page()

for t in range(50):
	pdf.line(-1, -1+t*0.19685, 6, -1+t*0.19685)

for t in range(50):
	pdf.line(-1+t*0.19685, -1, -1+t*0.19685, 7)

pdf.output('graph_paper_4x6.pdf', 'F')