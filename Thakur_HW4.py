import pickle


class Employee:

    def __init__(self, name, id, department, title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title

    # The set_name method sets the name attribute.
    def set_name(self, name):
        self.__name = name

    # The set_id method sets the id attribute.
    def set_id(self, id):
        self.__id = id

    # The set_department method sets the department attribute.
    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    # The get_name method returns the name attribute.
    def get_name(self):
        return self.__name

    # The get_id method returns the id attribute.
    def get_id(self):
        return self.__id

    # The get_department method returns the department attribute.
    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title


    def __str__(self):
        return "Name: " + self.__name + \
               "\nID: " + self.__id + \
               "\nDepartment: " + self.__department + \
               "\nJob Title: " + self.__title


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


FILENAME = 'Employee.dat'

def main():

    myemployees = load_employees()


    choice = 0


    while choice != QUIT:

        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(myemployees)
        elif choice == ADD:
            add(myemployees)
        elif choice == CHANGE:
            change(myemployees)
        elif choice == DELETE:
            delete(myemployees)

    # Save the mycontacts dictionary to a file.
    save_employees(myemployees)

def load_employees():
    try:
        # Open the contacts.dat file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        employee_dct = pickle.load(input_file)

        # Close the phone_inventory.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        employee_dct = {}

    # Return the dictionary.
    return employee_dct


def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a employee')
    print('2. Add a new employee')
    print('3. Change an existing employee')
    print('4. Delete a employee')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# The look_up function looks up an item in the
# specified dictionary.
def look_up(myemployees):
    # Get a id to look up.
    id = input('Enter a id: ')

    # Look it up in the dictionary.
    print(myemployees.get(id, 'That id is not found.'))


def add(myemployees):
    # Get the contact info.
    name = input('Name: ')
    id = input('ID Number: ')
    department = input('Department: ')
    title = input('Title: ')

    # Create a Employee object named entry.
    entry = Employee(name, id, department, title)


    if id not in myemployees:
        myemployees[id] = entry
        print('The entry has been added.')
    else:
        print('That id already exists.')

def change(myemployees):
    # Get a id to look up.
    id = input('Enter a id: ')

    if id in myemployees:
        # Get a new name.
        name = input('Enter the new name: ')

        # Get a new department.
        department = input('Enter the new department: ')

        # Get a new title.
        title = input('Enter the new title: ')

        # Create a contact object named entry.
        entry = Employee(name, id, department, title)

        # Update the entry.
        myemployees[id] = entry
        print('Information updated.')
    else:
        print('That id is not found.')


def delete(myemployees):
    # Get a name to look up.
    id = input('Enter a id: ')

    # If the name is found, delete the entry.
    if id in myemployees:
        del myemployees[id]
        print('Entry deleted.')
    else:
        print('That id is not found.')


def save_employees(myemployees):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(myemployees, output_file)


    output_file.close()


main()

