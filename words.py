def print_upper_words(list):
    '''Will print each word in a list as an uppercase word. 

    ['hi', 'scooby', 'doo'] will print 
    HI
    SCOOBY
    DOO
    '''
    for words in list: 
        print(words.upper())

print_upper_words(['hi', 'scooby', 'doo'])


def print_upper_e_words(list):
    '''Will print each word in a list as an uppercase word, only if it starts with the letter e. 

    ['hi', 'scooby', 'doo', 'everyday'] will print 
    EVERYDAY
    '''
    for words in list:
        if words.startswith('e') or words.startswith('E'):
            print(words.upper())

print_upper_e_words(['hi', 'scooby', 'doo', 'everyday'])


def print_if_starts_with(list, must_start_with):
    '''Will print each word in a list, only if it starts with the letter must_start_with is. 

    ['hi', 'scooby', 'doo', 'everyday'], 'd' will print 
    doo
    '''
    for words in list:
        if words.startswith(must_start_with) or words.startswith(must_start_with.upper()):
            print(words)

print_if_starts_with(['hi', 'scooby', 'doo', 'everyday'], 'd')