
#import requests # Keep this to test after the fix
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("URL_FOR_API")
# Make a GET request to the REST API
print(f"Making request to URL: {url}")
response = requests.get(url)
output = response.json()
official_name = output[0]['name']['official']
# Print the response
if response.status_code == 200:
    print(f"Official Name: {official_name}")
else:
    print(f"Error: {response.status_code}") 