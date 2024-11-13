import requests
import time
import csv
from bs4 import BeautifulSoup

# Load usernames from file
file_path = 'usernames.txt'
output_file = 'admin_scores.csv'

with open(file_path, 'r', encoding='utf-8') as file:
    usernames = [line.strip() for line in file.readlines()]

# Load already processed usernames from the CSV file to avoid duplicate processing
processed_users = set()
try:
    with open(output_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            processed_users.add(row['username'])
except FileNotFoundError:
    # If the file doesn't exist, we'll create it when saving the results
    pass

# Define base URL for XTools admin score
base_url = "https://xtools.wmcloud.org/adminscore/en.wikipedia.org/{}"

# Custom headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://xtools.wmcloud.org/",
}

# Function to get admin score for a user
def get_admin_score(username):
    try:
        url = base_url.format(username)
        response = requests.get(url, headers=headers)
        
        # Check if rate-limited
        if response.status_code == 429:
            print("Rate limited! Waiting 5 minutes before retrying...")
            time.sleep(300)  # Wait 5 minutes
            response = requests.get(url, headers=headers)  # Retry after waiting
        
        response.raise_for_status()

        # Parse HTML to find the Total score using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        total_score_element = soup.find('th', text='Total')
        total_score = total_score_element.find_next('th').text.strip() if total_score_element else "N/A"
        
        print(f"Fetched score for {username}: Total = {total_score}")
        return {"username": username, "total_score": total_score}
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch score for {username}: {e}")
        return {"username": username, "total_score": "N/A"}

# Append results to CSV file
def save_to_csv(data, file_path):
    file_exists = False
    try:
        # Check if file exists to write headers only once
        with open(file_path, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['username', 'total_score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header only if file doesn't already exist
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

# Process all usernames, skipping the already processed ones
# Specify which mod result you want to process (0, 1, 2, 3, or 4)

# Mod 0 = Malen
# Mod 1 = Gal
# Mod 2 = Tallula
# Mod 3 = Eds
# Mod 4 = Benoit

<<<<<<< HEAD
mod_value = 3  # Change this to 1, 2, 3, or 4 as needed
=======
mod_value = 4  # Change this to 1, 2, 3, or 4 as needed
>>>>>>> 9d54725498d520794eff4501c72fdc5193aeabcd

for i, username in enumerate(usernames):
    # Process usernames where the index mod 5 matches the specified mod_value
    if i % 5 != mod_value:
        continue
    
    # Check if the username has already been processed
    if username in processed_users:
        print(f"Skipping {username}, already processed.")
        continue
    
    # Process the username
    result = get_admin_score(username)
    save_to_csv(result, output_file)
    print(f"Processed {username} with index {i}")
    
    # Be kind to the server
    time.sleep(1)
