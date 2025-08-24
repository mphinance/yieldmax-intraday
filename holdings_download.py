import requests
import datetime
import os

# The direct URL to the CSV file
url = "https://www.yieldmaxetfs.com/bitnami/wordpress/wp-content/fund_files2/files/holdings/TidalETF_Services.40ZZ.A4_Holdings_ULTY.csv"

# The new folder where you want to save the file
save_folder = "/home/mnt/Download2/docs/Financial/YM/holdings_files"

# Make sure the folder exists. If not, create it.
os.makedirs(save_folder, exist_ok=True)

# Get the current date to append to the filename
today = datetime.datetime.now().strftime("%Y-%m-%d")

# The filename will be the original name with the date appended
# The os.path.basename() function extracts the filename from the URL
original_filename = os.path.basename(url)
filename, file_extension = os.path.splitext(original_filename)
new_filename = f"{filename}-{today}{file_extension}"

# Create the full path for the new file
save_path = os.path.join(save_folder, new_filename)

try:
    # Step 1: Download the CSV file
    response = requests.get(url)
    
    # Check if the download was successful
    response.raise_for_status()
    
    # Step 2: Save the CSV content to the file
    with open(save_path, "wb") as f:
        f.write(response.content)
    
    print(f"Successfully downloaded and saved {new_filename} to {save_folder}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while downloading the file: {e}")

