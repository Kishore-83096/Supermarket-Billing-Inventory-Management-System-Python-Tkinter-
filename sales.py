from tkinter import *
from tkinter import messagebox
from mysql.connector import connect,errors
from datetime import datetime
class sales:
    def D_sales(self,salesWin):
       def opendb():
           try:
               global connection
               connection = connect(host="localhost", user="root", password="Kishore@2000", database="Project1")
               global mycursor
               mycursor = connection.cursor()
               crttable_qry="CREATE TABLE IF NOT EXISTS Sales(Transaction_id INT AUTO_INCREMENT, ITEM_CODE VARCHAR(500), DATE_AND_TIME DATETIME, ITEM_QUANTITY VARCHAR(500), Total_Cost FLOAT DEFAULT 0, Mobile_Number VARCHAR(10), PRIMARY KEY(Transaction_id))"
               mycursor.execute(crttable_qry)
           except errors.Error as e:
               messagebox.showinfo("Error", e)
       salesWin.title("Stock Input")
       salesWin.state("zoomed")
       salesWin.configure(bg="Antique white")
       salesWin.grab_set()
       hdframe = Frame(salesWin, bg="Antique White", height=100, width=100)
       hdframe.place(x=700, y=50)
       hdlbl = Label(hdframe, text="SALES", font=("Lato Regular", 30), fg="#3C1414", bg="Antique White")
       hdlbl.pack()

       fr1=Frame(salesWin,bg="#EDC9AF",width=750,height=500,highlightbackground="#3C1414",highlightthickness=2)
       fr1.place(x=10,y=200)

       fr2 = Frame(salesWin, bg="#EDC9AF", width=750, height=500, highlightbackground="#3C1414", highlightthickness=2)
       fr2.place(x=775, y=200)
       txtfld = Text(fr2, font=("Lato Regular", 15), fg="#3C1414", bg="White", height=14, width=66, background="white")
       txtfld.place(x=9, y=10)
       txtfld.config(state="disabled")
       scrollb = Scrollbar(fr2, orient="vertical", command=txtfld.yview)
       scrollb.place(x=720, y=11, height=324, width=20)
       txtfld.configure(yscrollcommand=scrollb.set)
       txtfld.config(state="normal")
       txtfld.insert(END, "ITEM CODE \t\t MRP \t\t QUANTITY \t\t PRICE \n")
       txtfld.insert(END, f'{90 * "-"}')
       txtfld.config(state="disabled")

       itemcode=Label(fr1,text="ITEM CODE :",font=("Lato Regular",17),fg="#3C1414",bg="#EDC9AF")
       itemcode.place(x=10,y=10)

       def validate(P):
           if len(P) <= 5:
               return True
           else:
               return False
       vcmd1 = (salesWin.register(validate), '%P')
       itmcdentry=Entry(fr1,font=("Lato Regular",17),fg="#3C1414",bg="White",width=32,validate="key",validatecommand=vcmd1)
       itmcdentry.place(x=170,y=10)

       itname=Label(fr1,text="ITEM NAME :",font=("Lato Regular",17),fg="#3C1414",bg="#EDC9AF")
       itname.place(x=10,y=60)
       def allowonlyalpha(char):
           return char == "" or all(char.isalpha() or char.isspace() for char in char)
       vcmd2 = (salesWin.register(allowonlyalpha), '%S')
       itnameentry=Entry(fr1,font=("Lato Regular",17),fg="#3C1414",bg="White",width=32,validate="key",validatecommand=vcmd2)
       itnameentry.place(x=170,y=60)
       itnameentry.config(state="disabled")

       itemrp=Label(fr1,text="ITEM MRP    :",font=("Lato Regular",17),fg="#3C1414",bg="#EDC9AF")
       itemrp.place(x=10,y=110)
       itemrpentry=Entry(fr1,font=("Lato Regular",17),fg="#3C1414",bg="White",width=32)
       itemrpentry.place(x=170,y=110)
       itemrpentry.config(state="disabled")

       dtlbl=Label(fr1,text="DATE            :",font=("Lato Regular",17),fg="#3C1414",bg="#EDC9AF")
       dtlbl.place(x=10,y=160)
       dtedl=Entry(fr1,font=("Lato Regular",17),fg="#3C1414",bg="White",width=32)
       dtedl.place(x=170,y=160)
       dtedl.insert(0,datetime.now().strftime("%d/%m/%Y %H:%M"),)
       dtedl.config(state="disabled")

       qnty=Label(fr1,text="QUANTITY   :",font=("Lato Regular",17),fg="#3C1414",bg="#EDC9AF")
       qnty.place(x=10,y=210)
       def validate(value):
           return value.isdigit() or value == ""
       vcmd5 = (salesWin.register(validate), '%P')
       quntyentry=Entry(fr1,font=("Lato Regular",17),fg="#3C1414",bg="White",width=15,validate="key",validatecommand=vcmd5)
       quntyentry.place(x=170,y=210)

       available=Label(fr1,text="Available:",font=("Lato Regular",17),fg="#3C1414",bg="#EDC9AF")
       available.place(x=380,y=210)
       availableentry=Entry(fr1,font=("Lato Regular",17),fg="#3C1414",bg="White",width=7)
       availableentry.place(x=495,y=210)
       availableentry.config(state="disabled")

       pricelbl=Label(fr1,text="PRICE          :",font=("Lato Regular",17),fg="#3C1414",bg="#EDC9AF")
       pricelbl.place(x=10,y=260)
       priceentry=Entry(fr1,font=("Lato Regular",17),fg="#3C1414",bg="White",width=32)
       priceentry.place(x=170,y=260)
       priceentry.config(state="disabled")

       mbnolbl=Label(fr1,text="MOBILE NO :",font=("Lato Regular",17),fg="#3C1414",bg="#EDC9AF")
       mbnolbl.place(x=10,y=310)
       def allowonlytennum(P):
           if P == "" or P.replace(".", "", 1).isdigit() and len(P) <= 10:
               return True
           return False
       vcmd6 = (salesWin.register(allowonlytennum), '%P')
       mbnoentry=Entry(fr1,font=("Lato Regular",17),fg="#3C1414",bg="White",width=32,validate="key",validatecommand=vcmd6,state="disabled")
       mbnoentry.place(x=170,y=310)

       transid=Label(fr1,text="TRANS ID    :",font=("Lato Regular",17),fg="#3C1414",bg="#EDC9AF")
       transid.place(x=10,y=360)
       transidentry=Entry(fr1,font=("Lato Regular",17),fg="#3C1414",bg="White",width=32)
       transidentry.place(x=170,y=360)
       transidentry.insert(0,"Auto generated by system.")
       transidentry.config(state="disabled")


       def find():
           if len(itmcdentry.get()) > 0:
               if len(itmcdentry.get()) == 5:
                   opendb()
                   srch_qry = "SELECT count(*) FROM Inventory WHERE ITEM_CODE = %s"
                   mycursor.execute(srch_qry, (itmcdentry.get(),))
                   cbuf=mycursor.fetchone()
                   if cbuf[0] == 1:
                       fillqry1 = "SELECT * FROM INVENTORY WHERE ITEM_CODE = %s"
                       mycursor.execute(fillqry1, (itmcdentry.get(),))
                       fbuf = mycursor.fetchall()
                       itnameentry.config(state="normal")
                       itemrpentry.config(state="normal")
                       itnameentry.delete(0, END)
                       itemrpentry.delete(0, END)
                       itnameentry.insert(0, fbuf[0][1])
                       itemrpentry.insert(0, fbuf[0][2])
                       itnameentry.config(state="disabled")
                       itemrpentry.config(state="disabled")

                       srch_qry2 = "SELECT count(*) FROM Stock_input WHERE ITEM_CODE = %s"
                       mycursor.execute(srch_qry2, (itmcdentry.get(),))
                       cbuf2 = mycursor.fetchone()
                       if cbuf2[0] == 1:
                           fillqry2 = "SELECT ITEM_QUANTITY FROM Stock_input WHERE ITEM_CODE = %s"
                           mycursor.execute(fillqry2, (itmcdentry.get(),))
                           fbuf2 = mycursor.fetchall()
                           availableentry.config(state="normal")
                           availableentry.delete(0, END)
                           availableentry.insert(0, fbuf2[0][0])
                           availableentry.config(state="disabled")
                           mycursor.close()
                           connection.close()
                       else:
                           availableentry.config(state="normal")
                           availableentry.delete(0, END)
                           availableentry.config(state="disabled")
                           messagebox.showinfo("Error", "Item Code does not exist in Stock Input")
                           mycursor.close()
                           connection.close()
                           return
                   else:
                       messagebox.showinfo("Error", "Item Code does not exist")
                       mycursor.close()
                       connection.close()
                       return
               else:
                   messagebox.showinfo("Error", "Item Code must be 5 characters long")
           else:
               messagebox.showinfo("Error", "Item Code is required")
               return

       findbtn=Button(fr1,text="Search",font=("Lato Regular",10),fg="Antique White", bg="#3C1414",width=5,height=0,command=find)
       findbtn.place(x=600,y=10)

       def confirmbtn():
           if len(quntyentry.get()) > 0:
               if len(availableentry.get()) > 0:
                   if int(quntyentry.get()) <= int(availableentry.get()):
                       price = float(itemrpentry.get()) * int(quntyentry.get())
                       priceentry.config(state="normal")
                       priceentry.delete(0, END)
                       priceentry.insert(0, price)
                       priceentry.config(state="disabled")
                   else:
                       quntyentry.delete(0, END)
                       messagebox.showinfo("Error", f"only {availableentry.get()} items are available in the stock")
                       return
               else:
                   messagebox.showinfo("Error", "Available quantity is required to confirm the transaction.")
                   return
           else:
               messagebox.showinfo("Error", "Item quantity is required")
               return
       confirmbtn=Button(fr1,text="CONFIRM",font=("Lato Regular",10),fg="Antique White", bg="#3C1414",width=10,height=0,command=confirmbtn)
       confirmbtn.place(x=600,y=210)

       cd=[]
       mr=[]
       qt=[]
       avai=[]
       pric=[]
       def cart():
           if len(itmcdentry.get()) > 0:
               if len(itmcdentry.get()) == 5:
                   if len(itnameentry.get()) > 0:
                       if len(itemrpentry.get()) > 0:
                           if len(quntyentry.get()) > 0:
                               if len(priceentry.get()) > 0:
                                   code = itmcdentry.get()
                                   mrp = itemrpentry.get()
                                   qty = quntyentry.get()
                                   avail =availableentry.get()
                                   price = priceentry.get()
                                   txtfld.config(state="normal")
                                   txtfld.insert(END,f"\n {code}  \t\t {mrp} \t\t  {qty} \t\t  {price}")
                                   txtfld.config(state="disabled")
                                   cd.append(code)
                                   mr.append(float(mrp))
                                   qt.append(int(qty))
                                   avai.append(int(avail))
                                   pric.append(float(price))
                                   clr()
                               else:
                                   messagebox.showinfo("Error", "Price is required")
                                   return
                           else:
                               messagebox.showinfo("Error", "Quantity is required")
                               return
                       else:
                           messagebox.showinfo("Error", "Item Price is required")
                           return
                   else:
                       messagebox.showinfo("Error", "Item Name is required")
                       return
               else:
                   messagebox.showinfo("Error", "Item Code must be 5 characters long")
                   return
           else:
               messagebox.showinfo("Error", "Item Code is required")
               return

       addtobill=Button(fr1,text="ADD TO CART",font=("Lato Regular",14),fg="Antique White", bg="#3C1414",width=12,height=0,command=cart)
       addtobill.place(x=10,y=420)

       def clr():
           itmcdentry.config(state="normal")
           itnameentry.config(state="normal")
           itemrpentry.config(state="normal")
           availableentry.config(state="normal")
           priceentry.config(state="normal")
           itmcdentry.delete(0, END)
           itnameentry.delete(0, END)
           itemrpentry.delete(0, END)
           quntyentry.delete(0, END)
           availableentry.delete(0, END)
           priceentry.delete(0, END)
           mbnoentry.delete(0, END)
           itnameentry.config(state="disabled")
           itemrpentry.config(state="disabled")
           availableentry.config(state="disabled")
           priceentry.config(state="disabled")
       clrbtn=Button(fr1,text="CLEAR",font=("Lato Regular",14),fg="Antique White", bg="#3C1414",width=12,height=0,command=clr)
       clrbtn.place(x=448,y=420)

       mbnolbl = Label(fr2, text="MOBILE NO :", font=("Lato Regular", 17), fg="#3C1414", bg="#EDC9AF")
       mbnolbl.place(x=10, y=350)
       def allowonlytennum(P):
           if P == "" or P.replace(".", "", 1).isdigit() and len(P) <= 10:
               return True
           return False
       vcmd7 = (salesWin.register(allowonlytennum), '%P')
       mbinoentry = Entry(fr2, font=("Lato Regular", 17), fg="#3C1414", bg="White", width=32, validate="key",validatecommand=vcmd7)
       mbinoentry.place(x=170, y=350)

       def cnf():
           if len(cd) > 0:
               if len(qt) > 0:
                   txtfld.config(state="normal")
                   txtfld.delete(f"{len(cd)+3}.0", END)
                   txtfld.insert(END, f"\n{"-" * 90}\n")
                   txtfld.insert(END, f"TOTAL \t\t\t\t\t\t {sum(pric)}\n")
                   txtfld.config(state="disabled")
                   itmcdentry.config(state="disabled")
                   quntyentry.config(state="disabled")
                   purchasebtn.config(state="normal")
               else:
                   messagebox.showinfo("Error", "item code is required")
                   return
           else:
               messagebox.showinfo("Error", "item quantity is required")
               return
       cnfr = Button(fr2, text="CONFIRM", font=("Lato Regular", 20), fg="Antique White", bg="#3C1414", width=12,height=0,command=cnf)
       cnfr.place(x=9, y=420)

       def pur():
           if len(mbinoentry.get()) > 0:
               if len(mbinoentry.get()) == 10:
                   if len(cd) > 0:
                       if len(mr) > 0:
                           if len(qt) > 0:
                               opendb()
                               insertqry = """Insert into Sales (ITEM_CODE, DATE_AND_TIME, ITEM_QUANTITY, Total_Cost, Mobile_Number) values (%s, %s, %s, %s, %s)"""
                               values = (str(cd), datetime.now(), str(qt), sum(pric), mbinoentry.get())
                               mycursor.execute(insertqry, values)
                               for i in range(0,len(cd)):
                                   print(cd[i],qt[i],avai[i]-qt[i],pric[i])
                                   updateqry = """Update Stock_input set ITEM_QUANTITY = ITEM_QUANTITY - %s where ITEM_CODE = %s"""
                                   values = (qt[i], cd[i])
                                   mycursor.execute(updateqry, values)
                               crttblq2="CREATE TABLE IF NOT EXISTS Salessub(ITEM_CODE VARCHAR(500),QUANTITY_SOLD INT,QUANTITY_REMAINING INT,MRP FLOAT,SELLING_COST FLOAT)"
                               mycursor.execute(crttblq2)
                               for i in range(0,len(cd)):
                                   chkq="SELECT count(*) FROM Salessub WHERE ITEM_CODE = %s"
                                   mycursor.execute(chkq, (cd[i],))
                                   result=mycursor.fetchone()
                                   if result[0] == 0:
                                       insq="INSERT INTO Salessub values(%s,%s,%s,%s,%s)"
                                       values=(cd[i],qt[i],avai[i]-qt[i],mr[i],pric[i])
                                       mycursor.execute(insq,values)
                                   elif result[0] == 1:
                                       updq2 = """
                                           UPDATE Salessub 
                                           SET QUANTITY_SOLD = QUANTITY_SOLD + %s,
                                               QUANTITY_REMAINING = QUANTITY_REMAINING - %s,
                                               SELLING_COST = SELLING_COST + %s 
                                           WHERE ITEM_CODE = %s
                                       """
                                       values = (qt[i], qt[i], pric[i], cd[i])
                                       mycursor.execute(updq2, values)

                                       purchasebtn.config(state="disabled")
                                       messagebox.showinfo("Success", "ITEMS SOLD")
                                   else:
                                       print(result[0])
                               mycursor.execute(crttblq2)
                               connection.commit()
                               mycursor.close()
                               connection.close()
                               cncl()
                           else:
                               messagebox.showinfo("Error", "Quantity is required")
                               return
                       else:
                           messagebox.showinfo("Error", "MRP is required")
                           return
                   else:
                       messagebox.showinfo("Error", "Item Code is required")
                       return
               else:
                   messagebox.showinfo("Error", "Mobile Number must be 10 digits long")
                   return
           else:
               messagebox.showinfo("Error", "Mobile Number is required")
               return

       purchasebtn=Button(fr2,text="SELL",font=("Lato Regular",20),fg="Antique White", bg="#3C1414",width=12,height=0,command=pur)
       purchasebtn.place(x=305,y=420)
       purchasebtn.config(state="disabled")

       def cncl():
           txtfld.config(state="normal")
           txtfld.delete(3.0, END)
           txtfld.config(state="disabled")
           mbinoentry.delete(0, END)
           cd.clear()
           mr.clear()
           pric.clear()
           avai.clear()
           qt.clear()
           itmcdentry.config(state="normal")
           quntyentry.config(state="normal")
       cancelbtn=Button(fr2,text="CANCEL",font=("Lato Regular",20),fg="Antique White", bg="#3C1414",command=cncl)
       cancelbtn.place(x=605,y=420)

       def viewdb():
           viewdbwin = Toplevel()
           viewdbwin.title("View Database")
           viewdbwin.state('zoomed')
           viewdbwin.grab_set()
           viewdbwin.configure(bg="Antique White")
           swhdframe = Frame(viewdbwin, bg="Antique White", height=100, width=100)
           swhdframe.place(x=500, y=50)
           hdlbl1 = Label(swhdframe, text="Sales DATABASE", font=("Lato Regular", 30), fg="#3C1414",
                          bg="Antique White")
           hdlbl1.pack()

           screen_width1 = viewdbwin.winfo_screenwidth()
           screen_height1 = viewdbwin.winfo_screenheight()

           frame_width1 = 1200
           frame_height1 = 500

           x1 = (screen_width1 - frame_width1) // 2
           y1 = (screen_height1 - frame_height1) // 2

           swcenframe = Frame(viewdbwin, bg="#EDC9AF", width=frame_width1, height=frame_height1,
                              highlightbackground="#3C1414", highlightthickness=2)
           swcenframe.place(x=x1, y=y1)

           txtfld = Text(swcenframe, font=("Lato Regular", 20), fg="#3C1414", bg="White", width=78, height=15.49)
           txtfld.place(x=10, y=5)
           scrollb = Scrollbar(swcenframe, orient="vertical", command=txtfld.yview)
           scrollb.place(x=1163, y=6, height=481, width=20)
           txtfld.configure(yscrollcommand=scrollb.set)
           txtfld.config(state="disabled")
           opendb()
           sslqry="Select * from Sales"
           mycursor.execute(sslqry)
           fbuf=mycursor.fetchall()
           txtfld.config(state="normal")
           txtfld.insert(END, f"{"Trans_id" :<20}{"Item Code":<20}{"Date/Time":<20}{"Item Qunatity" :<20}{"Total" :<20}{"Mbno"}\n")
           txtfld.insert(END, f"{'-' * 90}\n")
           for i in fbuf:
               txtfld.config(state="normal")
               txtfld.insert(END, f"{i[0]:<20} {i[1] :<20}\n")
               txtfld.config(state="disabled")

       viwdb=Button(salesWin,text="View Database",font=("Lato Regular",20),fg="Antique White", bg="#3C1414",width=15, height=1,command=viewdb)
       viwdb.place(x=10,y=720)
       viwdb['state']='disabled'

       quitbtn=Button(salesWin,text="QUIT",font=("Lato Regular",20),fg="Antique White", bg="#3C1414",command=salesWin.destroy)
       quitbtn.place(x=1435,y=720)


       salesWin.mainloop()
Class = sales()