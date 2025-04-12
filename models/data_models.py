class Quote:
    """
    Represents a quote with its text, author, tags, and a link to the author's page.
    """
    def __init__(self, text, author, tags=None, author_link=None):
        self.text = text
        self.author = author
        self.tags = tags if tags else []
        self.author_link = author_link

    def to_dict(self):
        return {
            "text": self.text,
            "author": self.author,
            "tags": self.tags,
            "author_link": self.author_link
        }

    def __str__(self):
        return f'"{self.text}" - {self.author} ({", ".join(self.tags)})'


class Author:
    """
    Represents an author and their metadata (expandable from author profile page).
    """
    def __init__(self, name, bio=None, born_date=None, born_location=None):
        self.name = name
        self.bio = bio
        self.born_date = born_date
        self.born_location = born_location

    def to_dict(self):
        return {
            "name": self.name,
            "bio": self.bio,
            "born_date": self.born_date,
            "born_location": self.born_location
        }

    def __str__(self):
        return f"{self.name} (born {self.born_date} in {self.born_location})"
