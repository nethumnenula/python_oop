class Book:

    # CONSTRUCTOR
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # to_string
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Check Equality
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # Check Less Than
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # Check Greater Than
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # Add
    def __add__(self, other):
        return self.num_pages + other.num_pages

    # Search for an item within an object
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    # Get an item from an object
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found."