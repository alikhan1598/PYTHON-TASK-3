[README.md](https://github.com/user-attachments/files/21801104/README.md)
# 📰 News Scraper

A simple Python script that scrapes headlines from [Hacker News](https://news.ycombinator.com/) and saves them to a text file.

## 📌 Features

* Fetches the latest headlines from Hacker News.
* Extracts only meaningful link text (more than 3 words).
* Saves the filtered headlines into a `headlines.txt` file.
* Lightweight and easy to modify for other websites.

## 🛠 Requirements

Make sure you have **Python 3.x** installed along with:

```bash
pip install requests beautifulsoup4
```

## 🚀 Usage

1. Clone or download this script.
2. Open a terminal in the script's folder.
3. Run:

   ```bash
   python news_scraper.py
   ```
4. Check the generated `headlines.txt` file for the scraped headlines.

## 📂 Output

* **File:** `headlines.txt`
* **Content:** Each line contains a headline (only those with more than 3 words).

## ⚠️ Notes

* This script is configured to scrape **Hacker News**.
  To scrape another site, update the `url` variable and adjust HTML parsing logic.
* Be respectful of website terms of service and scraping policies.

