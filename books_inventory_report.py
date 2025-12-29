import requests
from bs4 import BeautifulSoup
import csv
import time
import random

# System Configuration
BASE_URL = "https://books.toscrape.com/catalogue/"
REPORT_NAME = "books_inventory_200_report.csv"


def fetch_page_content(url):
    """Handles HTTP requests with integrated error logging."""
    try:
        # Optimized browser headers for stability
        browser_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=browser_headers, timeout=12)
        if response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")
    except Exception as error:
        print(f"Network Alert: {error}")
    return None


def get_detailed_summary(link):
    """Extracts specific product descriptions from individual item pages."""
    page_soup = fetch_page_content(link)
    if not page_soup:
        return "N/A"

    # Targeted extraction of the product overview paragraph
    content_area = page_soup.find("div", id="product_description")
    if content_area:
        full_text = content_area.find_next("p").text.strip()
        # Data sanitization for clean CSV formatting
        return (full_text[:95] + '...') if len(full_text) > 100 else full_text
    return "No description found"


def run_inventory_extraction(total_pages=10):
    """Primary engine to iterate through catalog pages and build inventory."""
    print(f"Initiating automated extraction for approximately {total_pages * 20} items...")
    inventory_data = []

    for page_num in range(1, total_pages + 1):
        # Dynamic URL construction for pagination
        current_url = f"{BASE_URL}page-{page_num}.html"
        print(f"\n--- Accessing Catalog Page {page_num} ---")

        soup = fetch_page_content(current_url)
        if not soup:
            print(f"Skipping page {page_num} due to connection error.")
            continue

        # Locate product containers in the main display grid
        product_grid = soup.find_all("article", class_="product_pod")

        for item in product_grid:
            try:
                # Primary data extraction
                name = item.h3.a["title"]
                cost = item.find("p", class_="price_color").text
                stock_status = item.find("p", class_="instock availability").text.strip()

                # URL normalization for deep-level sub-page scraping
                relative_path = item.h3.a["href"].replace("catalogue/", "")
                target_url = f"{BASE_URL}{relative_path}"

                print(f"Processing Item: {name[:25]}")

                # Navigate to product page for the description
                info_summary = get_detailed_summary(target_url)

                inventory_data.append({
                    "Product Name": name,
                    "Unit Price": cost,
                    "Availability": stock_status,
                    "Description Summary": info_summary,
                    "Reference URL": target_url
                })

                # Ethical request throttling (Human-like delay)
                time.sleep(random.uniform(0.6, 1.2))


            except (AttributeError, KeyError) as e:

                print(f"Data missing for an item, skipping: {e}")

                continue

                # Finalize data export to CSV format
    if inventory_data:
        field_names = inventory_data[0].keys()
        with open(REPORT_NAME, "w", newline="", encoding="utf-8-sig") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(inventory_data)
        print(f"\nSuccess. {len(inventory_data)} entries exported to {REPORT_NAME}.")


if __name__ == "__main__":
    # Execute build for 10 pages (20 books per page = 200 books)
    run_inventory_extraction(total_pages=10)