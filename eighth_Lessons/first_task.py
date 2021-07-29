


class Books:
    def __init__(self, author, book_name, publishing_year, book_genre):
        self.author = author
        self.book_name = book_name
        self.publishing_year = publishing_year
        self.book_genre = book_genre

    def __repr__(self):
        return f'\nAuthor: {self.author} \nBook name: {self.book_name} \nThe year of publishing: {self.publishing_year} \nBook genre: {self.book_genre}\n'

    def __str__(self):
        return f'\nAuthor: {self.author} \nBook name: {self.book_name} \nThe year of publishing: {self.publishing_year} \nBook genre: {self.book_genre}\n'

    def __eq__(self, other):
        return isinstance(other, Books) and Books.__repr__(self) == Books.__str__(self)


first_Book = Books('Bob', "Bob's history", 2000, 'History')
second_Book = Books('Alfred', 'Interesting history about Lion', 1992, 'Drama')

if first_Book == second_Book:
    print(first_Book)
    print(second_Book)
else:
    print(second_Book)


