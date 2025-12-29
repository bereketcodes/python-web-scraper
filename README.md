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
![alt text](image-3.png)  
 ![alt text](image-2.png)
 ![alt text](image-1.png)  