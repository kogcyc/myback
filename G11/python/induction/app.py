import frontmatter
import markdown

def render_file(input_file, output_file):
    
    post = frontmatter.load(input_file)
    
    # Generate the HTML output
    html_output = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{post["title"]}</title>
    </head>
    <body>
        {markdown.markdown(post.content)}
    </body>
    </html>
    '''
    
    # Write the HTML output to the output file
    with open(output_file, 'w') as f:
        f.write(html_output)

if __name__ == "__main__":
    input_file = "article.md"  # Replace with the path to your input Markdown file
    output_file = "output.html"  # Replace with the desired output HTML file path
    render_file(input_file, output_file)

