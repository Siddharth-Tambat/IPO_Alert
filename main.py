import csv
import datetime
from bs4 import BeautifulSoup
import requests
import pytz
from telegram_bot import ipo_alert 
from dotenv import load_dotenv
import os

load_dotenv()
IPO_LINK = os.getenv('IPO_LINK')
CSV = os.getenv('CSV')
APP_LINK = os.getenv('APP_LINK')

# Today's date in IST
ist_timezone = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist_timezone).date()

# Function to check if an IPO is open
def is_ipo_open(open_date, close_date):
    if (open_date != '') and (close_date != ''):
        open_date_obj = datetime.datetime.strptime(open_date, "%b %d, %Y").date()
        close_date_obj = datetime.datetime.strptime(close_date, "%b %d, %Y").date()
        return open_date_obj <= today <= close_date_obj
    return False

try:
    # Send GET request and parse HTML
    response = requests.get(IPO_LINK)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table element
    table = soup.find('table', class_='table table-bordered table-striped table-hover w-auto')

    # Extract and filter data
    active_ipos = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')

        ipo_name = cells[0].text.strip()
        open_date = cells[1].text.strip()
        close_date = cells[2].text.strip()
        if is_ipo_open(open_date, close_date):
            active_ipos.append({'name': ipo_name, 'open_date': open_date, 'close_date': close_date})

    # Check if IPOs exist in CSV file
    existing_ipos = []
    with open(CSV, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            existing_ipos.append(row['name'])

    # Print and save new IPOs
    new_ipos = [ipo for ipo in active_ipos if ipo['name'] not in existing_ipos]
    if new_ipos:
        for ipo in new_ipos:
            message = f"{ipo['name']} \n---------------------------------------------------------\n Open Date: {ipo['open_date']} \n Close Date: {ipo['close_date']}"
            ipo_alert(message, APP_LINK)

        # Append new IPOs to CSV file
        with open(CSV, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'open_date', 'close_date'])
            writer.writerows(new_ipos)

except Exception as e:
    # Send failure message with the error
    message = f"Error: {str(e)}"
    ipo_alert(message, APP_LINK)
