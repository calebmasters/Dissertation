import csv
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

extracted_data = []

with open('speeches.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip the header row if present

    for row in reader:
        url = row[1]  # Assuming URLs are in the second column
        try:
            response = requests.get(url, headers=headers)  # Include headers in the request
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Adjust the selectors based on the actual page structure
                title = soup.find('h2').text.strip() if soup.find('h2') else 'Title Not Found'
                content = ' '.join([p.text for p in soup.find_all('div', class_='field-item even')]) if soup.find_all('div', class_='field-item even') else 'Content Not Found'

                extracted_data.append((title, url, content))
                
                time.sleep(1)  # Increase delay to be more polite to the server
            else:
                print(f"Failed to fetch {url} - Status code: {response.status_code}")
        except Exception as e:
            print(f"Error fetching or parsing {url}: {e}")

with open('extracted_speech_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'URL', 'Content'])
    writer.writerows(extracted_data)

print(f"Finished extracting data for {len(extracted_data)} speeches.")
