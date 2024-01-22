import os

def list_files_and_directories(directory):
    for root, dirs, files in os.walk(directory):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            print(f"Directory: {dir_path}")
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"File: {file_path}")

if __name__ == "__main__":
    directory_to_list = "/path/to/your/directory"
    
    list_files_and_directories(directory_to_list)
