# ftx-compound-lending
Simple Python script that leverages FTX Rest API to compound margin lending.

## Disclaimer
Any action you take upon the information in this repository is strictly at your own risk. I will not be liable for any losses.

## What this will help you do
- This script will connect to your FTX account and max out funds for lending for any coins already being lent.
- As such, the script will allow you to compound interest.
- The script will only be able to run when the machine it is on is powered on and connected to the internet.

## What you will need
- A Linux/MacOS/Windows environment with Python 3+
- An FTX account with API key and API secret
- A copy of this repo:
  - `ftx.py`
  - `compound_lending.py`

## Set-up
1) Install the Python module `requests` using pip. Example for Python 3: `python3 -m pip install requests`
2) Copy `ftx.py` and `compound_lending.py` to a working folder of your choice
3) Edit `compound_lending.py` with your own API key & secret
```
api = "YOUR_API_KEY"
secret = "YOUR_SECRET"
```

**WARNING: DO NOT SHARE YOUR API KEY AND SECRET WITH ANYONE AND KEEP THEM SAFE.
Your API key and secret enable full access to your FTX account and funds.**

4) Test run `compound_lending.py`. Example for Python3: `python3 compound_lending.py`
5) Validate that the script ran properly in the console and log file `log.txt`
6) Schedule the script to run at the desired schedule. For example hourly.
    - Windows: https://www.google.com/search?q=windows+schedule+python+script
    - Linux: https://www.google.com/search?q=linux+schedule+python+script
    - MacOS: https://www.google.com/search?q=macos+schedule+python+script
