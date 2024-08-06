from bs4 import BeautifulSoup
import csv

# The path to the HTML file you provided
html_file_path = '/Users/calebmasters/Library/CloudStorage/OneDrive-Personal/Documents/university/dissertation/coding folder/linguistic analysis/project directory/Web Scraping/html files/links.html'

# The path where you want the CSV to be saved
output_csv_file_path = '/Users/calebmasters/Library/CloudStorage/OneDrive-Personal/Documents/university/dissertation/coding folder/linguistic analysis/project directory/Web Scraping/UNFCCClinks.csv'

# Function to parse the HTML content and write to CSV
def parse_html_to_csv(html_path, csv_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Open the CSV file for writing
    with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Write the headers
        writer.writerow(['Link', 'Language', 'Name of Speech', 'Date'])

        # Iterate over each row in the table body
        for row in soup.select('table tbody tr'):
            # Find the document link and language
            link_tag = row.select_one('a[hreflang]')
            link = link_tag['href'] if link_tag else 'No link available'
            language = link_tag['hreflang'] if link_tag else 'No language specified'

            # Find the name of the speech
            name_of_speech_tag = row.select_one('.views-field-title .documentid')
            name_of_speech = name_of_speech_tag.get_text(strip=True) if name_of_speech_tag else 'No title available'

            # Find the date of the speech
            date_tag = row.select_one('.views-field-field-document-publication-date time')
            date = date_tag['datetime'] if date_tag else 'No date available'

            # Write to CSV
            writer.writerow([link, language, name_of_speech, date])

# Run the function with your file paths
parse_html_to_csv(html_file_path, output_csv_file_path)

print(f"Data has been extracted to {output_csv_file_path}")
