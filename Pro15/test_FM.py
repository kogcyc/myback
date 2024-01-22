from frontmatter import Frontmatter

post = Frontmatter.read_file('testfile.md')

fm = post['attributes']
content = post['body']

print(fm['title']
