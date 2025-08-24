import csv
import datetime
import os

def filter_and_save_ulty_data(input_filename, output_filename):
    """
    Reads a CSV file, filters for rows where the 'Fund' column is 'ULTY',
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
            header = next(reader)
            
            # Process the remaining rows.
            for row in reader:
                # Assuming the 'Fund' column is the second column (index 1).
                # Check for "ULTY" in the second element of the row.
                if len(row) > 1 and row[1].strip() == 'ULTY':
                    filtered_rows.append(row)
        
        # Check if any data was found before trying to write to a new file.
        if not filtered_rows:
            print(f"No rows found with 'ULTY' in the '{header[1]}' column. No output file will be created.")
            return

        # Write the filtered data to the new output file.
            
            # Write the header row first.
            writer.writerow(header)
            
            # Write all the filtered rows.
            writer.writerows(filtered_rows)
        
        print(f"Successfully filtered data and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please ensure the file is in the correct directory.")
    except IndexError:
        print("Error: The CSV file format is unexpected. Ensure it has at least two columns.")

# --- How to use this script ---
# Dynamically generate the filename with today's date.
today_date = datetime.date.today().strftime("%Y-%m-%d")
input_file = f"intraday-{today_date}.csv"
output_file = f"ULTY_intraday-{today_date}.csv"

# Check if the output file already exists before running the filtering process.
if os.path.exists(output_file):
    print(f"The output file '{output_file}' already exists. Skipping the process.")
else:
    # Call the function to run the filtering and saving process.
    filter_and_save_ulty_data(input_file, output_file)
