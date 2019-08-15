

from tkinter import *
from tkinter import messagebox

#


root = Tk()
root.geometry("450x450")
root.title("Login Portal")
lbl = Label(root, text="Please Login", justify='center')
lbl.pack()
label1 = Label(root, text="Username:", width=20)
label1.place(x=3, y=130)
username = StringVar()
password = StringVar()
entry1 = Entry(root, textvariable=username)
entry1.place(x=105, y=130)
label2 = Label(root, text="Password", width=10)
label2.place(x=38, y=180)
entry2 = Entry(root, textvariable=password, show="*")
entry2.place(x=105, y=180)


def compute_area():
    top = Toplevel()
    top.title("Calculate Hypotenuse")
    top.geometry("550x170")
    labela = Label(top, text='Side A')
    labela.place(x=2, y=2)
    sideA = StringVar()
    sideB = StringVar()
    sideC = StringVar()

    entrya = Entry(top, textvariable=sideA, width=82)
    entrya.place(x=40, y=2)
    labelb = Label(top, text='Side B')
    labelb.place(x=2, y=20)
    entryb = Entry(top, textvariable=sideB, width=82)
    entryb.place(x=40, y=20)
    labelc = Label(top, text='Side C')
    labelc.place(x=2, y=40)
    entryc = Entry(top, textvariable=sideC, width=82)
    entryc.place(x=40, y=40)
    entryc.configure(state="disabled")
    Button(top, text="Calculate", width=7, command=lambda: computearea(sideA.get(), sideB.get())).place(x=100, y=70)
    Button(top, text="Exit", width=7, command=root.destroy).place(x=160, y=70)

    def computearea(s1, s2):
        # messagebox.showinfo("Login", "Hey there")
        s3 = (int(s1) ** 2) + (int(s2) ** 2)
        s3 = s3 ** 0.5
        sideC.set('{:.3f}'.format(s3))




def open_window(user, password):
    pass_text = open('users.txt', 'r')
    line = pass_text.readline()
    while (line != ''):
        lin = line.strip()
        ar = lin.split("|")
        # print(ar[0])
        # print(user)
        if (ar[0] == user and ar[1] == password):
            compute_area()
            # messagebox.showinfo("Login", "Hey there")
            break
            # quit()
            # compute_area()
        else:
            line = pass_text.readline()
    else:
        messagebox.showwarning("Login", " Please try again")
        pass

    pass_text.close()


Button(root, text="Login", width=7, command=lambda: open_window(username.get(), password.get())).place(x=100, y=220)
Button(root, text="Exit", width=7, command=root.destroy).place(x=160, y=220)
root.mainloop()




