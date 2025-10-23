
def generate_id(entity_dict):
    if not entity_dict:
        return 1
    else:
        return max(entity_dict.keys()) + 1

class Book:
    def __init__(self, id = 0, title = "", author = "", isbn = ""):
        self.id  =  id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None
        self.due_date = None

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    
    def borrow_book(self, Member, due_date):
        if self.available:
            self.available = False
            self.borrower = Member
            self.due_date = due_date
            return "Book borrowed successfully"
        else:
            return "This book has been borrowed"

    def return_book(self):
        if self.available == False:
            self.available = True
            self.borrower = None
            self.due_date = None
            return "Book returned successfully"
        else:
            return "Book not borrowed"
        
    def is_available(self):
        return self.available
        


class Member:
    def __init__(self, id=0, name="", email=""):
        self.borrowed_books = []
        self.id = id
        self.name = name
        self.email = email

    def borrow_book(self, Book, due_date):
        if Book.is_available() == True:
            Book.borrow_book(self, due_date)
            self.borrowed_books.append(Book)
        else:
            return "Book not available"
        
    def return_book(self, Book):
        if Book in self.borrowed_books:
            Book.return_book()
            self.borrowed_books.remove(Book)
        else:
            return "This member did not borrow that book"
        
    def view_borrowed_books(self):
        if not self.borrowed_books:
            return "No borrowed books"
        return "\n".join(f"{each.title}, due on {each.due_date}" for each in self.borrowed_books)
            

class Library:

    def __init__(self):
        
        self.books = {}
        self.members = {}
        self.transactions = []
        self.name = ""
        
    def add_book(self, Book):
        if Book.id in self.books:
            return "Book already exists"
        else:
            Book.id = generate_id(self.books)
            self.books[Book.id] = Book
            return "Book added successfully"
        
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return "Book removed successfully"
        else:
            return "Book not found"

    def register_member(self, Member):
        if Member.id in self.members:
            return "Member already registered"
        else:
            Member.id = generate_id(self.members)
            self.members[Member.id] = Member
            return "Member registered Successfullly"
    
    def find_book_by_title(self, title):
        for book in self.books.values():
            if title.lower() in book.title.lower():
                return book.id, book.title, book.author
        return "Book not found"
            
    def borrow_book(self,book_id, member_id, due_date):
        if book_id not in self.books:
            return "Book not found"
        if member_id not in self.members:
            return "Member not found"
        Book = self.books[book_id]
        Member = self.members[member_id]

        if Book.available == True:
            Member.borrow_book(Book, due_date)
            transaction = {"book_id": Book.id, "member_id": Member.id, "status": "Borrowed"}
            self.transactions.append(transaction)
        else:
            return "Book is already borrowed"

    def return_book(self, book_id, member_id):
        if book_id not in self.books:
            return "Book not found"
            
        if member_id not in self.members:
            return "Member not found"
            

        book = self.books[book_id]
        member = self.members[member_id]

        member.return_book(book)
        transaction = {"book_id": book.id, "member_id": member.id, "status": "Returned"}
        self.transactions.append(transaction)

    def show_all_books(self):
        for book in self.books.values():
            print(book)
            status = (
                "Available"
                if book.available
                else f"Borrowed by {book.borrower.name}" if book.borrower else "Unavailable"
            )
            print(f"ID - {book.id}, Title - {book.title}, Author - {book.author}, {status}")

    def show_all_members(self):
        for member in self.members.values():
            print(member.id, member.name, "Borrowed:", len(member.borrowed_books))


#START PROGRAM
library = Library()
print("Welcome to City Central Library")
#library.load_data()

user_choice = " "

while True:
    print("")
    print("--------------------------------")
    print("--------------------------------")
    print("1. View all books")
    print("2. Add a new book")
    print("3. Register a new member")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. View member details")
    print("7. Exit")

    user_choice = str(input())
    

    if user_choice == "1":
        if not library.books:
            print("No books available in the library")
        else:
            library.show_all_books()

    elif user_choice == "2":
        user_title = input("Enter book title: ")
        user_author = input("Enter book author: ")
        user_isbn = input("Enter book isbn: ")
        book_id = generate_id(library.books)
        new_book = Book(book_id, user_title, user_author, user_isbn)
        library.add_book(new_book)

    elif user_choice == "3":
        user_name = input("Enter your name: ")
        user_email = input("Enter your email: ")
        member_id = generate_id(library.members)
        new_member = Member(member_id, user_name, user_email)
        library.register_member(new_member)

    elif user_choice == "4":
        print("Pick one book from the following to borrow")
        print(library.show_all_books())
        cli_book_id = int(input("enter the book_id for the book you want to borrow"))
        cli_member_id = int(input("Enter your membership ID: "))
        cli_due_date = input("Enter due date to return the book(YYYY/MM/DD):")

        library.borrow_book(cli_book_id, cli_member_id, cli_due_date)

    elif user_choice == "5":
        cli_book_id = int(input("enter the book_id for the book you want to borrow"))
        cli_member_id = int(input("Enter your membership ID: "))
        library.return_book(cli_book_id, cli_member_id)

    elif user_choice == "6":
        cli_member_id = int(input("Enter your membership ID: "))
        member = library.members[member_id]
        if member:
            member.view_borrowed_books()
        else:
            print("Member not found")

    elif user_choice == "7" or user_choice.lower() == "exit":
        print("Saving data...")
        #CALL library.save_data()
        print("Goodbye!")
        break 

    else:
        print("Invalid choice")

