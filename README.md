# Quote Scraper - Web Scraping Project

A Python-based web scraper for collecting quotes and author data from [quotes.toscrape.com](http://quotes.toscrape.com/). This tool efficiently scrapes multiple pages, parses quote and author details, saves the results, analyzes them, and presents insights using a GUI.

## 🔧 Features

- **Web Scraping**:
  - Extracts quotes, authors, tags, and author profile links.
  - Follows pagination across all quote pages.
  - Respects `robots.txt` with delay and user-agent headers.

- **Data Modeling**:
  - Structured classes (`Quote`, `Author`) to hold scraped data.

- **Data Analysis**:
  - Finds most common tag.
  - Identifies most quoted author.
  - Calculates average number of tags per quote.

- **Data Export**:
  - Supports saving to both JSON and CSV.

- **GUI Application**:
  - Displays data in a table format.
  - Shows statistical analysis.
  - Visualizes top 10 tags using a bar graph.

## 📁 Project Structure
``` bash 
Python-Web-Scraping-Midterm-Project/
├── models/
│   └── data_models.py         # Quote and Author data classes
├── scraper/
│   ├── collector.py           # Handles all scraping logic
│   └── parser.py              # Parses HTML using BeautifulSoup
├── utils/
│   ├── analyzer.py            # Analyzes scraped quote data
│   ├── file_handler.py        # JSON/CSV read and write helpers
│   └── gui.py                 # Tkinter-based GUI to display and visualize
├── main.py                    # Main script to run scraping and saving
├── requirements.txt
└── README.md

```



## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/quote-scraper.git
cd Python-Web-Scraping-Midterm-Project
pip install -r requirements.txt
```
## 🚀 Usage
To run the scraper and save data:

``` bash
python main.py
```
To launch the GUI:
```bash 
python utils/gui.py
```

## 📊 Output
Data will be saved to the output/ directory as:

- quotes.json: All quotes in JSON format

- quotes.csv: Quotes exported to CSV

## 🛠️ Technologies Used
- requests: For making HTTP requests

- BeautifulSoup4: For parsing HTML

- tkinter: For GUI interface

- matplotlib: For data visualization

- pandas: For handling and displaying tabular data

## 📌 Notes
- Rate-limiting is handled with a 1-second delay between page requests.


