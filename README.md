# IPO Alert

## Description

This Python script extracts information about ongoing IPOs from a specified webpage, checks if any new IPOs have become active today, and sends alerts to a Telegram group. The script is scheduled to run at specified intervals.

## Features

- **Web Scraping:** Utilizes BeautifulSoup for scraping IPO information from the provided webpage.
- **Date Checking:** Verifies if an IPO is currently open based on its open and close dates.
- **Telegram Alert:** Sends alerts to a Telegram group if new IPOs are found, using a specified Telegram bot.
- **CSV Tracking:** Maintains a CSV file to keep track of previously alerted IPOs and avoids duplicate alerts.

## Schedule

To ensure timely alerts, it is recommended to schedule the script to run regularly. Here are the steps to schedule the script:

### Cloud Hosting:

1. Deploy the script on a cloud platform (e.g., AWS, Google Cloud, Azure).
2. Set up a cron job to run the script at desired intervals.

### Free Alternative: [PythonAnywhere](https://www.pythonanywhere.com/):

1. Create a free account on PythonAnywhere.
2. Upload your script and required files.
3. Use the PythonAnywhere task scheduler to run the script daily.

## Usage

1. **Environment Setup:**
   - Install the required Python packages using `pip install -r requirements.txt`.
   - Ensure you have a valid `.env` file with necessary environment variables (IPO_LINK, CSV, APP_LINK).

2. **Telegram Setup:**
   - Create a Telegram bot and obtain the bot token.
   - Add the bot to your Telegram group and obtain the group chat ID.

3. **Schedule Script:**
   - Set up a scheduler to run the script at specified intervals (daily is recommended).

4. **Alerts:**
   - When new IPOs are detected, the script sends alerts with IPO details to the Telegram group.

## Files

- `ipo_alert.py`: Contains Telegram alert function.
- `script.py`: Main script for IPO data extraction and alerting.
- `requirements.txt`: List of required Python packages.
- `.env.example`: Example environment variable file.

## Note

- Regularly check for updates or modifications based on the source webpage's structure. Ensure the script adapts to any changes in the HTML structure of the webpage to maintain accurate data extraction and alerts.

