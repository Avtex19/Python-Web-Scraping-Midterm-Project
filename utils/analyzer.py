from collections import Counter


def most_common_tag(quotes):
    all_tags = [tag for quote in quotes for tag in quote['tags']]
    tag_counts = Counter(all_tags)
    return tag_counts.most_common(1)[0] if tag_counts else None


def most_quoted_author(quotes):
    author_counts = Counter(quote['author'] for quote in quotes)
    return author_counts.most_common(1)[0] if author_counts else None


def average_tags_per_quote(quotes):
    if not quotes:
        return 0
    total_tags = sum(len(quote['tags']) for quote in quotes)
    return round(total_tags / len(quotes), 2)
