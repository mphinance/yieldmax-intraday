# csv_downloader.py

import requests
import datetime
import os

# The URL of the CSV file to download.
# The original URL was a webpage containing an iframe that linked to the actual CSV file.
# This is the direct link to the CSV data on Google Sheets.
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT28cQMYy4k0UD9DbpVVeg2EDIDNCurCeqenrDZfX849izXsk0sBGC1yfDKOeIkre0Ec9hRQ0i1Q_jn/pub?gid=0&single=true&output=csv"

# --- Main function to download and save the file ---
def download_csv():
    """
    Downloads a CSV file from a specified URL and saves it
    with the current date as the filename.
    """
    print("Starting CSV download process...")

    # Get the current date in YYYY-MM-DD format.
    today = datetime.date.today()
    date_string = today.strftime("%Y-%m-%d")

    # Define the filename and file path.
    # The new file will be named, for example, 'intraday-2023-10-27.csv'
    filename = f"intraday-{date_string}.csv"
    
    # Use a try-except block to handle potential errors during the download.
    try:
        # Send an HTTP GET request to the URL.
        # The stream=True parameter is useful for large files to avoid
        # loading the entire content into memory at once.
        response = requests.get(CSV_URL, stream=True)
        
        # Check if the request was successful (status code 200).
        response.raise_for_status()
        
        # Open the file in binary write mode ('wb').
        # Using 'with' ensures the file is closed automatically.
        with open(filename, 'wb') as file:
            # Write the content of the response to the new file in chunks.
            # This is more memory-efficient for large files.
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Successfully downloaded and saved the file as '{filename}'.")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., connection refused, timeout).
        print(f"Error during download: {e}")
    except IOError as e:
        # Handle file I/O errors (e.g., permission denied).
        print(f"Error saving the file: {e}")
    except Exception as e:
        # Handle any other unexpected errors.
        print(f"An unexpected error occurred: {e}")


# --- Entry point of the script ---
if __name__ == "__main__":
    download_csv()
