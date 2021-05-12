"""
Steven Yang-Zong 1931679
420-LCU COmputer Programming, Section-01
S.Hilal, instructor
Assignment 3
"""
#imports for the graph
import numpy as np
import matplotlib.pyplot as plt

#Read & put the text into a dictionary
fp = open('top-books.txt')
top_books = {}
while True: #keeps reading
    line = fp.readline()
    if not line: break
    line = line.strip("\n") #removes first line
    book_records = line.split(",")
    book_dict = {}
    book_dict = {"author": book_records[1], "language": book_records[2], "type": book_records[3], "sold": int(book_records[4])}
    top_books[book_records[0]] = book_dict
fp.close

while True:
    #menu
    print("""
    "Goodreads: 100 Books You Should Read in a Lifetie" database analysis

    1- How many different languages are there? Print the list of languages.
    2- What language has the most books?
    3- Display all books in a given language.
    4- What are the different types of books? Which type has sold most copies?
    5- List all authors who have more than 1 book on the list.
    6- For a given author, what is the total number of books sold?
    7- List all books of a given type.
    8- What are the top 8 types of books?
    9- Display a plot to show the distribution of books among the top 8 types of books.
    10- Exit
    """)
    menu_inp = input("Select an option by entering its number or 10 to exit: ")
    print("\n")

    #verify if book list is empty
    if not top_books:
        print("ERROR, top_books list is empty")
        exit()

    #option 1 Number of languages & list
    if menu_inp == "1":
        language_lst = []
        #put language into list
        for key, val in top_books.items():
            language_lst.append(val["language"])
        fnl_language_lst = list(dict.fromkeys(language_lst))
        print("There are", len(fnl_language_lst), "languages in total.\n")
        print("The languages are:")
        for i in fnl_language_lst:
            print("-> {0}".format(i)) #format list

    #option 2 language with most books
    elif menu_inp == "2":
        #get all the languages & counting number of books for each type
        language_count = {}
        for key, val in top_books.items():
            language_count[val["language"]] = language_count.get(val["language"],0)+1

        #search for the language with the max value
        top_language_count = max(language_count, key = language_count.get)
        print(top_language_count, "is the language that has the most books.")
        print("\n")

    #option 3 Books in input language
    elif menu_inp == "3":
        inp_language = input("Input a language to receive all books written in that language: ")
        validity = 0
        print("\n")
        for key, val in top_books.items():
            #compare dictionary to input language
            if top_books[key]["language"] == inp_language:
                a, b, c, d = key, val["author"], val["type"], val["sold"]
                print("Title: {0} - Author: {1} - Type: {2} - Number of copies sold: {3}".format(a, b, c, d), "\n") #formatting
                validity = 1
        #if enters unknown languages
        if validity == 0:
            print("There are no books of that language in this database.")
        print("\n")

    #option 4 types of books & type with most copies sold
    elif menu_inp == "4":
        #counts type
        type_count = {}
        for key, val in top_books.items():
            type_count[val["type"]] = type_count.get(val["type"],0)+val["sold"]

        print("The different types of books are: \n")
        for i in type_count:
            print("-> {0}".format(i))

        top_type_count = max(type_count, key = type_count.get)
        print("\n", top_type_count, "is the type that has the most amount of books.")
        print("\n")

    #option 5 List author with more than 1 book in list
    elif menu_inp == "5":
        #dictionary with all the authors
        author_count = {}
        for key, val in top_books.items():
            author_count[val["author"]] = author_count.get(val["author"],0)+1

        #sees which have more than 1 book in the dictionary
        author_validity = 0
        print("Authors with multiple books sold: \n")
        for key, val in author_count.items():
            if val > 1:
                print(key, ":", val, "books sold" )
                author_validity = 1

        if author_validity == 0:
            print("There are no author that have two of their published books in this database.")
        print("\n")

    #option 6 input author & books written
    elif menu_inp == "6":
        inp_author = input("Input an author to receive the total copies of books sold of the books in this database: ")

        print("\n")
        #Search for books sold by author then search for number of copies sold
        books_sold_author = 0
        for key, val in top_books.items():
            if val["author"] == inp_author:
                books_sold_author += top_books[key]["sold"]
        print(inp_author, "has sold", books_sold_author, "copies.")
        print("\n")

    #option 7 list book from input type
    elif menu_inp == "7":
        #from 4
        type_count = {}
        for key, val in top_books.items():
            type_count[val["type"]] = type_count.get(val["type"],0)+1
        print("The different types of books are: \n")
        for i in type_count:
            print("-> {0}".format(i))

        inp_type = input("\nInput a type from the list above to receive all books in that type/genre: ")

        #print books of a certain type
        print("\nBooks in this type: \n")
        for key, value in top_books.items():
            if value["type"] == inp_type:
                print("-> {0}".format(key))
        print("\n")

    #option 8 & 9
    elif menu_inp == "8" or menu_inp =="9":
        #from 4, gets all the types
        type_count2 = {}
        for key, val in top_books.items():
            type_count2[val["type"]] = type_count2.get(val["type"],0)+val["sold"]

        #sort in ascending order
        sort_type_sold = sorted(type_count2, key = type_count2.get)

        #option 8 list top 8 books
        if menu_inp == "8":
            print("Top 8 types of books: \n")
            for i in range(9):
                print("-> Number", i+1, "{0}".format(sort_type_sold[-(i+1)]))
            print("\n")

        #option 9creates and displays the graph (top8 book types vs books sold)
        elif menu_inp == "9":
            x = [] #x-axis markings
            for i in range(9):
                x.append(sort_type_sold[-(i+1)])
            markings = np.arange(len(x))
            y = [] #number of copies Sold
            for key in x:
                y.append(type_count2.get(key))
            plt.bar(markings,y, align='center',alpha=0.5) #barchart
            plt.xticks(markings,x) #draw x-axis markings
            plt.title("Distribution of books among the top 8 types of books")
            plt.xlabel("Types of books")
            plt.ylabel("Copies Sold")
            plt.show()

    #Exit program
    elif menu_inp == "10":
        print("Thank you for using the program.")
        exit()

    else:
        print("ERROR, the entered menu option is invalid.")
