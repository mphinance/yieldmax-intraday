import csv
import os

def combine_files(fund_ticker):
    """
    Combines data from the latest intraday CSV file and the latest holdings CSV file
    for a specified fund. It adds an "Exec Price" column as "Cost Basis"
    to the holdings data based on matching Tickers.

    Args:
        fund_ticker (str): The ticker symbol for the fund (e.g., 'ULTY', 'SLTY').
    """
    # Define file paths based on the fund ticker
    base_dir = "/home/mnt/Download2/docs/Financial/YM"
    intraday_file_path = os.path.join(base_dir, "intraday_files", f"{fund_ticker}_intraday-Latest.csv")
    holdings_file_path = os.path.join(base_dir, "holdings_files", f"TidalETF_Services.40ZZ.A4_Holdings_{fund_ticker}-Latest.csv")
    combined_file_path = os.path.join(base_dir, f"{fund_ticker}_Combined_Latest.csv")

    intraday_data = {}
    holdings_data = []

    try:
        # Step 1: Read intraday data into a dictionary for easy lookup
        with open(intraday_file_path, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            ticker_index = header.index('Ticker')
            price_index = header.index('Exec Price')
            for row in reader:
                if row:
                    ticker = row[ticker_index].strip().upper()
                    exec_price = row[price_index].strip()
                    # Use a list to handle multiple entries for the same ticker
                    if ticker not in intraday_data:
                        intraday_data[ticker] = []
                    intraday_data[ticker].append(exec_price)

        # Step 2: Read holdings data and match with intraday data
        with open(holdings_file_path, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            holdings_header = next(reader)
            # Add the new column to the header
            if "Cost Basis" not in holdings_header:
                holdings_header.append("Cost Basis")
            holdings_data.append(holdings_header)

            # CORRECTED: Use 'CUSIP' as the matching column
            cusip_col_index = holdings_header.index('CUSIP')

            for row in reader:
                if row:
                    cusip_value = row[cusip_col_index].strip().upper()
                    cost_basis = ""
                    
                    # Find a direct match with the intraday data ticker
                    if cusip_value in intraday_data:
                        prices = intraday_data[cusip_value]
                        cost_basis = "; ".join(prices)
                    
                    row.append(cost_basis)
                    holdings_data.append(row)

        # Step 3: Write the combined data to a new CSV file
        with open(combined_file_path, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(holdings_data)

        print(f"Successfully combined data and saved to '{combined_file_path}'.")

    except FileNotFoundError as e:
        print(f"Error: A required file was not found: {e}.")
    except ValueError as e:
        print(f"Error processing CSV files: {e}. Check if the header columns are correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- How to use this script ---
# Example for a specific fund, like 'ULTY'
combine_files('ULTY')