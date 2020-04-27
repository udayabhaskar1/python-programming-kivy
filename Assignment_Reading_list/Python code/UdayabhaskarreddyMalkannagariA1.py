"""
This module is an implementation of a console-based program of a simple reading list.
The program receives several inputs from the user to track books they wish to read and books they have completed reading.
The user can add new books to the reading list and also mark books as completed.
Based on the user inputs,the reading list will be updated with the read and completed status of the books.

Author: Udaya Bhaskar Reddy Malkannagari
Student ID: 13368171
Date: 4 Jan,2017
Version: 1.0
Github repository: https://github.com/mudaybr/CP1404-Assignment
"""
from operator import itemgetter  #importing the itemgetter from the operator module to sort the reading list.
import string                    # importing the string module to error check for integers in author_name
FILENAME = "books.csv"
MENU = "Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"
file_list = []                   # initializing an empty list(of lists) to store the data for the reading list.

def main():
    """
    The main function takes inputs from the user and updates the reading list based on user choices.

    call read_file()
    call print_header()
    display the Menu
    get user_choice from the user and convert it into lowercase
    while user_choice is not "q":
        if user_choice = "r" then:
            display "Required books"
            call list_books(user_choice)
        else if user_choice = "c" then:
            display "Completed books"
            call list_books(user_choice)
        else if user_choice = "m" then:
            count = call book_count("r")
            if count = 0 then:
                display "No required books"
            else:
                display "Required books"
                call list_books("r")
                call mark_book()
        else if user_choice = "a" then:
            call add_book()
        else:
            display "Invalid input;please choose the options from the menu"
        display MENU
        get user_choice from the user and convert it to lowercase
    call write_file()
    display message with the number of books saved to the file
    display "Have a nice day!"

    """

    read_file()                             #call the function read_file() to load the books
    print_header()                          #display a welcome message with name in it
    print(MENU)
    user_choice = input(">>>").lower()      #convert the user input to lowercase to handle both uppercase and lowercase letters
    while user_choice != "q":               #Loop until the user choice is not "q"(Quit the program)
        if user_choice == "r":
            print("Required books:")
            list_books(user_choice)         #list all Required books by calling the function list_books()
        elif user_choice == "c":
            print("Completed books:")
            list_books(user_choice)         #list all Completed books by calling the function list_books()
        elif user_choice == "m":
            count = book_count("r")         #Call the function book_count() to check the count of required books in the reading list and assign it a variable "count"
            if count == 0:
                print("No required books")  #Display the message "No required books" if the count is zero
            else:
                print("Required books:")
                list_books("r")
                mark_book()                 #Call the function mark_book to mark a book as completed
        elif user_choice == "a":
            add_book()                      #Call the function add_book to add a new book to the reading list
        else:
            print("Invalid menu choice")
        print(MENU)
        user_choice = input(">>>").lower()
    write_file()                            #Call the function write_file() to save the books to the CSV file
    print("{} books saved to {}".format(len(file_list),FILENAME))
    print("Have a nice day:)")


def print_header():
    """
    This function prints the header with a message that includes the  user name and the number of books in the reading list.

    Display the welcome message with user name and the number of books in the reading list.
    :return: displays a welcome message with name and the number of books loaded.
    """
    print("Reading List 1.0 - by Udaya Bhaskar Reddy\n{} books loaded from books.csv".format(len(file_list)))

def read_file():
    """
    This function loads the readling list from the books.csv file

    open the file,"FILENAME", to read and assign it a variable name "file_pointer"
    for index,data in enumerate(file_pointer.readlines()):
        use the strip method to remove whitespace characters from data
        split the data using the separator "," and assign it to a variable "datum"
        append the file_list by passing the object "datum" into it
    Sort the file_list
    Close the file

    """
    file_list
    file_pointer = open(FILENAME, "r")
    for index, data in enumerate(file_pointer.readlines()):
        data = data.strip()                     # using the strip method to remove whitespace characters
        datum = data.split(",")                 # splitting "data" using the separator ","
        file_list.append(datum)                 # appending the file_list with the object "datum"
    file_list.sort(key=itemgetter(1, 2))        # sorting the file_list
    file_pointer.close()

def list_books(choice):
    """
    This function lists the books in the reading list based on the user choice(Required or Completed)

    Call the function book_count to check if the list of books(based on user choice) is empty
    if book_count(choice) = o then:
        display "No books"
    else:
        Set initial value of count to 0
        Set initial value of pages to 0
        for index, data in enumerate(file_list):
            if data[-1] == choice then:
                count = count + 1
                pages = pages + 1
                display the message with the appropriate number of pages, book name and author name
        display the message with the number of books and the total number of pages in it

    :param choice: user choice(Required(R) or Completed(C))

    """

    if book_count(choice) == 0:         #Call the function book_count() to check if the count of books is zero
        print("No books")
    else:
        count = 0
        pages = 0
        for index, data in enumerate(file_list):        #loop through the file_list
            if data[-1] == choice:              #if the last element of the list(here data = file_list[index]) is equal to the user choice("r" or "c")
                count += 1
                pages += int(data[2])           #data[2] means "file_list[index][2]"; converting it to an integer to count the pages
                print(" {}. {:45s} by {:20s} {:<3} pages".format(index, data[0], data[1], data[2]))
        print("Total pages for {} books: {}\n".format(count, pages))

