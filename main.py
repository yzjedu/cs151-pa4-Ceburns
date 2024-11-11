import os
#comments

def file_selection():
    selection = input('Select a file to analyze:\n\t2014.txt\n\t2015.txt\n\t2016.txt\n\t2017.txt\n\t2018.txt\n\t2019.txt\n\tType selection here: ')
    while not os.path.isfile(selection):
        print('Error, file does not exist. Please try again.')
        selection = input('Select a file to analyze:\n\t2014.txt\n\t2015.txt\n\t2016.txt\n\t2017.txt\n\t2018.txt\n\t2019.txt\n\ttestfile.txt\n\tType selection here: ')
    print(f'You selected {selection}')
    return selection

def menu():
    choice = input('Select a file analysis option:\n\tC- count how many headlines a specific word appears in\n\tW- write headlines containing a specific word to a new file\n\tA- average number of characters per headline\n\tL- determine the longest and shortest headlines\n\tN- new file\n\tE- exit\n\tType selection here: ')
    choice = choice.upper()
    while choice != 'W' and choice != 'C' and choice != 'A' and choice != 'N' and choice != 'L' and choice != 'E':
        choice = input('Select a file analysis option:\n\tC- count how many headlines a specific word appears in\n\tW- write headlines containing a specific word to a new file\n\tA- average number of characters per headline\n\tL- determine the longest and shortest headlines\n\tN- new file\n\tE- exit\n\tType selection here: ')
        choice = choice.upper()
    print(f'You chose {choice}')
    return choice

def headline_word(selection):
    word = input('What word are you looking for?: ')
    word = word.lower()
    fd = open(selection, 'r')
    file_content = fd.read()
    word_count = file_content.count(word)
    if word_count != 1:
        print(f'{word} appears {word_count} times')
    else:
        print(f'{word} appears {word_count} time')
    fd.close()

def word_list(selection):
    fd = open(selection, 'r')
    headlines = fd.readlines()

def headline_avg(selection):
    #wrong - need to find length of each headline not just length of list
    fd = open(selection, 'r')
    headlines = fd.read()
    length = len(headlines)
    count = 0
    for headline in headlines:
        count += 1
    average = length / count
    print(f'The average of headlines {selection} is {average}')
    fd.close()

def headline_length(selection):
    fd = open(selection, 'r')





def main():
    selection = file_selection()
    choice = menu()
    while choice != 'E':
        if choice == 'C':
            headline_word(selection)
        elif choice == 'W':
            word_list(selection)
        elif choice == 'A':
            headline_avg(selection)
        elif choice == 'L':
            headline_length(selection)
        elif choice == 'N':
            selection = file_selection()
        choice = menu()
    print('Thanks!')


main()