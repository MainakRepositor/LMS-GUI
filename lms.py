from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import sqlite3
image1='library.png'
image2='image2.png'
image3='finance.png'
#pip install Pillow
class menu:

    def __init__(self):
        self.root=Tk()
        self.root.title('Menu')
        self.root.state('zoomed')
        conn=sqlite3.connect('test.db')
        conn.execute('''create table if not exists book_info
        (ID VARCHAR PRIMARY KEY NOT NULL,
        TITLE VARTEXT NOT NULL,
        AUTHOR VARTEXT NOT NULL,
        GENRE VARTEXT NOT NULL,
        COPIES VARINT NOT NULL,
        LOCATION VARCHAR NOT NULL);''')
        conn.commit()
        conn.execute('''create table if not exists book_issued
        (BOOK_ID VARCHAR NOT NULL,
        STUDENT_ID VARCHAR NOT NULL,
        ISSUE_DATE DATE NOT NULL,
        RETURN_DATE DATE NOT NULL,
        PRIMARY KEY (BOOK_ID,STUDENT_ID));''')
        conn.commit()
        conn.close()
        self.a=self.canvases(image1)
        l1=Button(self.a,text='BOOK DATA',font='Papyrus 22 bold',fg='Yellow',bg='Black',width=19,padx=10,borderwidth=0,command=self.book).place(x=100,y=500)
        l2=Button(self.a,text='STUDENT DATA',font='Papyrus 22 bold',fg='Yellow',bg='Black',width=19,padx=10,borderwidth=0,command=self.student).place(x=800,y=500)
        self.root.mainloop()
    def canvases(self,images):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        #photo=PhotoImage(file=images)
        photo=Image.open(images)
        photo1=photo.resize((w,h),Image.ANTIALIAS)
        photo2=ImageTk.PhotoImage(photo1)

        #photo2 = ImageTk.PhotoImage(Image.open(images).resize((w, h)),Image.ANTIALIAS)
        self.canvas = Canvas(self.root, width='%d'%w, height='%d'%h)
        self.canvas.grid(row = 0, column = 0)
        self.canvas.grid_propagate(0)
        self.canvas.create_image(0, 0, anchor = NW, image=photo2)
        self.canvas.image=photo2
        return self.canvas
    def book(self):
        self.a.destroy()
        self.a=self.canvases(image2)
        l1=Button(self.a,text='Add Books',font='Papyrus 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.addbook).place(x=12,y=100)
        l2=Button(self.a,text='Search Books',font='Papyrus 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.search).place(x=12,y=200)

        l4=Button(self.a,text='All Books',font='Papyrus 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.all).place(x=12,y=300)
        l4=Button(self.a,text='<< Main Menu',font='Papyrus 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.mainmenu).place(x=12,y=500)





    def addbook(self):
        self.aid=StringVar()
        self.aauthor=StringVar()
        self.aname=StringVar()
        self.acopies=IntVar()
        self.agenre=StringVar()
        self.aloc=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Papyrus 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=50)
        e1=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.aid).place(x=150,y=50)
        l2=Label(self.f1,text='Title : ',font='Papyrus 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=100)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.aname).place(x=150,y=100)
        l3=Label(self.f1,text='Author : ',font='Papyrus 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=150)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.aauthor).place(x=150,y=150)
        l4=Label(self.f1,text='Genre : ',font='Papyrus 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=200)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.agenre).place(x=150,y=200)
        l4=Label(self.f1,text='Copies : ',font='Papyrus 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=250)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.acopies).place(x=150,y=250)
        l5=Label(self.f1,text='Location : ',font='Papyrus 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=300)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.aloc).place(x=150,y=300)
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Add',font='Papyrus 10 bold',fg='black',bg='white',width=15,bd=3,command=self.adddata).place(x=150,y=400)
        b2=Button(self.f1,text='Back',font='Papyrus 10 bold',fg='black',bg='white',width=15,bd=3,command=self.rm).place(x=350,y=400)

    def rm(self):
        self.f1.destroy()
    def mainmenu(self):
        self.root.destroy()
        a=menu()

    def adddata(self):
        a=self.aid.get()
        b=self.aname.get()
        c=self.aauthor.get()
        d=self.agenre.get()
        e=self.acopies.get()
        f=self.aloc.get()
        conn=sqlite3.connect('test.db')
        try:
            if (a and b and c and d  and f)=="":
                messagebox.showinfo("Error","Fields cannot be empty.")
            else:
                conn.execute("insert into book_info \
                values (?,?,?,?,?,?)",(a.capitalize(),b.capitalize(),c.capitalize(),d.capitalize(),e,f.capitalize(),));
                conn.commit()
                messagebox.showinfo("Success","Book added successfully")
        except sqlite3.IntegrityError:
            messagebox.showinfo("Error","Book is already present.")


        conn.close()

    def search(self):
        #self.search.state('zoomed')
        self.sid=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID/Title/Author/Genre: ',font=('Papyrus 10 bold'),bd=2, fg='white',bg='black').place(x=20,y=40)
        e1=Entry(self.f1,width=25,bd=5,bg='white',fg='black',textvariable=self.sid).place(x=260,y=40)
        b1=Button(self.f1,text='Search',bg='white',font='Papyrus 10 bold',width=9,bd=2,command=self.serch1).place(x=500,y=37)
        b1=Button(self.f1,text='Back',bg='white',font='Papyrus 10 bold',width=10,bd=2,command=self.rm).place(x=250,y=450)

    def create_tree(self,plc,lists):
        self.tree=ttk.Treeview(plc,height=13,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=100)
            n=n+1
        return self.tree


    def serch1(self):
        k=self.sid.get()
        if k!="":
            self.list4=("BOOK ID","TITLE","AUTHOR","GENRE","COPIES","LOCATION")
            self.trees=self.create_tree(self.f1,self.list4)
            self.trees.place(x=25,y=150)
            conn=sqlite3.connect('test.db')

            c=conn.execute("select * from book_info where ID=? OR TITLE=? OR AUTHOR=? OR GENRE=?",(k.capitalize(),k.capitalize(),k.capitalize(),k.capitalize(),))
            a=c.fetchall()
            if len(a)!=0:
                for row in a:

                    self.trees.insert("",END,values=row)
                conn.commit()
                conn.close()
                self.trees.bind('<<TreeviewSelect>>')
                self.variable = StringVar(self.f1)
                self.variable.set("Select Action:")


                self.cm =ttk.Combobox(self.f1,textvariable=self.variable ,state='readonly',font='Papyrus 15 bold',height=50,width=15,)
                self.cm.config(values =('Add Copies', 'Delete Copies', 'Delete Book'))

                self.cm.place(x=50,y=100)
                self.cm.pack_propagate(0)


                self.cm.bind("<<ComboboxSelected>>",self.combo)
                self.cm.selection_clear()
            else:
                messagebox.showinfo("Error","Data not found")



        else:
            messagebox.showinfo("Error","Search field cannot be empty.")


    def combo(self,event):
        self.var_Selected = self.cm.current()
        #l7=Label(self.f1,text='copies to update: ',font='Papyrus 10 bold',bd=1).place(x=250,y=700)
        if self.var_Selected==0:
            self.copies(self.var_Selected)
        elif self.var_Selected==1:
            self.copies(self.var_Selected)
        elif self.var_Selected==2:
            self.deleteitem()
    def deleteitem(self):
        try:
            self.curItem = self.trees.focus()

            self.c1=self.trees.item(self.curItem,"values")[0]
            b1=Button(self.f1,text='Update',font='Papyrus 10 bold',width=9,bd=3,command=self.delete2).place(x=500,y=97)

        except:
            messagebox.showinfo("Empty","Please select something.")
    def delete2(self):
        conn=sqlite3.connect('test.db')
        cd=conn.execute("select * from book_issued where BOOK_ID=?",(self.c1,))
        ab=cd.fetchall()
        if ab!=0:
            conn.execute("DELETE FROM book_info where ID=?",(self.c1,));
            conn.commit()
            messagebox.showinfo("Successful","Book Deleted sucessfully.")
            self.trees.delete(self.curItem)
        else:
            messagebox.showinfo("Error","Book is Issued.\nBook cannot be deleted.")
        conn.commit()
        conn.close()


    def copies(self,varr):
        try:
            curItem = self.trees.focus()
            self.c1=self.trees.item(curItem,"values")[0]
            self.c2=self.trees.item(curItem,"values")[4]
            self.scop=IntVar()
            self.e5=Entry(self.f1,width=20,textvariable=self.scop)
            self.e5.place(x=310,y=100)
            if varr==0:
                b5=Button(self.f1,text='Update',font='Papyrus 10 bold',bg='white',fg='black',width=9,bd=3,command=self.copiesadd).place(x=500,y=97)
            if varr==1:
                b6=Button(self.f1,text='Update',font='Papyrus 10 bold',bg='white',fg='black',width=9,bd=3,command=self.copiesdelete).place(x=500,y=97)
        except:
            messagebox.showinfo("Empty","Please select something.")

    def copiesadd(self):
        no=self.e5.get()
        if int(no)>=0:

            conn=sqlite3.connect('test.db')

            conn.execute("update book_info set COPIES=COPIES+? where ID=?",(no,self.c1,))
            conn.commit()

            messagebox.showinfo("Updated","Copies added sucessfully.")
            self.serch1()
            conn.close()

        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

    def copiesdelete(self):
        no1=self.e5.get()
        if int(no1)>=0:
            if int(no1)<=int(self.c2):
                conn=sqlite3.connect('test.db')

                conn.execute("update book_info set COPIES=COPIES-? where ID=?",(no1,self.c1,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Updated","Deleted sucessfully")
                self.serch1()

            else:
                messagebox.showinfo("Maximum","No. of copies to delete exceed available copies.")
        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

    def all(self):
        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        b1=Button(self.f1,text='Back',bg='white' ,fg='black',width=10,bd=3,command=self.rm).place(x=250,y=400)
        conn=sqlite3.connect('test.db')
        self.list3=("BOOK ID","TITLE","AUTHOR","GENRE","COPIES","LOCATION")
        self.treess=self.create_tree(self.f1,self.list3)
        self.treess.place(x=25,y=50)
        c=conn.execute("select * from book_info")
        g=c.fetchall()
        if len(g)!=0:
            for row in g:
                self.treess.insert('',END,values=row)
        conn.commit()
        conn.close()

    def student(self):
        self.a.destroy()
        self.a=self.canvases(image2)
        l1=Button(self.a,text='Issue book',font='Papyrus 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.issue).place(x=12,y=100)
        l2=Button(self.a,text='Return Book',font='Papyrus 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.returnn).place(x=12,y=200)
        l3=Button(self.a,text='Student Activity',font='Papyrus 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.activity).place(x=12,y=300)
        l4=Button(self.a,text='<< Main Menu',font='Papyrus 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.mainmenu).place(x=12,y=600)




    def issue(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=550,width=500,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='papyrus 15 bold',bg='black',fg='white').place(x=50,y=100)
        e1=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.aidd).place(x=180,y=100)
        l2=Label(self.f1,text='Student Id : ',font='papyrus 15 bold',bg='black',fg='white').place(x=50,y=150)
        e2=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=150)
        b1=Button(self.f1,text='Back',font='Papyrus 10 bold',fg='black',bg='white',width=10,bd=3,command=self.rm).place(x=50,y=250)
        b1=Button(self.f1,text='Issue',font='Papyrus 10 bold',fg='black',bg='white',width=10,bd=3,command=self.issuedbook).place(x=200,y=250)

    def issuedbook(self):
        bookid=self.aidd.get()
        studentid=self.astudentt.get()
        conn=sqlite3.connect('test.db')
        cursor=conn.cursor()
        cursor.execute("select ID,COPIES from book_info where ID=?",(bookid.capitalize(),))
        an=cursor.fetchall()
        if (bookid and studentid!=""):
            if an!=[]:
                for i in an:
                    if i[1]>0:
                        try:
                            conn.execute("insert into book_issued \
                            values (?,?,date('now'),date('now','+7 day'))",(bookid.capitalize(),studentid.capitalize(),));
                            conn.commit()
                            conn.execute("update book_info set COPIES=COPIES-1 where ID=?",(bookid.capitalize(),))
                            conn.commit()
                            conn.close()
                            messagebox.showinfo("Updated","Book Issued sucessfully.")
                        except:
                            messagebox.showinfo("Error","Book is already issued by student.")

                    else:
                        messagebox.showinfo("Unavailable","Book unavailable.\nThere are 0 copies of the book.")
            else:
                messagebox.showinfo("Error","No such Book in Database.")
        else:
            messagebox.showinfo("Error","Fields cannot be blank.")

    def returnn(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()

        self.f1=Frame(self.a,height=550,width=500,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='papyrus 15 bold',fg='white', bg='black').place(x=50,y=100)
        e1=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.aidd).place(x=180,y=100)
        l2=Label(self.f1,text='Student Id : ',font='papyrus 15 bold',fg='white', bg='black').place(x=50,y=150)
        e2=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=150)
        b1=Button(self.f1,text='Back',font='Papyrus 10 bold',bg='white',fg='black',width=10,bd=3,command=self.rm).place(x=50,y=250)
        b1=Button(self.f1,text='Return',font='Papyrus 10 bold',bg='white',fg='black',width=10,bd=3,command=self.returnbook).place(x=200,y=250)
        self.f1.grid_propagate(0)

    def returnbook(self):
        a=self.aidd.get()
        b=self.astudentt.get()

        conn=sqlite3.connect('test.db')

        fg=conn.execute("select ID from book_info where ID=?",(a.capitalize(),))
        fh=fg.fetchall()
        conn.commit()
        if fh!=None:
            c=conn.execute("select * from book_issued where BOOK_ID=? and STUDENT_ID=?",(a.capitalize(),b.capitalize(),))
            d=c.fetchall()
            conn.commit()
            if len(d)!=0:
                c.execute("DELETE FROM book_issued where BOOK_ID=? and STUDENT_ID=?",(a.capitalize(),b.capitalize(),));
                conn.commit()
                conn.execute("update book_info set COPIES=COPIES+1 where ID=?",(a.capitalize(),))
                conn.commit()

                messagebox.showinfo("Success","Book Returned sucessfully.")
            else:
                messagebox.showinfo("Error","Data not found.")
        else:
            messagebox.showinfo("Error","No such book.\nPlease add the book in database.")
        conn.commit()
        conn.close()

    def activity(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=550,width=500,bg='black')
        self.f1.place(x=500,y=80)
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        self.trees=self.create_tree(self.f1,self.list2)
        self.trees.place(x=50,y=150)


        l1=Label(self.f1,text='Book/Student ID : ',font='Papyrus 15 bold',fg='white',bg='black').place(x=50,y=30)
        e1=Entry(self.f1,width=20,bd=4,bg='white',textvariable=self.aidd).place(x=280,y=35)
        #l2=Label(self.f1,text='Student Id : ',font='papyrus 15 bold',fg='white',bg='black').place(x=50,y=80)
        #e2=Entry(self.f1,width=20,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=80)
        b1=Button(self.f1,text='Back',bg='white',font='Papyrus 10 bold',width=10,bd=3,command=self.rm).place(x=340,y=450)
        b1=Button(self.f1,text='Search',bg='white',font='Papyrus 10 bold',width=10,bd=3,command=self.searchact).place(x=40,y=450)
        b1=Button(self.f1,text='All',bg='white',font='Papyrus 10 bold',width=10,bd=3,command=self.searchall).place(x=190,y=450)
        self.f1.grid_propagate(0)

    def searchact(self):
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        self.trees=self.create_tree(self.f1,self.list2)
        self.trees.place(x=50,y=150)
        conn=sqlite3.connect('test.db')
        bid=self.aidd.get()
        #sid=self.astudentt.get()
        try:
            c=conn.execute("select * from book_issued where BOOK_ID=? or STUDENT_ID=?",(bid.capitalize(),bid.capitalize(),))
            d=c.fetchall()
            if len(d)!=0:
                for row in d:
                    self.trees.insert("",END,values=row)
            else:
                messagebox.showinfo("Error","Data not found.")
            conn.commit()

        except Exception as e:
            messagebox.showinfo(e)
        conn.close()

    def searchall(self):
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        self.trees=self.create_tree(self.f1,self.list2)
        self.trees.place(x=50,y=150)
        conn=sqlite3.connect('test.db')
        try:
            c=conn.execute("select * from book_issued")
            d=c.fetchall()
            for row in d:
                self.trees.insert("",END,values=row)

            conn.commit()

        except Exception as e:
            messagebox.showinfo(e)
        conn.close()

#===================START=======================
def canvases(images,w,h):
    photo=Image.open(images)
    photo1=photo.resize((w,h),Image.ANTIALIAS)
    photo2=ImageTk.PhotoImage(photo1)

#photo2 = ImageTk.PhotoImage(Image.open(images).resize((w, h)),Image.ANTIALIAS)
    canvas = Canvas(root, width='%d'%w, height='%d'%h)
    canvas.grid(row = 0, column = 0)
    canvas.grid_propagate(0)
    canvas.create_image(0, 0, anchor = NW, image=photo2)
    canvas.image=photo2
    return canvas
root = Tk()
root.title("LOGIN")
"""width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)"""

#root.state('zoomed')
#root.resizable(0, 0)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
canvas=canvases(image3,w,h)
#photo=PhotoImage(file=images)


#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("python1.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `login` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `login` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `login` (username, password) VALUES('Mainak', 'admin')")
        conn.commit()

def Login(event=None):
    Database()


    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("Error","Please complete the required field!")
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `login` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            #HomeWindow()
            #Top.destroy()
            root.destroy()

            #print("hello logged in ")
            a=menu()
            #USERNAME.set("")
            #PASSWORD.set("")
            #lbl_text.config(text="")
        else:
            messagebox.showinfo("Error","Invalid username or password.")
            #lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()

#==============================FRAMES=========================================
'''Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=BOTTOM, pady=20)'''
#==============================LABELS=========================================
lbl_title = Label(canvas, text = "ADMIN   LOGIN", font=('Papyrus', 30,'bold', ),bg='black', fg='white')
lbl_title.place(x=500,y=100)
lbl_username = Label(canvas, text = "Username:", font=('Papyrus', 15,'bold'),bd=4,bg='black', fg='white')
lbl_username.place(x=500,y=230)
lbl_password = Label(canvas, text = "Password :", font=('Papyrus', 15,'bold'),bd=3, bg='black', fg='white')
lbl_password.place(x=500, y=330)
lbl_text = Label(canvas)
lbl_text.place(x=450,y=500)
lbl_text.grid_propagate(0)



#==============================ENTRY WIDGETS==================================
username = Entry(canvas, textvariable=USERNAME, font=(14), bg='black', fg='white',bd=6)
username.place(x=650, y=230,)
password = Entry(canvas, textvariable=PASSWORD, show="*", font=(14),bg='black', fg='white',bd=6)
password.place(x=650, y=330)

#==============================BUTTON WIDGETS=================================
btn_login = Button(canvas, text="LOGIN", font=('Papyrus 15 bold'),width=25,command=Login, bg='black', fg='white')
btn_login.place(x=500,y=400)
btn_login.bind('<Return>', Login)
root.mainloop()
