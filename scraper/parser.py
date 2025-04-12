from bs4 import BeautifulSoup


class QuoteParser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def parse_quotes(self):
        quotes_data = []

        quote_elements = self.soup.find_all('div', class_='quote')

        for quote_div in quote_elements:
            try:
                # 1. Using .find()
                text = quote_div.find('span', class_='text').get_text(strip=True)

                # 2. Using .select() (CSS selector)
                author = quote_div.select('small.author')[0].get_text(strip=True)

                # 3. Using .find_all()
                tags = [tag.get_text(strip=True) for tag in quote_div.find_all('a', class_='tag')]

                # 4. Navigating nested info
                author_link = quote_div.find('a')['href']
                author_link = f"https://quotes.toscrape.com{author_link}"  # Full URL

                quotes_data.append({
                    'text': text,
                    'author': author,
                    'tags': tags,
                    'author_link': author_link
                })
            except Exception as e:
                print(f"[!] Error parsing quote: {e}")
                continue

        return quotes_data
