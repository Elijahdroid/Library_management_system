class Book:
    library_code = "Code2025"

    def __init__(self, title, author, isbn, total_copies, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = available_copies
        

    def __str__(self):
        return f"Title = {self.title}, Author = {self.author}, ISBN = {self.isbn}, Avaliable = {self.available_copies}/{self.total_copies}, Code: {self.library_code}"

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
        else:
            pass

    @classmethod
    def change_library_code(cls, new_code):
        cls.library_code = new_code


class Member:

    def __init__(self, name, member_id):
        self._name = name
        self._member_id = member_id
        self._borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self._borrowed_books.append(book)
            print(f"{self._name} successfully borrowed {book.title}")
        else:
            print("There aren't any more avaliable books.")

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.return_book()
            print(f"{self._name} successfully returned {book.title}")

    def __str__(self):
        return f"Name = {self._name}, ID = {self._member_id}"


class StudentMember(Member):
    max_books = 0

    def __init__(self, name, student_id, max_books):
        super().__init__(name, student_id)
        self.max_books = max_books
        self._borrowed_books = []

    def book_borrow(self, book):
        if self.max_books == len(self._borrowed_books):
            print(f"{self._name} is not allowed to get any more books")
            self._borrowed_books.append(book)
        else:
            Member.borrow_book(self, book)

    def maxi(self, book):
        if self.max_books <= 0:
            print(f"{self._name}, STOP REDUCING THE NUMBER OF BOOKS YOU CAN READ")
        else:
            self.max_books = self.max_books

    def __str__(self):
        return f"Name = {self._name}, ID = {self._member_id}, Max_Books = {self.max_books}"


class Library():
    def __init__(self):
        self.b = []
        self.m = []

    def add_Book(self, fullBook):
        self.b.append(fullBook)

    def add_Member(self, fullMember):
        self.m.append(fullMember)

    def find_Book(self):
        for i in range(0, len(self.b)):
            if self.b[i] == fullBook[1]:
                return self.b[i]

    def find_Members(self):
        for i in range(0, len(self.m)):
            if self.m[i] == fullMember[1]:
                return self.m[i]


def main():
    l1 = Library()

    b1 = Book("Harry Potter", "J.K.Rowling", 1234, 100, 35)
    l1.add_Book(b1)
    b2 = Book("Diary of a Wimpy Kid", "Jeff Kinney", 2345, 150, 55)
    l1.add_Book(b2)
    b3 = Book("World's Worst Children", "David Walliams", 4568, 5, 2)
    l1.add_Book(b3)
    b4 = Book("Christmas Carol", "Charles Dickins", 1001, 7, 3)
    l1.add_Book(b4)

    m1 = Member("Charles", "Char1234")
    l1.add_Member(m1)
    sm1 = StudentMember("Daniel", "Dan1234", 2)
    l1.add_Member(sm1)

    sm1.book_borrow(b1)
    sm1.book_borrow(b2)
    sm1.book_borrow(b3)
    m1.borrow_book(b3)
    m1.borrow_book(b3)
    m1.borrow_book(b3)

    for book in l1.b:
        print(book)

    for member in l1.m:
        print(member)

    Book.change_library_code("LIB2026")
    print(b1)

if __name__ == "__main__":
    main()