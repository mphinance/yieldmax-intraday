import csv
import datetime
import os

def filter_and_save_slty_data(input_filename, output_filename):
    """
    Reads a CSV file, filters for rows where the 'Fund' column is 'SLTY',
    and saves the filtered rows to a new CSV file.

    Args:
        input_filename (str): The path to the input CSV file.
        output_filename (str): The path for the new output CSV file.
    """
    filtered_rows = []
    try:
        # Open the input CSV file for reading.
        with open(input_filename, 'r', newline='') as infile:
            reader = csv.reader(infile)
            
            # Read and store the header row to include in the output file.
            try:
                header = next(reader)
            except StopIteration:
                print(f"Error: The file '{input_filename}' is empty.")
                return

            # Find the index of the 'Fund' column.
            try:
                fund_column_index = header.index('Fund')
            except ValueError:
                print(f"Error: 'Fund' column not found in the header of '{input_filename}'.")
                return
            
            # Process the remaining rows.
            for row in reader:
                # Check for "SLTY" in the correct column.
                if len(row) > fund_column_index and row[fund_column_index].strip() == 'SLTY':
                    filtered_rows.append(row)
        
        # Check if any data was found before trying to write to a new file.
        if not filtered_rows:
            print(f"No rows found with 'SLTY' in the 'Fund' column. No output file will be created.")
            return

        # Write the filtered data to the new output file.
        # This part has been moved inside a new 'with' block.
        with open(output_filename, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            
            # Write the header row first.
            writer.writerow(header)
            
            # Write all the filtered rows.
            writer.writerows(filtered_rows)
        
        print(f"Successfully filtered data and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please ensure the file is in the correct directory.")
    except IndexError:
        print("Error: The CSV file format is unexpected. Ensure it has the correct number of columns.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- How to use this script ---

# Dynamically generate the filename with today's date.
today_date = datetime.date.today().strftime("%Y-%m-%d")
input_file = f"intraday-{today_date}.csv"

# Define the filenames for the dated and 'Latest' output files.
dated_output_file = f"SLTY_intraday-{today_date}.csv"
latest_output_file = "SLTY_intraday-Latest.csv"

# Check if the dated output file already exists before running the filtering process.
if os.path.exists(dated_output_file):
    print(f"The dated output file '{dated_output_file}' already exists. Skipping the filtering process.")
else:
    # Call the function to run the filtering and saving process for the dated file.
    filter_and_save_slty_data(input_file, dated_output_file)

# Always run the process for the "Latest" file to ensure it's up-to-date.
# This will overwrite the file each time the script is run.
print("\nSaving the latest version...")
filter_and_save_slty_data(input_file, latest_output_file)
