import requests
from bs4 import BeautifulSoup
import datetime
import os

# URL that hosts the iframe
url = "https://www.yieldmaxetfs.com/ym/intraday-file"

# Folder where you want to save files
save_folder = "/home/mnt/Download2/docs/Financial/YM/intraday_files"

# Make sure folder exists
os.makedirs(save_folder, exist_ok=True)

# Step 1: Get the page HTML
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

# Step 2: Find the iframe
iframe = soup.find("iframe")
csv_url = iframe["src"]

print("CSV link:", csv_url)

# Step 3: Download the CSV
csv_resp = requests.get(csv_url)

# Add current date to filename
today = datetime.datetime.now().strftime("%Y-%m-%d")
filename = os.path.join(save_folder, f"intraday-{today}.csv")

with open(filename, "wb") as f:
    f.write(csv_resp.content)

print(f"Downloaded {filename}")
