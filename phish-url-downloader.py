import requests
from datetime import datetime

def download_data(url, filename):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Content of the website
            data = response.text
            
            # Get the current date and time
            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            
            # Create a filename with the current date and time
            filename = f"{filename}_{current_datetime}.txt"
            
            # Save the data to the generated filename
            with open(filename, "w", encoding="utf-8") as file:
                file.write(data)
            
            print(f"Data downloaded successfully and saved as {filename}.")
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

# URL and filename for the first dataset
url1 = "https://phishunt.io/feed.txt"
filename1 = "phishunt"

# URL and filename for the second dataset
url2 = "https://openphish.com/feed.txt"
filename2 = "openphish"

# Call the download_data function for the first URL and filename
download_data(url1, filename1)

# Call the download_data function for the second URL and filename
download_data(url2, filename2)
