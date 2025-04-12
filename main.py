from scraper.collector import Scraper
from scraper.parser import QuoteParser
from models.data_models import Quote
from utils.file_handler import save_to_json, save_to_csv
from utils.analyzer import most_common_tag, most_quoted_author, average_tags_per_quote


def main():
    scraper = Scraper()
    pages = scraper.fetch_all_pages()

    all_quotes = []

    for html in pages:
        parser = QuoteParser(html)
        parsed_data = parser.parse_quotes()

        for item in parsed_data:
            quote = Quote(
                text=item['text'],
                author=item['author'],
                tags=item['tags'],
                author_link=item['author_link']
            )
            all_quotes.append(quote)

    # Convert Quote objects to dicts for saving
    quote_dicts = [q.to_dict() for q in all_quotes]

    # Save data
    save_to_json(quote_dicts, "output/quotes.json")
    save_to_csv(quote_dicts, "output/quotes.csv")

    # Analyze
    print("\n📊 Data Analysis:")
    tag, tag_count = most_common_tag(quote_dicts)
    print(f"Most common tag: {tag} ({tag_count} times)")

    author, author_count = most_quoted_author(quote_dicts)
    print(f"Most quoted author: {author} ({author_count} quotes)")

    avg_tags = average_tags_per_quote(quote_dicts)
    print(f"Average tags per quote: {avg_tags}")


if __name__ == "__main__":
    main()
