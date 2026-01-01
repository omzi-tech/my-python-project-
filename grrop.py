class LibrarySystem:
    def _init_(self):
        self.books = [
            {"id": 1, "name": "The Catcher in the Rye", "available": True},
            {"id": 2, "name": "To Kill a Mockingbird", "available": True},
            {"id": 3, "name": "1984", "available": True},
            {"id": 4, "name": "Pride and Prejudice", "available": True},
            {"id": 5, "name": "The Great Gatsby", "available": True},
            {"id": 6, "name": "One Hundred Years of Solitude", "available": True},
            {"id": 7, "name": "The Hobbit", "available": True},
            {"id": 8, "name": "Brave New World", "available": True},
            {"id": 9, "name": "The Lord of the Rings", "available": True},
            {"id": 10, "name": "The Chronicles of Narnia", "available": True},
        ]
        self.borrowed_books = []
        self.borrowers = {}

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(
                f"ID: {book['id']}, {book['name']} - {'Available' if book['available'] else 'Borrowed'}")

    def display_books_alphabetically(self):
        sorted_books = sorted(self.books, key=lambda x: x["name"])
        for book in sorted_books:
            print(f"ID: {book['id']}, {book['name']}")

    def borrow_book(self, student_id):
        book_id = int(input("Enter the ID of the book to borrow: "))
        for book in self.books:
            if book["id"] == book_id and book["available"]:
                book["available"] = False
                self.borrowed_books.append(
                    {"id": book["id"], "name": book["name"], "student_id": student_id})
                print(
                    f"{book['name']} (ID: {book['id']}) has been borrowed by Student {student_id}.")
                return
        print("Book not available or does not exist.")

    def return_book(self):
        book_id = int(input("Enter the ID of the book to return: "))
        borrowed_book = next(
            (book for book in self.borrowed_books if book["id"] == book_id), None)
        if borrowed_book:
            self.borrowed_books.remove(borrowed_book)
            book = next((b for b in self.books if b["id"] == book_id), None)
            if book:
                book["available"] = True
                print(
                    f"{borrowed_book['name']} (ID: {book_id}) has been returned by Student {borrowed_book['student_id']}.")
            else:
                print("Error: Book not found.")
        else:
            print("Error: Book not found or not borrowed.")

    def search_borrowers(self):
        book_id = int(
            input("Enter the ID of the book to search for borrowers: "))
        borrowers = [(entry["student_id"], entry["name"])
                     for entry in self.borrowed_books if entry["id"] == book_id]
        print(f"Borrowers of Book (ID: {book_id}):")
        for student_id, book_name in borrowers:
            print(f"Student ID: {student_id}, Book: {book_name}")

    def send_notification(self, student_id):
        print(f"Notification sent to Student {student_id}.")

    def view_statistics(self):
        total_books = len(self.books)
        borrowed_books_count = total_books - \
            sum(book["available"] for book in self.books)
        percentage_borrowed = (borrowed_books_count / total_books) * 100
        print(f"Total Books: {total_books}")
        print(f"Borrowed Books: {borrowed_books_count}")
        print(f"Percentage of Books Borrowed: {percentage_borrowed}%")

    def run(self):
        while True:
            print("\nChempaka’s High School Library System")
            print("1. View all books")
            print("2. View books alphabetically")
            print("3. Borrow a book")
            print("4. Return a book")
            print("5. Search borrowers of a book")
            print("6. Send notification")
            print("7. View library statistics")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                self.display_books()
            elif choice == "2":
                self.display_books_alphabetically()
            elif choice == "3":
                student_id = input("Enter student ID: ")
                self.borrow_book(student_id)
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                self.search_borrowers()
            elif choice == "6":
                student_id = input("Enter student ID: ")
                self.send_notification(student_id)
            elif choice == "7":
                self.view_statistics()
            elif choice == "8":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")


if _name_ == "_main_":
    library_system = LibrarySystem()
    library_system.run()