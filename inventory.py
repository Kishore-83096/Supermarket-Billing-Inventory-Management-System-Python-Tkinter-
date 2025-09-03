from tkinter import *
from tkinter import messagebox
from mysql.connector import connect,errors

class Inventory:
    def D_inventory(self,InvW):
        def opendb():
            try:
                global connection
                connection = connect(host="localhost",user="root",password="Kishore@2000")
                global mycursor
                mycursor = connection.cursor()
                mycursor.execute("CREATE DATABASE IF NOT EXISTS Project1")
                connection.database = "Project1"
                print("Project1 Database Connected")
                crtetbl_query = "CREATE TABLE IF NOT EXISTS INVENTORY(ITEM_CODE VARCHAR(5)  PRIMARY KEY, ITEM_NAME VARCHAR(31), ITEM_MRP FLOAT DEFAULT 0)"
                mycursor.execute(crtetbl_query)
            except errors.Error as e:
                messagebox.showinfo("Error",e)
        InvW.title("Inventory")
        InvW.state("zoomed")
        #InvW.grab_set()
        InvW.configure(bg="Antique White")
        hdframe=Frame(InvW,bg="White",height=100,width=100)
        hdframe.place(x=650,y=50)
        hdlbl=Label(hdframe,text="INVENTORY",font=("Lato Regular",30),fg="#3C1414",bg="Antique White")
        hdlbl.pack()


        screen_width = InvW.winfo_screenwidth()
        screen_height = InvW.winfo_screenheight()

        frame_width = 900
        frame_height = 500

        x = (screen_width - frame_width) // 2
        y = (screen_height - frame_height) // 2

        cenframe = Frame(InvW, bg="#EDC9AF", width=frame_width, height=frame_height, highlightbackground="#3C1414", highlightthickness=2)
        cenframe.place(x=x, y=y)

        itmcodelbl = Label(cenframe, text="ITEM CODE :", font=("Lato Regular", 20), fg="#3C1414", bg="#EDC9AF")
        itmcodelbl.place(x=100, y=100)
        def validate(P):
            if len(P) <= 5:
                return True
            else:
                return False
        vcmd1 = (InvW.register(validate), '%P')
        itmcodeentry = Entry(cenframe, font=("Lato Regular", 20), fg="#3C1414", bg="White",width=32,validate="key",validatecommand=vcmd1)
        itmcodeentry.place(x=300, y=100)

        itmnamelbl = Label(cenframe, text="ITEM NAME :", font=("Lato Regular", 20), fg="#3C1414", bg="#EDC9AF")
        itmnamelbl.place(x=100, y=180)

        def allowonlyalpha(char):
            return char == "" or all(char.isalpha() or char.isspace() for char in char)
        vcmd2 = (InvW.register(allowonlyalpha), '%S')
        itmnameentry = Entry(cenframe, font=("Lato Regular", 20), fg="#3C1414", bg="White",width=32,validate="key",validatecommand=vcmd2)
        itmnameentry.place(x=300, y=180)

        mrplbl=Label(cenframe,text="ITEM MRP   :",font=("Lato Regular",20),fg="#3C1414",bg="#EDC9AF")
        mrplbl.place(x=100,y=260)

        def allowonlynum(P):
            if P == "" or P.replace(".", "", 1).isdigit() and len(P) <= 9:
                return True
            return False

        vcmd3 = (InvW.register(allowonlynum), '%P')
        mrpentry=Entry(cenframe,font=("Lato Regular",20),fg="#3C1414",bg="White",width=32,validate="key",validatecommand=vcmd3)
        mrpentry.place(x=300,y=260)

        def savedb():
            if len(itmcodeentry.get()) > 0:
                if len(itmcodeentry.get()) == 5:
                    if len(itmnameentry.get()) > 0:
                        if len(mrpentry.get()) > 0:
                            opendb()
                            itmcode = itmcodeentry.get()
                            itmname = itmnameentry.get()
                            mrp = mrpentry.get()
                            srch_query = "SELECT count(*) FROM INVENTORY WHERE ITEM_CODE = %s"
                            mycursor.execute(srch_query, (itmcode,))
                            counterbuf = mycursor.fetchone()
                            if counterbuf[0] == 0:
                                insert_query = "INSERT INTO INVENTORY VALUES(%s,%s,%s)"
                                values = (itmcode, itmname, mrp)
                                mycursor.execute(insert_query, values)
                                print("Data Inserted")
                                itmcodeentry.delete(0, END)
                                itmnameentry.delete(0, END)
                                mrpentry.delete(0, END)
                                mycursor.close()
                                connection.commit()
                                connection.close()
                                print("Database Connection Closed")
                            else:
                                itmcodeentry.delete(0, END)
                                messagebox.showinfo("Error","Item Code already exists")
                                return
                        else:
                            messagebox.showinfo("Error","MRP is required")
                            return
                    else:
                        messagebox.showinfo("Error","Item Name is required")
                        return
                else:
                    messagebox.showinfo("Error","Item Code must be 5 characters long")
            else:
                messagebox.showinfo("Error","Item Code is required")
                return
        savebtn=Button(cenframe,text="ADD",font=("Lato Regular",15),fg="#3C1414",bg="Antique White",width=7,height=1,command=savedb)
        savebtn.place(x=100,y=380)

        def edit():
            if len(itmcodeentry.get()) > 0:
                if len(itmcodeentry.get()) == 5:
                    if len(itmnameentry.get()) > 0:
                        if len(mrpentry.get()) > 0:
                            opendb()
                            itmcode = itmcodeentry.get()
                            itmname = itmnameentry.get()
                            mrp = mrpentry.get()
                            srch_query = "SELECT count(*) FROM INVENTORY WHERE ITEM_CODE = %s"
                            mycursor.execute(srch_query, (itmcode,))
                            counterbuf = mycursor.fetchone()
                            if counterbuf[0] == 1:
                                editqry = "UPDATE INVENTORY SET ITEM_NAME = %s, ITEM_MRP = %s WHERE ITEM_CODE = %s"
                                editqry2="UPDATE Salessub SET  MRP = %s WHERE ITEM_CODE = %s"
                                values = (itmname, mrp, itmcode)
                                mycursor.execute(editqry, values)
                                mycursor.execute(editqry2, (mrp, itmcode))
                                print("Data Updated")
                                itmcodeentry.delete(0, END)
                                itmnameentry.delete(0, END)
                                mrpentry.delete(0, END)
                                mycursor.close()
                                connection.commit()
                                connection.close()
                                print("Database Connection Closed")

                            else:
                                itmcodeentry.delete(0, END)
                                messagebox.showinfo("Error","Item Code does not exist to edit")
                        else:
                            messagebox.showinfo("Error","MRP is required")
                            return
                    else:
                        messagebox.showinfo("Error","Item Name is required")
                        return
                else:
                    messagebox.showinfo("Error","Item Code must be 5 characters long")
                    return
            else:
                messagebox.showinfo("Error","Item Code is required")
                return
        editbtn=Button(cenframe,text="EDIT",font=("Lato Regular",15),fg="#3C1414",bg="Antique White",width=7,height=1,command=edit)
        editbtn.place(x=300,y=380)

        def find():
            if len(itmcodeentry.get()) > 0:
                if len(itmcodeentry.get()) == 5:
                    opendb()
                    itmcode = itmcodeentry.get()
                    srch_query = "SELECT count(*) FROM INVENTORY WHERE ITEM_CODE = %s"
                    mycursor.execute(srch_query, (itmcode,))
                    counterbuf = mycursor.fetchone()
                    if counterbuf[0] == 1:
                        fetch_query = "SELECT * FROM INVENTORY WHERE ITEM_CODE = %s"
                        mycursor.execute(fetch_query, (itmcode,))
                        myresult = mycursor.fetchone()
                        itmnameentry.delete(0, END)
                        mrpentry.delete(0, END)
                        itmnameentry.insert(0, myresult[1])
                        mrpentry.insert(0, myresult[2])
                        mycursor.close()
                        connection.close()
                        print("Database Connection Closed")
                    else:
                        messagebox.showinfo("Error", "Item Code does not exist")
                        return
        findbtn=Button(cenframe,text="FIND",font=("Lato Regular",15),fg="#3C1414",bg="Antique White",width=6,height=1,command=find)
        findbtn.place(x=800,y=98)

        def delete():
            if len(itmcodeentry.get()) > 0:
                if len(itmcodeentry.get()) == 5:
                    opendb()
                    itmcode = itmcodeentry.get()
                    srch_query = "SELECT count(*) FROM INVENTORY WHERE ITEM_CODE = %s"
                    mycursor.execute(srch_query, (itmcode,))
                    counterbuf = mycursor.fetchone()
                    if counterbuf[0] == 1:
                        delqry = "DELETE FROM INVENTORY WHERE ITEM_CODE = %s"
                        mycursor.execute(delqry, (itmcode,))
                        print("Data Deleted")
                        itmcodeentry.delete(0, END)
                        itmnameentry.delete(0, END)
                        mrpentry.delete(0, END)
                        mycursor.close()
                        connection.commit()
                        connection.close()
                    else:
                        messagebox.showinfo("Error", "Item Code does not exist")
                        return
                else:
                    messagebox.showinfo("Error", "Item Code must be 5 characters long")
                    return
            else:
                messagebox.showinfo("Error", "Item Code is required")
                return
        deletebtn=Button(cenframe,text="DELETE",font=("Lato Regular",15),fg="#3C1414",bg="Antique White",width=7,height=1,command=delete)
        deletebtn.place(x=490,y=380)

        def cncl():
            itmcodeentry.delete(0, END)
            itmnameentry.delete(0, END)
            mrpentry.delete(0, END)
        Cancelbtn=Button(cenframe,text="CLEAR",font=("Lato Regular",15),fg="#3C1414",bg="Antique White",width=7,height=1,command=cncl)
        Cancelbtn.place(x=700,y=380)

        def viewdb():
            viewdbwin=Toplevel()
            viewdbwin.title("View Database")
            viewdbwin.state('zoomed')
            viewdbwin.configure(bg="Antique White")
            #viewdbwin.grab_set()
            swhdframe=Frame(viewdbwin,bg="Antique White",height=100,width=100)
            swhdframe.place(x=500,y=50)
            hdlbl=Label(swhdframe,text="INVENTORY DATABASE",font=("Lato Regular",30),fg="#3C1414",bg="Antique White")
            hdlbl.pack()

            screen_width = InvW.winfo_screenwidth()
            screen_height = InvW.winfo_screenheight()

            frame_width = 900
            frame_height = 500

            x = (screen_width - frame_width) // 2
            y = (screen_height - frame_height) // 2

            swcenframe = Frame(viewdbwin, bg="#EDC9AF", width=frame_width, height=frame_height, highlightbackground="#3C1414",highlightthickness=2)
            swcenframe.place(x=x, y=y)

            txtfld=Text(swcenframe,font=("Lato Regular",20),fg="#3C1414",bg="White",width=58,height=15.49)
            txtfld.place(x=10,y=5)
            scrollb = Scrollbar(swcenframe, orient="vertical", command=txtfld.yview)
            scrollb.place(x=864, y=7, height=481, width=20)
            txtfld.configure(yscrollcommand=scrollb.set)
            txtfld.config(state="disabled")
            def showinvdb():
                try:
                    opendb()
                    selciventbl_query = "SELECT * FROM INVENTORY"
                    mycursor.execute(selciventbl_query)
                    data = mycursor.fetchall()
                    txtfld.config(state="normal")
                    txtfld.delete("1.0", END)
                    txtfld.insert(END, "ITEM CODE\t\tITEM NAME\t\t\tMRP\n")
                    txtfld.insert(END, "-" * 90 + "\n")
                    for i in data:
                        txtfld.insert(END,"{i[0]}\t\t{i[1]}\t\t\t{i[2]}\n".format(i=i))
                    txtfld.config(state="disabled")
                    mycursor.close()
                    connection.close()
                    print("Database Connection Closed")
                except errors.Error as e1:
                    messagebox.showinfo("Error",e1)
            showinvdb()


            rfshbtn=Button(viewdbwin,text="Refesh",font=("Lato Regular",20),fg="Antique White",bg="#3C1414",command=showinvdb)
            rfshbtn.place(x=316,y=700)
            closebtn=Button(viewdbwin,text="CLOSE",font=("Lato Regular",20),fg="Antique White",bg="#3C1414",command=viewdbwin.destroy)
            closebtn.place(x=1100, y=700)

        viewdb=Button(InvW,text="VIEW ALL ITEMS",font=("Lato Regular",20),fg="Antique White",bg="#3C1414",width=15,height=1,command=viewdb)
        viewdb.place(x=316,y=700)

        closebtn = Button(InvW, text="QUIT", font=("Lato Regular", 20), fg="Antique White", bg="#3C1414",command=InvW.destroy)
        closebtn.place(x=1128, y=700)
        InvW.mainloop()
Class=Inventory()