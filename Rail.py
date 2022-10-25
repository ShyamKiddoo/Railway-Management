import cx_Oracle
from tkinter import *
from tkinter import messagebox


def connect():
    con = cx_Oracle.connect('xe/ssn@localhost:1521/xe')   
    cursor = con.cursor()
    return con, cursor

def delete():
    con, cur = connect()
    s = str(e10.get())
    cur.execute(f"delete from user_details where user_id = '{s}'")
    lb.delete(0,END)
    
    messagebox.showinfo("Message","Record deleted!")
    con.commit()



def insert_win():
    def insert():
        id = int(e1.get())
        password = str(e2.get())
        name = str(e3.get())
        gender = str(e4.get())
        age = int(e5.get())
        ad_no = int(e6.get())
        mob_no = int(e7.get())
        city = str(e8.get())
        pin = int(e9.get())
        
        con, c = connect()
        c.execute(f"insert into user_details values ({id}, '{password}', '{name}', '{gender}',{age},{ad_no},{mob_no},'{city}',{pin})")
        c.close()

        messagebox.showinfo("Message","Record inserted")
        con.commit()
        con.close()

    win = Toplevel(root)
    win.geometry("400x400")
    e1 = Entry(win)
    e1.place(x=200,y=25)


    e2 = Entry(win)
    e2.place(x=200,y=50)

    e3 = Entry(win)
    e3.place(x=200,y=75)

    e4 = Entry(win)
    e4.place(x=200,y=100)

    e5 = Entry(win)
    e5.place(x=200,y=125)

    e6 = Entry(win)
    e6.place(x=200,y=150)

    e7 = Entry(win)
    e7.place(x=200,y=175)

    e8 = Entry(win)
    e8.place(x=200,y=200)

    e9 = Entry(win)
    e9.place(x=200,y=225)

    l1 = Label(win, text='ID',font="Calibri 12",bg='Black',fg='White')
    l1.place(x=100,y=25)

    l2 = Label(win, text="Password",font="Calibri 12",bg='Black',fg='White')
    l2.place(x=100,y=50)

    l3 = Label(win, text="Name",font="Calibri 12",bg='Black',fg='White')
    l3.place(x=100,y=75)

    l4 = Label(win, text="Gender",font="Calibri 12",bg='Black',fg='White')
    l4.place(x=100,y=100)

    l5 = Label(win, text="Age",font="Calibri 12",bg='Black',fg='White')
    l5.place(x=100,y=125)

    l6 = Label(win, text="Aadhar no",font="Calibri 12",bg='Black',fg='White')
    l6.place(x=100,y=150)

    l7 = Label(win, text="Mobile no",font="Calibri 12",bg='Black',fg='White')
    l7.place(x=100,y=175)

    l8 = Label(win, text="State",font="Calibri 12",bg='Black',fg='White')
    l8.place(x=100,y=200)

    l9 = Label(win, text="Pincode",font="Calibri 12",bg='Black',fg='White')
    l9.place(x=100,y=225)

    inst = Button(win, text="Insert",font="Calibri 14 bold", command=insert,bg='Yellow')
    inst.place(x =140 , y=270)

def disp_win():
    def search():
        con, cur = connect()
        s = str(e10.get())
        for i in cur.execute(f"select booked_by,seat_no,status,cost from pass_details p, ticket t where p.pass_id=t.pass_id and p.user_id = '{s}'"):
            lb.insert('end', i[0])
            lb.insert('end', i[1])
            lb.insert('end', i[2])
            lb.insert('end', i[3])
    
    def search1():
        con, cur = connect()
        s = str(e11.get())
        for i in cur.execute(f"select train_name, source, destination, arr_time, dept_time, avl_of_seats from train where train_no = '{s}'"):
            for j in i:
                lb1.insert('end', j)

    win = Toplevel(root)
    win.geometry("700x600")

    lb = Listbox(win, width=15,font="Calibri 14 bold",bg='cyan')
    lb.place(x=150,y=250)

    lb1= Listbox(win, width=15,font="Calibri 14 bold",bg='cyan')
    lb1.place(x=450,y=250)

    e10 = Entry(win)
    e10.place(x=400,y=30)

    e11= Entry(win)
    e11.place(x=400,y=80)

    l10=Label(win, text="Enter User ID:",font="Calibri 12",bg='Black',fg='White')
    l10.place(x=200,y=30)

    l11=Label(win, text="Enter Train No.:",font="Calibri 12",bg='Black',fg='White')
    l11.place(x=200,y=80)

    b1 = Button(win,text="Display reservation status",command=search,font="Calibri 12 bold",bg='green')
    b1.place(x=250,y=125)

    b2 = Button(win,text="Display Train details",command=search1,font="Calibri 12 bold",bg='green')
    b2.place(x=250,y=180)

    l12=Label(win, text="Name:",font="Calibri 12",bg='Black',fg='White')
    l12.place(x=90,y=250)

    l13=Label(win, text="Seat No:",font="Calibri 12",bg='Black',fg='White')
    l13.place(x=90,y=275)

    l14=Label(win, text="Status:",font="Calibri 12",bg='Black',fg='White')
    l14.place(x=90,y=300)

    l15=Label(win, text="Cost:",font="Calibri 12",bg='Black',fg='White')
    l15.place(x=90,y=325)

    l16=Label(win, text="Train Name:",font="Calibri 12",bg='Black',fg='White')
    l16.place(x=350,y=250)

    l17=Label(win, text="Source:",font="Calibri 12",bg='Black',fg='White')
    l17.place(x=350,y=275)

    l18=Label(win, text="Destination:",font="Calibri 12",bg='Black',fg='White')
    l18.place(x=350,y=300)

    l19=Label(win, text="Arr. time:",font="Calibri 12",bg='Black',fg='White')
    l19.place(x=350,y=325)

    l20=Label(win, text="Dept. time:",font="Calibri 12",bg='Black',fg='White')
    l20.place(x=350,y=350)

    l21=Label(win, text="Avl. seats",font="Calibri 12",bg='Black',fg='White')
    l21.place(x=350,y=375)


def delete_win():
    def delete():
        con, cur = connect()
        s = str(e10.get())
        cur.execute(f"delete from user_details where user_id = '{s}'")
        
        messagebox.showinfo("Message","Record deleted!")
        con.commit()

    win = Toplevel(root)
    win.geometry("400x300")

    l10=Label(win, text="Enter User ID:",font="Calibri 12",bg='Black',fg='White')
    l10.place(x=100,y=50)

    e10 = Entry(win)
    e10.place(x=200,y=50)

    b3 = Button(win,text="Delete User Details",command=delete,font="Calibri 12 bold",bg='red')
    b3.place(x=150,y=100)

root = Tk()
root.geometry('400x400')

bg = PhotoImage(file = "C:/Users/Sai shyam/OneDrive/Desktop/n2.png")
imglabel = Label( root, image = bg)
imglabel.place(x = 0, y = 0)

Label(text="Railway Management System", fg="red", font="Calibri 40 bold").pack(pady=(100,20))

inst = Button(root, text="Register user",font="Calibri 20 bold", command=insert_win,bg='Yellow')
inst.pack(pady=(160,10))

b2 = Button(root,text="Display Train details",command=disp_win,font="Calibri 20 bold",bg='green')
b2.pack(pady=(10,10))

b3 = Button(root,text="Delete User Details",command=delete_win,font="Calibri 20 bold",bg='red')
b3.pack(pady=(10,10))


root.mainloop()