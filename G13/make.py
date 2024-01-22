import mkepub

from pathlib import Path

file_path = "kogswell.epub"

# Create a Path object and use the unlink() method to delete the file
file = Path(file_path)
if file.is_file():
    file.unlink()
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} does not exist.")




book = mkepub.Book(title='The kogswell Book', author='MG')

c01 = book.add_page('Chapter 1', 'And so the book begins.')
c02 = book.add_page('Chapter 2', 'And so the book begins.')

#child = book.add_page('Chapter 1.1', 'Nested TOC is supported.', parent=first)
#book.add_page('Chapter 1.1.1', 'Infinite nesting levels', parent=child)
#book.add_page('Chapter 1.2', 'In any order you wish.', parent=first)

#book.add_page('Chapter 2', 'Use <b>html</b> to make your text <span class="pink">prettier</span>')

# book.add_page('Chapter 3: Images', '<img src="images/chapter3.png" alt="You can use images as well">')
# as long as you add them to the book:
# with open('chapter3.png', 'rb') as file:
    #book.add_image('chapter3.png', file.read())






book.save(file_path)