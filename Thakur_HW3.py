
import sqlite3
conn = sqlite3.connect('test.db')

conn.execute('''
CREATE TABLE if not exists Player1 (
    name   TEXT                    NOT NULL,
    wins   INTEGER                    NOT NULL,
    losses   INTEGER                  NOT NULL,
    ties   INTEGER                    NOT NULL
)''')


def view():
    cursor = conn.execute("select *  from Player1")
    print("{:15}{:>10}{:>13}{:>10}{:>12}".format("Name", "Wins", "Losses", "Ties", "Games"))
    print("------------------------------------------------------------")

    for row in cursor:
        print("{:15}{:>9}{:>13}{:>10}{:>12}".format(row[0], row[1], row[2], row[3], (row[1] + row[2] + row[3])))
    print()
    cursor.close()


def add():
    name = input("Name: ")
    try:
        wins = int(input("Wins: "))
        losses = int(input("Losses: "))
        ties = int(input("Ties: "))
        sql = '''INSERT INTO Player1 (name, wins,losses,ties) 
             VALUES (?, ?,?,?)'''
        cursor = conn.execute(sql, (name, wins, losses, ties))
        conn.commit()
        print(name, " was added to database.")
        cursor.close()
    except:
        print("Error: Please enter a valid number")
        main()


def update():
    upd_name = input("Name: ")
    cursor = conn.execute("select name from Player1 where name=(?)", (upd_name,))
    for row in cursor:
        try:
            upd_wins = int(input("Wins: "))
            upd_losses = int(input("Losses: "))
            upd_ties = int(input("Ties: "))
            cursor = conn.execute("Update Player1 set wins=?,losses=?,ties=? where name=?",
                                  [upd_wins, upd_losses, upd_ties, upd_name, ])
            conn.commit()
            print(upd_name, " was updated to database.")
            cursor.close()
        except:
            print("Error: Please enter a valid number")
            main()
    cursor.close()


def deletion():
    del_name = input("Name: ")
    cursor = conn.execute("DELETE from Player1 where name=(?)", (del_name,))
    conn.commit()
    print(del_name, " was deleted from database.")
    cursor.close()


def exit():
    print("Bye!")
    conn.close()


def main():
    choice = ""
    while choice != "exit":
        print('Player Manager \n')
        print('COMMAND MENU')
        print('view - View players')
        print('add - Add a player')
        print('update - Update player')
        print('del -  Delete a player')
        print('exit - Exit program')

        choice = str(input('Command: '))
        choice_in = choice.lower()
        inpt = ["view", "add", "update", "del", "exit"]
        if choice_in in inpt:
            if choice_in == "view":
                view()

            elif choice_in == "add":
                add()

            elif choice_in == "update":
                update()

            elif choice_in == "del":
                deletion()
            elif choice_in == "exit":
                exit()

        else:
            print("Error : Please enter a valid input \n")


main()

















