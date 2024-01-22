import mkepub

from pathlib import Path

import ziamath as zm

m_t01="""
<div style="margin: 0; height: 100%; width: 100%; padding: 40px; background-color: #000;">
<span style='padding: 20px; font-size: 24px; font-family: Supermercado One; font-weight: 900; background-color: #000; color: #fff;'>
kogswell
</span>
</div>
"""

m_c01="""
<div style="margin: 0; height: 100%; width: 100%; padding: 0px; background-color: #fff;">
<p style='padding: 0px 20px; font-size: 22px; font-family: sans-serif; font-weight: 900; background-color: #fff; color: #000;'>
Chapter 1
</p>
<p style='line-height: 1.6em; padding: 0px 20px; font-size: 13px; font-family: times; font-weight: 400; background-color: #fff; color: #000;'>
In the beginning, there was a lot of crap to sort through. Today, everything is so much easier. It makes you wonder how people did it any other way.
<br/>
<img src="images/some.png" style="width: 400px;"/>
</p>
</div>
"""

m_c02="""
<div style="margin: 0; height: 100%; width: 100%; padding: 0px; background-color: #fff;">
<p style='padding: 0px 20px; font-size: 22px; font-family: sans-serif; font-weight: 900; background-color: #fff; color: #000;'>
Chapter 2
</p>
<p style='line-height: 1.6em; padding: 0px 20px; font-size: 13px; font-family: times; font-weight: 400; background-color: #fff; color: #000;'>
<span style="font-size: 18px; font-weight: 900;">T</span>his is the way that Chapter two starts.
It is a long series of events that culminate in a paragraph about the needless waste of resources.
</p>
</div>
"""

mathh = """
<div style="padding: 20px;">
"""
mathh = mathh + zm.Latex("\\theta = tan^{-1}\\left(\\frac{opp}{adj}\\right)",size=11.0).svg()
mathh = mathh + """
</div>
"""

book = mkepub.Book(title='The kogswell Book', author='MG')

with open('kdp_cover.png', 'rb') as file:
	book.set_cover(file.read())

with open('style.css') as file:
    book.set_stylesheet(file.read())

with open('images/some.png', 'rb') as file:
    book.add_image('some.png', file.read())

t01 = book.add_page('Title', m_t01)
c01 = book.add_page('Chapter 1', m_c01)
c02 = book.add_page('Chapter 2', m_c02)
c03 = book.add_page('Chapter 3', mathh)

#child = book.add_page('Chapter 1.1', 'Nested TOC is supported.', parent=first)
#book.add_page('Chapter 1.1.1', 'Infinite nesting levels', parent=child)
#book.add_page('Chapter 1.2', 'In any order you wish.', parent=first)

#book.add_page('Chapter 2', 'Use <b>html</b> to make your text <span class="pink">prettier</span>')

# book.add_page('Chapter 3: Images', '<img src="images/chapter3.png" alt="You can use images as well">')
# as long as you add them to the book:
# with open('chapter3.png', 'rb') as file:
    #book.add_image('chapter3.png', file.read())




file_path = "kogswell.epub"

# Create a Path object and use the unlink() method to delete the file
file = Path(file_path)
if file.is_file():
    file.unlink()
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} did not exist.")

book.save(file_path)