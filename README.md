# 📚 E-Commerce Inventory Scraper 

An automated Python tool designed to extract deep-level product data from the 'Books to Scrape' catalog. 

## 🌟 Features
- **Deep Scraping:** Visits each of the 200 individual product pages to extract full descriptions.
- Excel Optimized:** Uses `utf-8-sig` encoding to ensure currency symbols (£) display perfectly in Excel.
- **Throttling:** Integrated `time.sleep` with random intervals to mimic human behavior (Ethical Scraping).
- **Clean Output:** Generates a sanitized CSV report with headers ready for business analysis.

## 🛠️ Tech Stack
- **Python 3**
- **BeautifulSoup4** (Parsing)
- **Requests** (HTTP)
- **CSV Module** (Data Export)

## 📊 Data Extracted
- Product Name
- Unit Price (Preserved formatting)
- Stock Availability
- 100-character Description Summary
- Reference URL

Header Optimization:** Dark-themed headers with 'Freeze Panes' enabled for seamless navigation of 200+ rows. 
 <img width="1828" height="658" alt="image" src="https://github.com/user-attachments/assets/4b598802-cbe9-4e8b-b812-f4ffb9368b1c" />
 <img width="1861" height="693" alt="image" src="https://github.com/user-attachments/assets/82923c0d-2ac2-4caa-beb0-9f77604e6725" />
 <img width="1866" height="675" alt="image" src="https://github.com/user-attachments/assets/84b7bb37-dd8a-4dfb-870d-b4f78494b75b" />


