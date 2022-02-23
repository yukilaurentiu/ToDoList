user_input = 'randam'
data =[]


def show_menu():
    print('Menu:\n',
          '1. Add an item\n',
          '2. Mark as done\n',
          '3. View item\n',
          '4. Exit\n')


while user_input != '4' :

    show_menu()
    user_input = input('Enter your choice: ')

    if user_input == '1':
        item = input('What is to be done? ')
        data.append(item)
        print('Added item', item)
    elif user_input == '2':
        item = input('What is to be marked as done? ')
        if item in data:
            data.remove(item)
            print('Removed item; ', item)
        else:
            print('Item does not exist')
    elif user_input == "3":
        print('List of to-do items: ')
        for item in data:
            print(item)
    elif user_input == '4':
        print('Goodbye!')
    else:
        print('Please enter one of 1,2,3 or 4')
