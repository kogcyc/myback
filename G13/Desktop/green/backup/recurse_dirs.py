import os
import shutil

def find_and_copy_files(source_dir, destination_dir, extension_list):
    for root, dirs, files in os.walk(source_dir):
        for file_name in files:
            file_extension = os.path.splitext(file_name)[1].lower()
            if file_extension in extension_list:
                source_file = os.path.join(root, file_name)
                destination_subdir = os.path.join(destination_dir, os.path.basename(root))
                destination_file = os.path.join(destination_subdir, file_name)
                
                if not os.path.exists(destination_subdir):
                    os.makedirs(destination_subdir)
                    
                shutil.copy2(source_file, destination_file)
                print(f"Copied file: {destination_file}")

if __name__ == "__main__":
    source_directory = "/home/matt"
    destination_directory = "/media/matt/Elements/recurse"
    extension_list = [".txt", ".py", ".svg", ".css", ".html", ".jpg", ".png", ".jpeg"]
    
    find_and_copy_files(source_directory, destination_directory, extension_list)
