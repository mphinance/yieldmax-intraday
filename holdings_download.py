import requests
import datetime
import os
import shutil

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
save_path_dated = os.path.join(save_folder, new_filename)

# --- NEW CODE ADDITION ---
# Define the path for the "Latest" version of the file.
save_path_latest = os.path.join(save_folder, f"{filename}-Latest{file_extension}")
# --- END NEW CODE ADDITION ---

try:
    # Step 1: Download the CSV file
    response = requests.get(url)

    # Check if the download was successful
    response.raise_for_status()

    # Step 2: Save the CSV content to the dated file
    with open(save_path_dated, "wb") as f:
        f.write(response.content)

    print(f"Successfully downloaded and saved {new_filename} to {save_folder}")

    # --- NEW CODE ADDITION ---
    # Step 3: Copy the newly saved dated file to the "Latest" path.
    shutil.copyfile(save_path_dated, save_path_latest)

    print(f"Also saved a copy to {os.path.basename(save_path_latest)}")
    # --- END NEW CODE ADDITION ---

except requests.exceptions.RequestException as e:
    print(f"An error occurred while downloading the file: {e}")
except FileNotFoundError:
    print(f"An error occurred while copying the file. Please ensure '{save_path_dated}' exists.")
