import requests
import time
import logging
from urllib.robotparser import RobotFileParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://quotes.toscrape.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; QuoteScraper/1.0)"
}
DELAY = 1


class Scraper:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.robot_parser = RobotFileParser()
        self._check_robots()

    def _check_robots(self):
        robots_url = f"{self.base_url}/robots.txt"
        self.robot_parser.set_url(robots_url)
        try:
            self.robot_parser.read()
            can_fetch = self.robot_parser.can_fetch("*", self.base_url)
            if not can_fetch:
                logger.warning("Scraping is disallowed by robots.txt.")
        except Exception as e:
            logger.error(f"Could not read robots.txt: {e}")

    def fetch_page(self, url):
        try:
            time.sleep(DELAY)  # Rate limiting
            response = self.session.get(url)
            response.raise_for_status()
            logger.info(f"Fetched: {url}")
            return response.text
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            return None

    def fetch_all_pages(self):
        """
        Fetches all pages by following the 'Next' button.
        """
        pages = []
        page_number = 1

        while True:
            url = f"{self.base_url}/page/{page_number}/"
            html = self.fetch_page(url)

            if not html or "No quotes found!" in html:
                break  # Stop if we hit a non-existent page or empty result

            pages.append(html)
            page_number += 1

        return pages

