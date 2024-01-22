import os
import re

def find_files_by_extension(directory_path, extension):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return []

    # Compile a regular expression pattern for valid file names
    valid_filename_pattern = re.compile(r'^[a-zA-Z0-9_]+\.' + re.escape(extension) + '$')

    # List to store valid file names
    valid_filenames = []

    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        # Check if it's a file with the given extension
        if filename.endswith(extension):
            # Check if the file name matches the pattern
            if valid_filename_pattern.match(filename):
                valid_filenames.append(filename)

    return valid_filenames

# Example usage
directory_path = './slugs'
file_extension = 'slug'  # Change this to your desired extension
result = find_files_by_extension(directory_path, file_extension)

print("Valid file names:")
print(result)



#def tt(slug):
# open and read slug file
# extract frontmatter into variables
# apply variables to slug_md
# save stuff as slug.slg
# apply stuff to layout
# save layout_stuff to slug.html
