"""
Created by: Shingai Dzinotyiweyi

Task 2: Data Scraper
Develop a web scraper to extract specific data from a website
(e.g., news headlines, product prices).

Objectives:
✅ - Use the requests library to retrieve web page content.
✅ - Parse the HTML using BeautifulSoup.
✅ - Extract specific data, such as article titles or product
details.
✅ - Save the scraped data into a CSV file.
"""
import requests
from bs4 import BeautifulSoup
import csv


def get_response(url):
    """
    Searches a website's url and returns an HTML response
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes

        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

website_url = f"https://www.hoopshype.com/salaries/teams/"

response = get_response(website_url)
soup = BeautifulSoup(response.content, 'html.parser')

all_teams = []


for table in soup.find_all('table'):

    try:
        table_headers = table.find('thead')
        table_records = table.find('tbody')

        field_names = []
        for record in table_headers:
            for r in record:
                if r.get_text() != "":
                    field_names.append(r.get_text())
        field_names.insert(0, 'Rank')
        print("Field names:", field_names)


        for record in table_records:
            team_info = {}
            i = 0
            for r in record:
                if r.get_text() != "":
                    print(r.get_text())
                    team_info[field_names[i]] = r.get_text()
                    i += 1
            all_teams.append(team_info)

        # Remove non-team values from list
        all_teams.reverse()
        all_teams = all_teams[:30]
        all_teams.reverse()
        print("All Teams Salary:", all_teams)

    except AttributeError:
        # Skip if any required element is None
        pass

if all_teams:

    # Create new .csv file
    with open("NBA_Team_Salary.csv", "a+", newline="", encoding="utf-8") as write_file:
        write = csv.DictWriter(write_file, fieldnames=field_names, delimiter=',')
        write.writeheader()
        write.writerows(all_teams)
        print("Saved to NBA_Team_Salary.csv")

