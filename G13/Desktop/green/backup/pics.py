import os

def get_file_names_in_current_directory():
    current_directory = os.getcwd()
    file_names = os.listdir(current_directory)
    file_names = [file_name for file_name in file_names if os.path.isfile(file_name)]
    file_names = sorted(file_names)
    return file_names

if __name__ == "__main__":
    file_names = get_file_names_in_current_directory()
    print('<body style="background-color: #000;">')
    for fn in file_names:
        print(f'<img src="./{fn}" style="width: 600px;"/><br/><span style="color: #fff; font-family: monospace; font-size: 1em;">{fn}</span><br/><br/>')
    print('</body>')