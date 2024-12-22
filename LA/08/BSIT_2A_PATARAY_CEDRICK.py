class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

bookOne = Book("Harry Potter","J. K. Rowling")
bookTwo = Book("Isang Kaibigan","VP Sarah Duterte")
del bookOne.author
print(bookTwo.title,bookTwo.author)
print(bookOne.title,bookOne.author)