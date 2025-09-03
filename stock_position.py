from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from mysql.connector import connect,errors


class stock_position:
    def D_stock_pos(self,stkposW):

        def opendb():
            try:
                global connection
                connection = connect(host="localhost", user="root", password="Kishore@2000", database="Project1")
                global mycursor
                mycursor = connection.cursor()
            except errors.Error as e:
                messagebox.showinfo("Error", e)

        stkposW.title("Stock Position")
        stkposW.state("zoomed")
        stkposW.configure(bg="Antique white")
        stkposW.grab_set()


        hdframe = Frame(stkposW, bg="Antique White", height=100, width=100)
        hdframe.place(x=615, y=50)
        hdlbl = Label(hdframe, text="STOCK POSITION", font=("Lato Regular", 30), fg="#3C1414", bg="Antique White")
        hdlbl.pack()

        screen_width = stkposW.winfo_screenwidth()
        screen_height = stkposW.winfo_screenheight()
        frame_width = 900
        frame_height = 500
        x = (screen_width - frame_width) // 2
        y = (screen_height - frame_height) // 2
        cenframe = Frame(stkposW, bg="#EDC9AF", width=frame_width, height=frame_height, highlightbackground="#3C1414",highlightthickness=2)
        cenframe.place(x=x, y=y)

        cdlbl = Label(cenframe, text="ITEM CODE       :", font=("Lato Regular", 15), fg="#3C1414", bg="#EDC9AF")
        cdlbl.place(x=150, y=140)
        cdentry = Entry(cenframe, font=("Lato Regular", 15), fg="#3C1414", bg="White", width=32,state="disabled")
        cdentry.place(x=335, y=140)


        nmlb = Label(cenframe, text="ITEM NAME       :", font=("Lato Regular", 15), fg="#3C1414", bg="#EDC9AF")
        nmlb.place(x=150, y=180)
        nmentry = Entry(cenframe, font=("Lato Regular", 15), fg="#3C1414", bg="White", width=32,state="disabled")
        nmentry.place(x=335, y=180)

        mrplb = Label(cenframe, text="ITEM MRP         :", font=("Lato Regular", 15), fg="#3C1414", bg="#EDC9AF")
        mrplb.place(x=150, y=220)
        mrpentry = Entry(cenframe, font=("Lato Regular", 15), fg="#3C1414", bg="White", width=32,state="disabled")
        mrpentry.place(x=335, y=220)

        qtremlb = Label(cenframe, text="QTY LEFT         :", font=("Lato Regular", 15), fg="#3C1414", bg="#EDC9AF")
        qtremlb.place(x=150, y=260)
        qtrementry = Entry(cenframe, font=("Lato Regular", 15), fg="#3C1414", bg="White", width=32,state="disabled")
        qtrementry.place(x=335, y=260)

        qtysdlb = Label(cenframe, text="QTY SOLD        :", font=("Lato Regular", 15), fg="#3C1414", bg="#EDC9AF")
        qtysdlb.place(x=150, y=300)
        qtysdedntry = Entry(cenframe, font=("Lato Regular", 15), fg="#3C1414", bg="White", width=32,state="disabled")
        qtysdedntry.place(x=335, y=300)

        totallb = Label(cenframe, text="TOTAL MRP      :", font=("Lato Regular", 15), fg="#3C1414", bg="#EDC9AF")
        totallb.place(x=150, y=340)
        totalentry = Entry(cenframe, font=("Lato Regular", 15), fg="#3C1414", bg="White", width=32,state="disabled")
        totalentry.place(x=335, y=340)

        lb1=Label(cenframe,text="SELECT FROM DROPDOWNBOX",font=("Arial",15),fg="#3C1414",bg="#EDC9AF")
        lb1.place(x=300,y=15)


        def update2combo(event):
            opendb()
            option=combo1.get()
            l=[]
            if option=="ITEM CODE":
                srcg1="SELECT ITEM_CODE FROM INVENTORY"
                mycursor.execute(srcg1)
                fbuf1=mycursor.fetchall()
                l.clear()
                for i in fbuf1:
                    l.append(i[0])
                combo2["values"]=l
                mycursor.close()
                connection.close()

            elif option=="ITEM NAME":
                srcg2="SELECT ITEM_NAME FROM INVENTORY"
                mycursor.execute(srcg2)
                fbuf2=mycursor.fetchall()
                l.clear()
                for i in fbuf2:
                    l.append(i[0])
                combo2["values"]=l
                mycursor.close()
                connection.close()

            else:
                messagebox.showinfo("Error","Invalid Option Selected")

        options=["ITEM CODE","ITEM NAME"]
        combo1=Combobox(cenframe,values=options,font=("Lato Regular",15),state='readonly')
        combo1.place(x=150,y=60)
        combo1.current(0)
        combo1.bind("<<ComboboxSelected>>",update2combo)

        def updateentrybox(event):
            option1=combo2.get()
            def fill():
                opendb()
                print(option1)
                fillqry="SELECT ITEM_CODE,ITEM_NAME,ITEM_MRP FROM INVENTORY WHERE ITEM_CODE=%s OR ITEM_NAME=%s"
                mycursor.execute(fillqry,(option1,option1,))
                fbuf=mycursor.fetchall()
                fillqry1 = "SELECT QUANTITY_REMAINING, QUANTITY_SOLD,SELLING_COST FROM Salessub WHERE ITEM_CODE=%s"
                mycursor.execute(fillqry1,(fbuf[0][0],))
                fbuf1=mycursor.fetchall()
                cdentry.config(state="normal")
                nmentry.config(state="normal")
                mrpentry.config(state="normal")
                cdentry.delete(0,END)
                nmentry.delete(0,END)
                mrpentry.delete(0,END)
                cdentry.insert(0, fbuf[0][0])
                nmentry.insert(0, fbuf[0][1])
                mrpentry.insert(0, fbuf[0][2])
                cdentry.config(state="disabled")
                nmentry.config(state="disabled")
                mrpentry.config(state="disabled")
                print(fbuf1)
                if len(fbuf1)>0:
                    qtrementry.config(state="normal")
                    qtysdedntry.config(state="normal")
                    totalentry.config(state="normal")
                    qtrementry.delete(0, END)
                    qtysdedntry.delete(0, END)
                    totalentry.delete(0, END)
                    qtrementry.insert(0,fbuf1[0][0])
                    qtysdedntry.insert(0,fbuf1[0][1])
                    totalentry.insert(0,fbuf1[0][2])
                    qtrementry.config(state="disabled")
                    qtysdedntry.config(state="disabled")
                    totalentry.config(state="disabled")
                else:
                    fillqry2 = "SELECT ITEM_QUANTITY from Stock_input WHERE ITEM_CODE=%s"
                    mycursor.execute(fillqry2, (fbuf[0][0],))
                    fbuf2 = mycursor.fetchone()

                    qtrementry.config(state="normal")
                    qtysdedntry.config(state="normal")
                    totalentry.config(state="normal")
                    qtrementry.delete(0, END)
                    qtysdedntry.delete(0, END)
                    totalentry.delete(0, END)

                    qtrementry.insert(0, fbuf2[0])
                    qtysdedntry.insert(0, "0")
                    totalentry.insert(0, "0")

                    qtrementry.config(state="disabled")
                    qtysdedntry.config(state="disabled")
                    totalentry.config(state="disabled")

            if combo1.get()=="ITEM CODE":
                fill()

            elif combo1.get()=="ITEM NAME":
                fill()

        combo2=Combobox(cenframe,values=options,font=("Lato Regular",15),state="readonly")
        combo2.place(x=450,y=60)
        combo2.bind("<<ComboboxSelected>>",updateentrybox)
        update2combo(None)

        def viewdb():
            viewbdW=Toplevel()
            viewbdW.title("View Database")
            viewbdW.state("zoomed")
            viewbdW.configure(bg="Antique white")
            swhdframe = Frame(viewbdW, bg="Antique White", height=100, width=100)
            swhdframe.place(x=570, y=50)
            hdlbl1 = Label(swhdframe, text="SALES DATABASE", font=("Lato Regular", 30), fg="#3C1414",bg="Antique White")
            hdlbl1.pack()
            screen_width1 = viewbdW.winfo_screenwidth()
            screen_height1 = viewbdW.winfo_screenheight()

            frame_width1 = 1500
            frame_height1 = 500

            x1 = (screen_width1 - frame_width1) // 2
            y1 = (screen_height1 - frame_height1) // 2

            swcenframe = Frame(viewbdW, bg="#EDC9AF", width=frame_width1, height=frame_height1,highlightbackground="#3C1414", highlightthickness=2)
            swcenframe.place(x=x1, y=y1)

            txtfld = Text(swcenframe, font=("Lato Regular", 20), fg="#3C1414", bg="White", width=95, height=15.49)
            txtfld.place(x=30, y=5)
            scrollb = Scrollbar(swcenframe, orient="vertical", command=txtfld.yview)
            scrollb.place(x=1440, y=6, height=481, width=20)

            txtfld.configure(yscrollcommand=scrollb.set)
            txtfld.config(state="disabled")

            def showdata():
                try:
                    opendb()
                    qr1 = "SELECT t2.item_name,t1.* FROM salessub t1 INNER JOIN inventory t2 ON t1.ITEM_CODE = t2.ITEM_CODE"
                    mycursor.execute(qr1)
                    fbuf = mycursor.fetchall()
                    txtfld.config(state="normal")
                    txtfld.delete(1.0, END)
                    txtfld.insert(END, "ITEM NAME\t\tITEM CODE\t\tQTY SOLD\t\tQTY LEFT\t\tITEM MRP\t\tTOTAL MRP\n")
                    txtfld.insert(END, "-"* 150 +"\n")

                    for i in fbuf:
                        txtfld.insert(END, str(i[0]) + "\t\t" + str(i[1]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + str(i[4]) + "\t\t" + str(i[5]) +"\n")
                    txtfld.config(state="disabled")
                    mycursor.close()
                    connection.close()
                except errors.Error as e:
                    messagebox.showinfo("Error", e)
            showdata()
            closebtn=Button(viewbdW,text="Close",font=("Lato Regular",30),fg="Antique White",bg="#3C1414",command=viewbdW.destroy)
            closebtn.place(x=700,y=700)

        vwdb=Button(stkposW,text="View Database",font=("Lato Regular",30),fg="Antique White",bg="#3C1414",command=viewdb)
        vwdb.place(x=317,y=700)

        closebtn = Button(stkposW, text="Close", font=("Lato Regular", 30), fg="Antique White", bg="#3C1414",command=stkposW.destroy)
        closebtn.place(x=1080, y=700)
        stkposW.mainloop()

Class=stock_position()
