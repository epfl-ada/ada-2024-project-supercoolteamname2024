import requests
import time
import csv
from bs4 import BeautifulSoup

file_path = '../../data/new_usernames.txt'
output_file = '../../data/new_admin_scores.csv'

# Charger les noms d'utilisateur
with open(file_path, 'r', encoding='utf-8') as username_file:
    usernames = [line.strip() for line in username_file.readlines()]

# Charger les utilisateurs déjà traités
processed_users = set()
try:
    with open(output_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            processed_users.add(row['username'])
except FileNotFoundError:
    pass

# URL de base
base_url = "https://xtools.wmcloud.org/adminscore/en.wikipedia.org/{}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# Récupérer le score admin
def get_admin_score(username):
    try:
        url = base_url.format(username)
        response = requests.get(url, headers=headers)
        
        if response.status_code == 429:
            print("Rate limited! Waiting 5 minutes...")
            time.sleep(300)
            response = requests.get(url, headers=headers)

        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        total_score_element = soup.find('th', text='Total')
        if not total_score_element:
            return {"username": username, "total_score": "N/A"}
        total_score = total_score_element.find_next('th').text.strip()
        return {"username": username, "total_score": total_score}
    except Exception as e:
        print(f"Failed to fetch score for {username}: {e}")
        return {"username": username, "total_score": "N/A"}

# Enregistrer les résultats
def save_to_csv(data, file_path):
    file_exists = False
    try:
        with open(file_path, 'r', encoding='utf-8'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(file_path, 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['username', 'total_score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

# Traiter les noms d'utilisateur
for i, username in enumerate(usernames):
    if username in processed_users:
        print(f"Skipping {username}, already processed.")
        continue
    
    result = get_admin_score(username)
    save_to_csv(result, output_file)
    print(f"Processed {username} with index {i}")
    time.sleep(1)
