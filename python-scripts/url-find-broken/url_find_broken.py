import pandas as pd
import requests
from tqdm import tqdm
import os

# Read the CSV file
df = pd.read_csv('urls.csv')

# Assume the CSV has a column named 'url'
urls = df['url'].tolist()

# Initialize a dictionary to store URLs by their response code
response_dict = {}

# Check each URL with a progress bar
for url in tqdm(urls, desc="Processing URLs", unit="url"):
    try:
        response = requests.head(url, allow_redirects=True)
        status_code = response.status_code

        # Group URLs by status code
        if status_code != 200:
            if status_code not in response_dict:
                response_dict[status_code] = []
            response_dict[status_code].append(url)
    except requests.RequestException as e:
        print(f"Error checking URL {url}: {e}")

# Create a CSV file for each response code
for status_code, url_list in response_dict.items():
    output_df = pd.DataFrame(url_list, columns=['url'])
    output_filename = f"response_{status_code}.csv"
    output_df.to_csv(output_filename, index=False)
    print(f"Created {output_filename} with {len(url_list)} URLs.")

print("Processing complete.")
