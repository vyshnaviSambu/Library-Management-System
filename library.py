# Library Management System with File Handling + HTML Report

FILENAME = "library.txt"

# Function to add a new book
def add_book(title, author):
    with open(FILENAME, "a") as f:
        f.write(f"{title},{author},Available\n")
    print(f"✅ Book '{title}' added successfully!")

# Function to view all books in console
def view_books():
    try:
        with open(FILENAME, "r") as f:
            books = f.readlines()
        print("\n📚 Library Books:")
        print("-" * 40)
        for i, book in enumerate(books, 1):
            title, author, status = book.strip().split(",")
            print(f"{i}. {title} by {author} - {status}")
    except FileNotFoundError:
        print("⚠ No books found. Add some books first.")

# Function to borrow a book
def borrow_book(title):
    try:
        with open(FILENAME, "r") as f:
            books = f.readlines()
        updated, found = [], False
        for book in books:
            b_title, author, status = book.strip().split(",")
            if b_title == title and status == "Available":
                updated.append(f"{b_title},{author},Borrowed\n")
                found = True
            else:
                updated.append(book)
        with open(FILENAME, "w") as f:
            f.writelines(updated)
        if found:
            print(f"✅ You borrowed '{title}'")
        else:
            print(f"⚠ '{title}' is not available.")
    except FileNotFoundError:
        print("⚠ No books available.")

# Function to return a book
def return_book(title):
    try:
        with open(FILENAME, "r") as f:
            books = f.readlines()
        updated, found = [], False
        for book in books:
            b_title, author, status = book.strip().split(",")
            if b_title == title and status == "Borrowed":
                updated.append(f"{b_title},{author},Available\n")
                found = True
            else:
                updated.append(book)
        with open(FILENAME, "w") as f:
            f.writelines(updated)
        if found:
            print(f"✅ You returned '{title}'")
        else:
            print(f"⚠ '{title}' was not borrowed or not found.")
    except FileNotFoundError:
        print("⚠ No books available.")

# Function to generate HTML report
def generate_report():
    try:
        with open(FILENAME, "r") as f:
            books = f.readlines()

        html = """
        <html>
        <head>
            <title>Library Report</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <h1>📚 Library Book Report</h1>
            <div class="book-container">
        """
        for book in books:
            title, author, status = book.strip().split(",")
            html += f"""
            <div class="book-card {status.lower()}">
                <h2>{title}</h2>
                <p><b>Author:</b> {author}</p>
                <p class="status">{status}</p>
            </div>
            """
        html += """
            </div>
        </body>
        </html>
        """

        with open("library_report.html", "w") as f:
            f.write(html)

        print("✅ Library report generated! Open 'library_report.html' in your browser.")
    except FileNotFoundError:
        print("⚠ No books to generate report.")

# Menu
def menu():
    while True:
        print("\n===== 📖 Library Menu =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Generate HTML Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            add_book(title, author)
        elif choice == "2":
            view_books()
        elif choice == "3":
            title = input("Enter book title to borrow: ")
            borrow_book(title)
        elif choice == "4":
            title = input("Enter book title to return: ")
            return_book(title)
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("👋 Exiting Library System. Goodbye!")
            break
        else:
            print("⚠ Invalid choice, try again!")

# Run Program
if __name__ == "__main__":
    menu()
