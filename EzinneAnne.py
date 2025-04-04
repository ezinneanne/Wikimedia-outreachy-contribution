import requests
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Task_2_Intern.csv')
data = pd.read_csv(file_path, delimiter=";")

# Function to get status code
def get_status(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException:
        return "Error"

# loop through the URLs and print their status codes and url
for url in data['urls']:
    status = get_status(url)
    print(f"({status}) {url}")