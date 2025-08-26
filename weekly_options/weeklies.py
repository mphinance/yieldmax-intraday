import requests
import os
from datetime import datetime
import csv

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

def compare_files(old_file_path, new_file_path):
    """
    Compares two CSV files to find new items.
    """
    # Check if the old file exists
    if not os.path.exists(old_file_path):
        print(f"Previous day's file '{old_file_path}' not found. Cannot compare.")
        return

    try:
        # Read the content of the old file
        with open(old_file_path, 'r', encoding='utf-8') as f:
            old_items = set(row[0] for row in csv.reader(f))

        # Read the content of the new file
        with open(new_file_path, 'r', encoding='utf-8') as f:
            new_items = set(row[0] for row in csv.reader(f))
        
        # Find the new items by taking the difference between the two sets
        newly_added = new_items - old_items

        if newly_added:
            print("\nNewly added items:")
            for item in newly_added:
                print(item)
        else:
            print("\nNo new items were added today.")
    except Exception as e:
        print(f"An error occurred during file comparison: {e}")

def filter_csv_to_equities(input_file, output_file):
    """
    Reads the input CSV, filters for the 'Equities' section, and saves the output.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            in_equities_section = False
            for row in reader:
                # The section header for Equities is "Available Weeklys - Equity"
                if len(row) > 0 and row[0].strip() == 'Available Weeklys - Equity':
                    in_equities_section = True
                    continue
                # Stop if we hit the next section
                if in_equities_section and len(row) > 0 and row[0].strip().startswith('Available Weeklys -'):
                    break
                # If we are in the equities section, write the row
                if in_equities_section:
                    writer.writerow(row)
        print(f"Filtered equities data saved to '{output_file}'")
    except Exception as e:
        print(f"Error filtering CSV: {e}")

# --- Main Script Execution ---

# Define the full paths for the files
current_date = datetime.now().strftime('%Y-%m-%d')
full_csv_file = os.path.join(os.getcwd(), 'CBOE_Weeklies_Full.csv')
dated_equities_file = os.path.join(os.getcwd(), f'CBOE_Weeklies_Equities_{current_date}.csv')
latest_equities_file = os.path.join(os.getcwd(), 'CBOE_Weeklies_Equities_Latest.csv')

# Step 1: Download the complete, unfiltered CSV
print("Downloading the full CSV file...")
download_csv(url, full_csv_file)

# Step 2: Compare the newly downloaded full file with the previous "Latest" file
# This comparison is based on the full file content, not just equities
print("\nComparing with previous file for changes...")
compare_files(latest_equities_file, full_csv_file)

# Step 3: Filter the full CSV to keep only the equities data
print("\nFiltering for Equities data...")
filter_csv_to_equities(full_csv_file, dated_equities_file)
filter_csv_to_equities(full_csv_file, latest_equities_file)

print("\nProcess completed.")
