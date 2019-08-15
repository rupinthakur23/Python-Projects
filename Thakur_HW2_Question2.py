#Rupin Singh Thakur
#1001651167
import os

print("Choice Menu")
print("1) Add a contact yo want to Enter")
print("2)  list of contacts")
print("3) Search for a  given name in the list")
print("4) Modify a given contact")
print("5) Delete a given contact from the list")
print("6) Quit")


def select():
    print("Choice Menu")
    print("1) Add a contact")
    print("2) Show the list of contacts")
    print("3) Search for a name in the list")
    print("4) Modify a contact")
    print("5) Delete a contact from the list")
    print("6) Quit")
    main()


def add():
    another = 'y'
    contact_file = open('contact.txt', 'w')

    while another == 'y' or another == 'Y':
        print('Enter the following info :')
        name = input('Name : ')
        email = input('Email: ')
        phone = int(input('Phone no : '))

        contact_file.write(name + '\n')
        contact_file.write(email + '\n')
        contact_file.write(str(phone) + '\n')

        print('Do you want to add another record ?')
        another = input('Y or y for YES , anything else is no:')

    contact_file.close()
    select()


def show():
    contact_file = open('contact.txt', 'r')
    print('List of contact(s) :')
    count = 0
    name = contact_file.readline()
    while name != '':
        email = contact_file.readline()
        phone = contact_file.readline()

        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phone = phone.rstrip('\n')

        count = count + 1
        print('Contact # ', count)
        print('Name : ', name)
        print('Email id :', email)
        print('Phone no :', phone)
        print('----------------------------')

        name = contact_file.readline()

    contact_file.close()
    select()


def search():
    found = False
    search = input('Enter the name you want to search : ')
    contact_file = open('contact.txt', 'r')
    name = contact_file.readline()

    while name != '':
        email = contact_file.readline()
        phone = contact_file.readline()

        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phone = phone.rstrip('\n')

        if name == search:
            print('Name : ', name)
            print('Email id :', email)
            print('Phone no :', phone)
            found = True
        name = contact_file.readline()
    contact_file.close()
    select()


def modify():
    found = False
    search = input('Enter the name to modify  : ')
    new_email = input('Enter the new email you want : ')
    new_phone = input('Enter the new Phone number you want : ')

    contact_file = open('contact.txt', 'r')

    temp_file = open('temp.txt', 'a')
    name = contact_file.readline()

    while name != '':
        email = contact_file.readline()
        phone = contact_file.readline()

        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phone = phone.rstrip('\n')

        if name == search:

            temp_file.write(name + '\n')
            temp_file.write(new_email + '\n')
            temp_file.write(new_phone + '\n')

            found = True
        else:
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(phone + '\n')

        name = contact_file.readline()

    contact_file.close()
    temp_file.close()

    os.remove('contact.txt')
    os.rename('temp.txt', 'contact.txt')

    if found:
        print('the file you enter  has been updated')
    else:
        print('There is no name like this in list')

    select()


def delete():
    found = False
    search = input('What contact would you like to delete : ')
    contact_file = open('contact.txt', 'r')
    temp_file = open('temp.txt', 'a')
    name = contact_file.readline()

    while name != '':
        email = contact_file.readline()
        phone = contact_file.readline()

        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phone = phone.rstrip('\n')

        if name != search:
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(phone + '\n')
        else:
            found = True

        name = contact_file.readline()
    contact_file.close()
    temp_file.close()

    os.remove('contact.txt')
    os.rename('temp.txt', 'contact.txt')

    if found:
        print('The file has been updated')
    else:
        print('That contact was not found in file')

    select()


def quit():
    print('Exiting the program........')


def main():
    choice = int(input('Enter your Choice: '))
    if choice == 1:
        add()
    elif choice == 2:
        show()
    elif choice == 3:
        search()
    elif choice == 4:
        modify()
    elif choice == 5:
        delete()
    elif choice == 6:
        quit()


main()
