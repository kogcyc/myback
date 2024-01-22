import sys
import requests
import zipfile
import io
import os

def download_and_extract_zip(url, extract_dir):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        zip_data = io.BytesIO(response.content)  # Convert response content to bytes-like object
        with zipfile.ZipFile(zip_data, 'r') as zip_ref:
            extracted_files = []
            for file_info in zip_ref.infolist():
                extracted_file = zip_ref.read(file_info)
                extracted_files.append((file_info.filename, extracted_file))
            
            # Create the extraction directory if it doesn't exist
            os.makedirs(extract_dir, exist_ok=True)
            
            # Write extracted binary files to the specified directory
            for filename, content in extracted_files:
                file_path = os.path.join(extract_dir, filename)
                with open(file_path, 'wb') as f:
                    f.write(content)
            
            return extracted_files
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <extract_directory>")
        sys.exit(1)

    url = sys.argv[1]
    extract_dir = sys.argv[2]
    
    extracted_files = download_and_extract_zip(url, extract_dir)

    if extracted_files is not None:
        print("Files extracted and saved to:", extract_dir)
