import os
import requests
import zipfile
from tqdm import tqdm
import dvc.api

# URL of the dataset
url = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"

# Local path to save the downloaded zip file
zip_path = "kagglecatsanddogs_5340.zip"

# Directory to extract the dataset
extract_dir = "data"

def download_file(url, filename):
    """Download a file from a URL with a progress bar."""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as progress_bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            progress_bar.update(size)

def extract_zip(zip_path, extract_dir):
    """Extract a zip file to a directory."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

def main():
    # Download the dataset
    print("Downloading dataset...")
    download_file(url, zip_path)

    # Extract the dataset
    print("Extracting dataset...")
    extract_zip(zip_path, extract_dir)

    # Remove the zip file
    os.remove(zip_path)

    print("Dataset downloaded, extracted, and added to DVC successfully!")

if __name__ == "__main__":
    main()