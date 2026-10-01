import requests
from bs4 import BeautifulSoup
import csv

def scrape_exchange(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr")
    company_list = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 3:  # First column is the serial number, second is Symbol, third is Company Name
            symbol = cols[1].get_text(strip=True)
            company_name = cols[2].get_text(strip=True)
            company_list.append((symbol, company_name))

    # Save to CSV
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Company Name"])
        writer.writerows(company_list)

    print(f"✅ Data saved to {output_file}")
    return company_list

# Exchange URLs
egx_url = "https://stockanalysis.com/list/egyptian-stock-exchange"
tadawul_url = "https://stockanalysis.com/list/saudi-stock-exchange"

# Call the function for each exchange
egx_companies = scrape_exchange(egx_url, "egx_companies.csv")
tadawul_companies = scrape_exchange(tadawul_url, "tadawul_companies.csv")

# Display a sample from each exchange
print("\n--- EGX Sample ---")
for s, n in egx_companies[:5]:
    print(f"{s} - {n}")

print("\n--- Tadawul Sample ---")
for s, n in tadawul_companies[:5]:
    print(f"{s} - {n}")
