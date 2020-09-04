from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id== "" or name== "" or phone==""):
        MessageBox.showinfo("Insert Status","All Fields are Required")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="python_tkinter")
        cursor = con.cursor()
        query = "insert into students values('"+ id +"','"+ name +"','"+ phone +"')"
        cursor.execute(query)
        cursor.execute("commit")
        con.close()
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        show()
        MessageBox.showinfo("Insert status","User added to database")

def delete():
    id = e_id.get()
    if(id==""):
        MessageBox.showinfor("Delete Status","Enter ID to be deleted")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="python_tkinter")
        cursor = con.cursor()
        query= "delete from students where id='"+id+"'"
        cursor.execute(query)
        cursor.execute("commit")
        con.close()
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        show()
        MessageBox.showinfo("Delete status","User Deleted from database")

def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id== "" or name== "" or phone==""):
        MessageBox.showinfo("Update Status","All Fields are Required")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="python_tkinter")
        cursor = con.cursor()
        query = "update students set name='"+ name +"',phone='"+ phone +"' where id = '"+ id +"'"
        cursor.execute(query)
        cursor.execute("commit")
        con.close()
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        show()
        MessageBox.showinfo("Update status","User Updated in database")

def get():
    id = e_id.get()
    if(id==""):
        MessageBox.showinfo("Fetch Status","Enter the ID to get information")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python_tkinter")
        cursor = con.cursor()
        query = "select * from students where id='"+ id +"'"
        cursor.execute(query)
        rows= cursor.fetchall()
        for row in rows:
            e_name.insert(0,row[1])
            e_phone.insert(0,row[2])
            
        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="", database="python_tkinter")
    cursor = con.cursor()
    query = "select * from students"
    cursor.execute(query)
    rows= cursor.fetchall()
    list.delete(0,list.size())
    for row in rows:
        InsertData= str(row[0])+'   '+row[1]+'   '+row[2]
        list.insert(list.size()+1, InsertData)
    con.close()

root = Tk()
root.geometry("900x600")
root.title("Python-Tkinter-Mysql Project")

id = Label(root, text="Enter ID", font =('bold',15))
id.place(x=20,y=30)

name = Label(root, text="Enter Name", font =('bold',15))
name.place(x=20,y=80)

phone = Label(root, text="Enter Phone", font =('bold',15))
phone.place(x=20,y=130)


e_id = Entry()
e_id.place(x=220,y=35)

e_name = Entry()
e_name.place(x=220,y=85)

e_phone = Entry()
e_phone.place(x=220,y=135)

insert = Button(root, font=("italic", 20),text="Insert" , bg="blue",command=insert)
insert.place(x=50, y=180)

delete = Button(root, font=("italic",20),text="Delete" ,bg="blue",command=delete)
delete.place(x=190, y=180)

update = Button(root, font=("italic",20),text="Update" ,bg="blue",command=update)
update.place(x=50, y=260)

get = Button(root, font=("italic",20),text="Get" ,bg="blue",command=get)
get.place(x=190, y=260)

list= Listbox(root)
list.place(x=425,y=35)
show()

root.mainloop()