def book_count(var):
    """
    This function is used to count and check if the number of books(required or completed) is zero

    Count the number of books in the file_list based on user choice("r" or "c") and assign it a variable count_of_books
    return the count_of_books

    :param var: "r" or "c"
    :return: count_of_books

    """
    count_of_books = sum(x.count(var) for x in file_list)    #storing the total number of required/completed books based on var(argument)
    return count_of_books

def mark_book():
    """
    This function marks a book from the reading list as completed.

    Set valid_input to False
    while not valid_input:
        try:
            Set book_name to an empty string
            Set author_name to an empty string
            get book_choice from the user
            while book_choice is less than zero or book_choice is greater than or equal to the length of the file_list
                display "Invalid input; enter a valid number"
                get book_choice from the user
            Set valid_input to True

            for index,data in enumerate(file_list):
                if index = book_choice and data[-1] = "r" then:
                    data[-1] = "c"
                    book_name = data[0]
                    author_name = data[1]
                    display that the book is marked as completed with appropriate book_name and author_name in the message
                else if index = book_choice and data[-1] = "c" then:
                    display "The book is already completed"
        except a ValueError:
            display "Invalid input; enter a valid number"
    """

    valid_input = False
    while not valid_input:
        try:
            book_name = ""
            author_name = ""
            book_choice = int(input("Enter the number of a book to mark as completed\n>>>"))
            while book_choice < 0 or book_choice >= len(file_list):         #looping until the book_choice is within the range of reading list
                print("Invalid input; enter a valid number")
                book_choice = int(input("Enter the number of a book to mark as completed\n>>>"))
            valid_input = True

            for index, data in enumerate(file_list):
                if index == book_choice and data[-1] == "r":   #checking if the last element of the list(based on the index) is "r" and index = book_choice
                    data[-1] = "c"                             #replacing the last element of the list to "c"
                    book_name = data[0]                        #assigning book_name to the first element of the list
                    author_name = data[1]                      #assigning author_name to the second element of the list
                    print("{} by {} marked as completed".format(book_name, author_name))
                elif index == book_choice and data[-1] == "c": #checking if the last element of the list(based on the index) is "c"
                    print("That book is already completed")
        except ValueError:
            print("invalid input; enter a valid number")

def write_file():
    """
    This function saves the books to the CSV file overwriting the file contents.

    open the file,"FILENAME",to write and assign it to a variable "output_file"
    join the elements of the file list with a separator "," using the map method and assign it a variable file_str
    write the elements in str1 to the file_list
    close the file

    """
    output_file = open(FILENAME, "w")
    file_str = [','.join(map(str,x)) for x in file_list]    #join the elements of the file_life with a separator "," using the map method
    for elem in file_str:
        print(elem, file=output_file)                       #write the books to the CSV file
    output_file.close()

def add_book():
    """
    This function adds the books to the reading list based on user inputs.

    get user inputs for "Title","Author" and "Pages",and assign the variables book_name,author_name, and book_pages to them
    error check for wrong user inputs and display the appropriate error message
    assign the variable book_status and set it to "r"
    create a list,"add_list"
    append the "file_list" with "add_list" as the object
    display the message with the appropriate book_name,author_name,number of pages added to the reading list

    """
    book_name = str(input("Title: "))
    while book_name == "" or book_name.isspace():       #looping to check if book_name is empty or just a space
        print("Input cannot be blank")
        book_name = str(input("Title: "))

    valid_input = True
    while valid_input:
        author_name = input("Author: ")
        if author_name == "" or author_name.isspace():  #error-checking if author_name is empty or just a space
            print("Input cannot be blank")
        else:
            count = 0                                   #Setting the initial value of count to 0
            for each in author_name:
                if each not in (string.ascii_letters + " ") :   #error-checking for valid author name; name of the author cannot be a number
                    count += 1
            if count > 0:                               #count > 0 implies there are other characters in the author name apart from alphabets and space
                print("Invalid author name; author name cannot be a number")
            else:
                valid_input = False

    result = None
    while result is None:
        book_pages = input("Pages: ")
        if book_pages == "":                            #if book_pages is empty
            print("Input cannot be blank")              #error-checking a blank user-input
        else:
            try:
                result = int(book_pages)
                if not result >= 0:                     #error-checking for a negative number
                    print("Number must be >= 0.")
                    result = None
            except ValueError:                          #excepting a value error
                print("Invalid input: enter a valid number")

    book_status = "r"
    add_list = [book_name, author_name, book_pages, book_status]  #creating a list based on user_inputs
    file_list.append(add_list)    #appending the list,"add_list", to file_list
    print("{} by {}, ({} pages) added to reading list".format(book_name, author_name, book_pages))

main()


