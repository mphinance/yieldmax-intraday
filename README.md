### README for `mphinance/yieldmax-intraday`

This directory contains scripts and data related to the automated downloading and tracking of financial data for YieldMax ETFs. The project is designed to periodically fetch holdings and intraday data and commit the changes to a Git repository.

#### Project Structure
* `daily_push.sh`: A shell script for automating the Git commit and push process. It adds all new and modified files, creates a dated commit message, and pushes to the remote repository.
* `holdings_download.py`: A Python script that downloads the daily holdings CSV file for the `ULTY` ETF from the YieldMax website and saves it to the `holdings_files` directory with a dated filename.
* `holdings_files/`: This directory stores the downloaded holdings data. An example file is `TidalETF_Services.40ZZ.A4_Holdings_ULTY-2025-08-24.csv`.
* `intraday_download.py`: A Python script that scrapes the YieldMax website to find the Google Sheets iframe URL and then downloads the intraday data as a CSV file.
* `intraday_cron.log`: A log file that tracks the execution of the `intraday_download.py` script, showing the CSV link and the downloaded file name.
* `intraday_files/`: This directory contains the downloaded intraday data.
