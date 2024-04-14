
class Book

    attr_accessor :title, :author, :pages

    def initialize(title, author, pages)

        @title = title
        @author = author
        @pages = pages

        puts "Title: "+title
        puts "Author: "+author
        puts "pages: "+pages.to_s
        puts "\n"


    end
end



book1 = Book.new("Harry Potter", "Jk Rowling", 400)

# book1.title = "Harry Potter"
# book1.author = "Jk Rowling"
# book1.pages = 400


# puts book1.title
# puts book1.author
# puts book1.pages



book2 = Book.new("Lord of the Rings", "Tolkein", 600)

# book2.title = "Lord of the rings"
# book2.author = "Tolkein"
# book2.pages = 600

# puts book2.title
# puts book2.author
# puts book2.pages