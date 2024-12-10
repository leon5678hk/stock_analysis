import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://companiesmarketcap.com/cad/tesla/revenue/"

response = requests.get(url)
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")

table = soup.find("table", class_="table")

tsla_revenue = []
for row in table.find("tbody").find_all("tr"):
    columns = row.find_all("td")
    year = columns[0].get_text(strip=True)
    revenue = columns[1].get_text(strip=True)
    change = columns[2].get_text(strip=True)
    tsla_revenue.append({"Year": year, "Revenue": revenue, "Change": change})

tsla_df = pd.DataFrame(revenue_data)

tsla_df.tail()
