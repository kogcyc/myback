import re

def process_markdown(markdown_text):
    cleaned_text = re.sub(r'[*_`~#]', '', markdown_text)
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)
    cleaned_text = re.sub(r'\b\w*\'\w*\b', '', cleaned_text)
    cleaned_text = cleaned_text.replace('\n', ' ')
    cleaned_list = cleaned_text.lower().split()
    result_string = ' '.join(cleaned_list)
    return result_string

markdown_text = """
# Example Markdown Text

This is some **markdown** text with _formatting_.

You won't believe it, but I can't do it!

"""

processed_text = process_markdown(markdown_text)
print(processed_text)
