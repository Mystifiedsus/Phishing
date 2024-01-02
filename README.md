Phishing URl Downloader
Overview
This Python script is designed to download data from specified URLs and save it to text files. It uses the requests library to make HTTP GET requests, fetches data, and saves it to files. The filenames are generated dynamically based on the current date and time.

Requirements
Python 3
requests library (install it using pip install requests)
Usage
Clone or download this repository to your local machine.

Install the required library:

bash
Copy code
pip install requests
Run the script:

bash
Copy code
python data_downloader.py
Configuration
Update the script with the URLs and filenames for the datasets you want to download.

python
Copy code
# URL and filename for the first dataset
url1 = "https://phishunt.io/feed.txt"
filename1 = "phishunt"

# URL and filename for the second dataset
url2 = "https://openphish.com/feed.txt"
filename2 = "openphish"
Result
The script will create text files containing the downloaded data. The filenames will include a timestamp for uniqueness.

Example filenames:

phishunt_2022-01-01_15-30-00.txt
openphish_2022-01-01_15-35-00.txt
Notes
Ensure an active internet connection for successful data retrieval.
The script uses the current date and time for filename uniqueness.
Handle any potential errors gracefully, and refer to the console for status updates.
