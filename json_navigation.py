import json


def read_file(file_path):
    file = open(file_path, mode='r').readlines()
    file = [f.strip() for f in file]
    file = ''.join(file)
    return json.loads(file)


def bool_check(usr_input):
    while True:
        if usr_input not in ('yes', 'no'):
            usr_input = input('Please enter either "yes" or "no"\n>>')
        else:
            break
    return usr_input


def data_navigation(file_path):
    data = read_file(file_path)
    path = '>>'
    while True:
        if type(data) == dict:
            options = '    '.join(list(data))
            usr_input = input(f'This is a dictionary. Please choose a key from the following: \n{options}\n{path}')

        elif type(data) == list:
            whole_list = input('This is a list. Would you like to see the whole list?\n>>')
            whole_list = bool_check(whole_list)
            if whole_list == 'yes':
                print(data)
                query = input('Do you wish to proceed?\n>>')
                query = bool_check(query)
                if query == 'yes':
                    continue
                elif query == 'no':
                    break
            try:
                usr_input = int(input(f'This is a list. Please enter the index of the list item you \
would like to view: \n{path}'))
            except ValueError:
                print('Invalid index!')
                continue
            while True:
                if usr_input >= len(data):
                    usr_input = int(input('Index too big! Try again.\n>>'))
                else:
                    break

        else:
            final = input(f'This is a {type(data)} object. Would you like to see it?\n')
            final = bool_check(final)
            if final == 'yes':
                print(data)
            break
        try:
            data = data[usr_input]
            path += str(usr_input) + '>>'
        except KeyError:
            print('There is no such key...')

    print('This is the end of the file.')
    return


data_navigation('frienfs_list_Obama.json')
