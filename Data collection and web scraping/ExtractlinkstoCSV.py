import csv
from bs4 import BeautifulSoup

# Make sure to provide the correct path to your downloaded HTML file
with open('page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with the class 'custom-press-release' and then find 'a' tags within 'h3'
speech_containers = soup.find_all('div', class_='custom-press-release')
speech_links = []
for container in speech_containers:
    a_tag = container.find('h3').find('a', href=True)
    if a_tag:
        # Complete the URL if it's relative
        full_url = a_tag['href']
        speech_links.append(full_url)
        print(f"Found link: {full_url}")  # This should print out each link found

# Check if we found any links
if not speech_links:
    print("No speech links found.")
else:
    # Write the links to a CSV file
    with open('speeches.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Link"])  # Header
        for link in speech_links:
            writer.writerow([link])  # Write each link as a new row

    print(f"Total speech links found and written to CSV: {len(speech_links)}")

