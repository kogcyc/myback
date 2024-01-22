from fpdf import FPDF
import lorem
from sys import argv

#pdf = FPDF('P','in',[6,9])
pdf = FPDF('P','in',[8.5,11])

pdf.add_font('ACPR', '', './AdobeCaslonRegular.ttf', uni=True)
pdf.add_font('ISBR', '', './HalisRegular.ttf', uni=True)
pdf.add_font('IMR', '', './IBMPlexMonoRegular.ttf', uni=True)
pdf.add_font('S', '', './SupermercadoOneRegular.ttf', uni=True)


pdf.add_page()



a = ''
for t in range(int(argv[1])):
	a = a + lorem.sentence()
a = """
Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.

"""

pdf.set_font('ISBR', '', 14)

pdf.set_xy(0.5,0.5)
pdf.multi_cell(5,.22, "Lincoln's Gettysburg Address")


pdf.set_font('ACPR', '', 10.8)

yy = pdf.get_y()
print(len(a))
pdf.set_xy(0.5,yy)
pdf.multi_cell(5,.22, a)



b = """

 from fpdf import FPDF
 import lorem
 from sys import argv

 pdf = FPDF('P','in',[6,9])

 pdf.add_font('ACPR', '', './typefaces/Caslon_Regular.ttf', uni=True)
 pdf.add_font('ISBR', '', './typefaces/IBM_PLEX_SANS_BOLD_Regular.ttf', uni=True)

 pdf.add_page()

"""

pdf.set_font('IMR', '', 7)
pdf.set_fill_color(244,244,244);

yy = pdf.get_y()
print(len(b))
pdf.set_xy(0.5,yy)
pdf.multi_cell(5,.13, b, fill=True)




pdf.set_font('S', '', 9)
pdf.set_fill_color(255,255,255);

yy = pdf.get_y()
print(len(b))
pdf.set_xy(0.5,yy)
#pdf.set_letter_spacing(0.4)
pdf.multi_cell(5,.13, 'kogswell', fill=True)



pdf.output('loremy.pdf', 'F')