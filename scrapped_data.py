import requests
from bs4 import BeautifulSoup

url = "https://www.zyxware.com/article/6469/list-inc-5000-companies-and-their-websites"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all <td> elements
td_elements = soup.find_all('td')

companies = []

# Iterate over the <td> elements
for i in range(0, len(td_elements), 4):

    company_name = td_elements[i+1].text.strip()
    companies.append(company_name)

# Print the list of company names
for company in companies:
    print(company)
