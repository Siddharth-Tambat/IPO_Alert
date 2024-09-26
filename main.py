import datetime
from bs4 import BeautifulSoup
import requests
import pytz
from telegram_bot import ipo_alert
from dotenv import load_dotenv
import os
# Importing database functions from db_utils
from db_utils import insert_ipo, ipo_exists, update_ipo_status

load_dotenv()
IPO_LINK = os.getenv('IPO_LINK')
APP_LINK = os.getenv('APP_LINK')

# Today's date in IST
ist_timezone = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist_timezone).date()

# Function to check if an IPO is open
def is_ipo_open(open_date, close_date):
    if open_date and close_date:
        open_date_obj = datetime.datetime.strptime(open_date, "%b %d, %Y").date()
        close_date_obj = datetime.datetime.strptime(close_date, "%b %d, %Y").date()
        return open_date_obj <= today <= close_date_obj
    return False

# Main logic to scrape, store, and send alerts
def scrape_and_alert():
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

        # Loop through active IPOs and check if they are already in the database
        for ipo in active_ipos:
            if not ipo_exists(ipo['name'], ipo['open_date']):  # If the IPO doesn't exist, insert and send alert
                insert_ipo(ipo['name'], ipo['open_date'], ipo['close_date'], status=0)
                message = f"{ipo['name']} \n---------------------------------------------------------\n Open Date: {ipo['open_date']} \n Close Date: {ipo['close_date']}"
                ipo_alert(message, APP_LINK)
                update_ipo_status(ipo['name'])  # Mark the IPO as alerted

    except Exception as e:
        # Send failure message with the error
        message = f"Error: {str(e)}"
        ipo_alert(message, APP_LINK)

# Run the IPO alert system
if __name__ == '__main__':
    scrape_and_alert()
