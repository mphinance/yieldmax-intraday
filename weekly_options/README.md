# CBOE Weeklys CSV Downloader

This is a Python script designed to automatically download the "Available Weeklys" CSV file from the Cboe website, filter it for Equities data, and track changes between daily runs.

### Features

* **Automated Download**: Fetches the latest CSV file directly from Cboe's website.

* **Date-Stamped Files**: Saves a copy of the filtered Equities data with a unique date in the filename for historical archiving (e.g., `CBOE_Weeklies_Equities_YYYY-MM-DD.csv`).

* **"Latest" File**: Creates a separate file named `CBOE_Weeklies_Equities_Latest.csv`, which is overwritten on each run to always contain the most recent data.

* **Change Tracking**: Compares the newly downloaded data with the previous "Latest" file and prints any new items that have been added.

* **Equities Filter**: Automatically filters the large CSV file to include only the "Equities" section.

### How to Use

1. **Dependencies**: This script requires the `requests` library. If you don't have it installed, you can install it using pip:

pip install requests


2. **Running the Script**: Execute the script from your terminal:

python your_script_name.py


(Note: Replace `your_script_name.py` with the actual name of your file.)

### Files Generated

* `CBOE_Weeklies_Full.csv`: A temporary file containing the entire, unfiltered CSV. This file is used for filtering and comparison.

* `CBOE_Weeklies_Equities_YYYY-MM-DD.csv`: A dated file containing only the Equities data.

* `CBOE_Weeklies_Equities_Latest.csv`: A file that always conta