from fpdf import FPDF
pdf = FPDF('P', 'mm', 'Letter')
pdf.set_left_margin(15.0)
pdf.set_right_margin(15.0)
pdf.add_page()
#pdf.add_font('caslonr', '', '/home/matt/typefaces/ttfs/ACaslonPro-Regular.ttf', uni=True)
#pdf.add_font('casloni', '', '/home/matt/typefaces/ttfs/ACaslonPro-Italic.ttf', uni=True)

pdf.set_fill_color(244, 222, 190)
pdf.set_fill_color(220, 220, 220)
pdf.rect(13, 15, 189, 20, 'F')

pdf.set_font('Times', '', 36)

pdf.write(1,'\nCaslon\n\n')

pdf.set_font('Times', '', 28)

upper = ""
for t in range(65,91):
	upper = upper + chr(t) + ' '
	if chr(t) == 'M':
		upper = upper + '\n'
upper = upper + '\n'
#pdf.write(12,upper)

pdf.set_font('Times', '', 36)

lower = ""
for t in range(97,97+26):
	lower = lower + chr(t) + ' '
	if chr(t) == 'm':
		lower = lower + '\n'
lower = lower + '\n'
#pdf.write(12, lower)

pdf.set_font('Times', '', 33)

#pdf.write(16,'0 1 2 3 4 5 6 7 8 9 . , ; ? ! \' \" \n')

pdf.set_font('Times', '', 33)

#pdf.write(11,'A G M W Q b a ')

pdf.set_line_height(12)

pdf.set_font('Times', '', 16)

pdf.write(14,'This method prints text from the current position.This method prints text from the current position.This method prints text from the current position.')





pdf.output('caslon.pdf', 'F')

