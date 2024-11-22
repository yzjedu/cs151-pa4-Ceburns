import os
# Programmers:  Caitlin Burns
  # Course:  CS151, Professor Zee
  # Due Date: 11/22
  # Programming Assignment:  PA4
  # Problem Statement:  allows user to choose from a menu of options to analyze a file
  # Data In: file name, word selection
  # Data Out:  word count, average, new file, shortest and longest headlines
  # Credits: this is based on the code in the readme file, class notes, and the class codes on github


# Purpose: allows user to select file
# Parameters: none
# Return: selection
def file_selection():
    selection = input(
        'Select a file to analyze:\n\t2014.txt\n\t2015.txt\n\t2016.txt\n\t2017.txt\n\t2018.txt\n\t2019.txt\n\tType selection here: ')
    while not os.path.isfile(selection):
        print('Error, file does not exist. Please try again.')
        selection = input(
            'Select a file to analyze:\n\t2014.txt\n\t2015.txt\n\t2016.txt\n\t2017.txt\n\t2018.txt\n\t2019.txt\n\ttestfile.txt\n\tType selection here: ')
    print(f'You selected {selection}')
    return selection

# Purpose: allows user to select options from menu
# Parameters: none
# Return: choice
def menu():
    choice = input(
        'Select a file analysis option:\n\tC- count how many headlines a specific word appears in\n\tW- write headlines containing a specific word to a new file\n\tA- average number of characters per headline\n\tL- determine the longest and shortest headlines\n\tN- new file\n\tE- exit\n\tType selection here: ')
    while choice != 'W' and choice != 'C' and choice != 'A' and choice != 'N' and choice != 'L' and choice != 'E':
        choice = input(
            'Select a file analysis option:\n\tC- count how many headlines a specific word appears in\n\tW- write headlines containing a specific word to a new file\n\tA- average number of characters per headline\n\tL- determine the longest and shortest headlines\n\tN- new file\n\tE- exit\n\tType selection here: ')
    choice = choice.upper()
    print(f'You chose {choice}')
    return choice

# Purpose:reads file
# Parameters: selection
# Return: file_content
def read_file(selection):
    try:
        fd = open(selection, 'r')
        file_content = fd.read()
        fd.close()
    except FileNotFoundError:
        print('File does not exist.')
    return file_content


# Purpose: finds how many times a word appears in a file of headlines
# Parameters: file_content
# Return: none
def headline_word(file_content):
    word = input('What word are you looking for?: ')
    while word.isdigit():
        print('Invalid entry.Try again')
        word = input('What word are you looking for?: ')
    word = word.lower()
    word_count = file_content.count(word)
    if word_count != 1:
        print(f'{word} appears {word_count} times')
    else:
        print(f'{word} appears {word_count} time')

# Purpose: writes a word selected by the user to a new file
# Parameters: file_content
# Return: none
def word_list(file_content):
    word = input('What word are you looking for?: ')
    while word.isdigit():
        print('Invalid entry.Try again')
        word = input('What word are you looking for?: ')
    word = word.lower()
    file_name = input('What would you like to name your file?: ')
    word_count = file_content.count(word)
    while word_count == 0:
        print(f'{word} appears 0 times. Pick a different word')
        word = input('What word are you looking for?: ')
        word_count = file_content.count(word)
    fd = open(file_name, 'w')
    list = (word + ' ') * word_count
    fd.write(list)
    fd.close()

# Purpose: creates a table from file
# Parameters: selection
# Return: table
def file_to_table(selection):
    table = []
    try:
        fd = open(selection, 'r')
        for line in fd:
            row = line.strip('\n')
            table.append(row)
        fd.close()
    except FileNotFoundError:
        print('File does not exist')
    return table

# Purpose:finds the average amount fo characters in headlines
# Parameters:  table, selection
# Return: none
def headline_avg(table, selection):
    count = 0
    for line in table:
        row_length = len(line)
        count += 1
    average = row_length / count
    print(f'The headline average of {selection} is {average:.2f}')


# Purpose: finds shortest and longest headlines in a file
# Parameters: table
# Return: none
def headline_length(table):
    shortest_headline = table[0]
    longest_headline = table[0]
    for line in table:
        if len(line) < len(shortest_headline):
            shortest_headline = line
        if len(line) > len(longest_headline):
            longest_headline = line
    print(f'The shortest headline is "{shortest_headline}" \nwith a length of {len(shortest_headline)} characters')
    print(f'The longest headline is "{longest_headline}" \nwith a length of {len(longest_headline)} characters')

# Purpose: runs main program
# Parameters: none
# Return: none
def main():
    print('~' * 90)
    print('This program allows a user to select from a variety of files and file analysis options.')
    print('~' * 90)
    selection = file_selection()
    choice = menu()
    file_content = read_file(selection)
    table = file_to_table(selection)
    while choice != 'E':
        if choice == 'C':
            headline_word(file_content)
        elif choice == 'W':
            word_list(file_content)
        elif choice == 'A':
            headline_avg(table, selection)
        elif choice == 'L':
            headline_length(table)
        elif choice == 'N':
            selection = file_selection()
        else:
            print('invalid choice')
        choice = menu()
    print('Thanks!')


main()