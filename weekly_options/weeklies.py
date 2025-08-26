import requests
import os
from datetime import datetime

# The URL to the direct CSV download
url = 'https://www.cboe.com/available_weeklys/get_csv_download/'

def download_csv(download_url, save_path):
    """
    Downloads a file from a given URL and saves it to a specified path.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(download_url)
        # Check if the request was successful
        response.raise_for_status()

        # Open the file in binary write mode and save the content
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"File successfully downloaded and saved as '{save_path}'")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except IOError as e:
        print(f"Error saving file: {e}")

# Get the current date and format it as a string (YYYY-MM-DD)
current_date = datetime.now().strftime('%Y-%m-%d')

# Define the filenames
dated_file_name = f'CBOE_Weeklies_{current_date}.csv'
latest_file_name = 'CBOE_Weeklies_Latest.csv'

# Define the full paths where you want to save the files
dated_save_location = os.path.join(os.getcwd(), dated_file_name)
latest_save_location = os.path.join(os.getcwd(), latest_file_name)

# Download the file with the dated filename
download_csv(url, dated_save_location)

# Download the file with the "Latest" filename
download_csv(url, latest_save_location)
