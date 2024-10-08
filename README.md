# IPO Alert

## Description

This Python script extracts information about ongoing IPOs from a specified webpage, checks if any new IPOs have become active today, and sends alerts to a Telegram group. The script is scheduled to run at specified intervals.

## Features

- **Web Scraping:** Utilizes BeautifulSoup for scraping IPO information from the provided webpage.
- **Date Checking:** Verifies if an IPO is currently open based on its open and close dates.
- **Telegram Alert:** Sends alerts to a Telegram channel if new IPOs are found, using a specified Telegram bot.
- **CSV Tracking:** Maintains a CSV file to keep track of previously alerted IPOs and avoids duplicate alerts.

## Schedule

To ensure timely alerts, it is recommended to schedule the script to run everyday. Here are the steps to schedule the script:

### Cloud Hosting (Free or Paid):

1. Deploy the script on a cloud platform (e.g., AWS - Lambda with Amazon EventBridge, GCP - Cloud Function with CLoud Scheduler, Azure - Azure Functions with Timer Trigger).
2. Set up a cron job to run the script at desired intervals.

### Free Alternative: [PythonAnywhere](https://www.pythonanywhere.com/):

1. Create a free account on PythonAnywhere.
2. Upload your script and required files.
3. Use the PythonAnywhere task scheduler to run the script daily.

### Scheduling on Windows or Raspberry Pi (Free):

1. Ensure Python is installed on your Windows laptop or Raspberry Pi.
2. Schedule a task using the Task Scheduler on Windows or cron jobs on Raspberry Pi to execute the script at your desired frequency.

## Telegram Setup

1. **Create a Telegram Bot:**
   - Use [BotFather](https://t.me/BotFather) to create a new bot.
   - Save the API Token.

2. **Get Telegram Channel ID:**
   - Create a channel on Telegram.
   - Add your bot and use [GetIDBot](https://t.me/getidsbot) to find the ID.

3. **Set Up in Script:**
   - Install required Python packages: `pip install python-telegram-bot python-dotenv`.
   - Create a `.env` file in the script directory:
     ```dotenv
     API_KEY=your_bot_api_key
     CHANNEL_ID=your_group_or_channel_id
     ```

4. **Modify Telebot Script:**
   - Copy the provided `ipo_alert` function into your script.
   - Customize it as needed.

5. **Telegram Channel Invitation:**
   - If you want to join my channel for latest IPO alerts, [click here](https://t.me/ipoalert97).

## Usage

1. **Environment Setup:**
   - Install the required Python packages using `pip install -r requirements.txt`.
   - Ensure you have a valid `.env` file with necessary environment variables (IPO_LINK, CSV, APP_LINK).
     
2. **Database Setup:**
   - Ensure that the SQLite database (ipo_alert_system.db) is properly set up. The script will insert new IPOs into the database and update their status after sending alerts.
   - Use the below table schema as a reference:
### Table Schema
| Column Name | Data Type | Description                         |
|-------------|-----------|-------------------------------------|
| id          | INTEGER   | Primary Key, Auto-Increment         |
| ipo_name    | TEXT      | Name of the IPO (NOT NULL)          |
| open_dt     | DATE      | IPO opening date                    |
| close_dt    | DATE      | IPO closing date                    |
| status      | BIT       | Status of IPO alert (0 = Not Sent, 1 = Sent) |

4. **Schedule Script:**
   - Set up a scheduler to run the script at specified intervals (daily is recommended).

5. **Alerts:**
   - When new IPOs are detected, the script sends alerts with IPO details to the Telegram group.

## Files

- `telegram_bot.py`: Contains Telegram alert function.
- `main.py`: Main script for IPO data extraction and alerting.
- `db_utils.py`: Contains database function
- `requirements.txt`: List of required Python packages.
- `.env.example`: Example environment variable file.

## Note

- Regularly check for updates or modifications based on the source webpage's structure. Ensure the script adapts to any changes in the HTML structure of the webpage to maintain accurate data extraction and alerts.

