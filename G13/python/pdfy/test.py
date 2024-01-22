from fpdf import FPDF

pdf = FPDF('P','in',[6,9])
pdf.add_page()
pdf.set_font('Times', '', 13)

pdf.set_xy(0.5,0.5)
pdf.multi_cell(5,.23, 'This method prints text from the current position. When the right margin is reached (or the newline character is met) a line break occurs and text continues from the left margin. Upon method exit, the current position is left just at the end of the text. ')
#pdf.write(1, 'Hello World!')
yy = pdf.get_y()
print(yy)
pdf.set_xy(0.5,yy+0.2)
pdf.multi_cell(5,.23, 'This method prints text from the current position. When the right margin is reached (or the newline character is met) a line break occurs and text continues from the left margin. Upon method exit, the current position is left just at the end of the text. ')

pdf.output('test.pdf', 'F')

