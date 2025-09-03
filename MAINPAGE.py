from tkinter import *
class Mainpage():
    def D_mainpage(self):
        MainW=Tk()
        MainW.title("Main Page")
        MainW.state("zoomed")
        MainW.configure(bg="Antique White")
        hdframe=Frame(MainW,bg="Antique White",height=100,width=100)
        hdframe.place(x=650,y=50)
        headlbl=Label(hdframe,text="HOMEPAGE",font=("Lato Regular",30),fg="#3C1414",bg="Antique White")
        headlbl.pack()

        screen_width = MainW.winfo_screenwidth()
        screen_height = MainW.winfo_screenheight()

        frame_width = 1000
        frame_height = 500

        x = (screen_width - frame_width) // 2
        y = (screen_height - frame_height) // 2

        cenframe=Frame(MainW,bg="#EDC9AF",width=frame_width, height=frame_height,highlightbackground="#3C1414",highlightthickness=2)
        cenframe.place(x=x, y=y)

        def invntry():
            from inventory import Class
            InvW=Toplevel()
            Class.D_inventory(InvW)
        invntrybtn=Button(cenframe,text="Inventory",font=("Lato Regular",30),fg="#3C1414",bg="Antique White",width=12,height=1,command=invntry)
        invntrybtn.place(x=150,y=100)

        def stkinp():
            from StockInput import Class
            stknpW=Toplevel()
            Class.D_stockinput(stknpW)
        stkinptbtn=Button(cenframe,text="Stock Entry",font=("Lato Regular",30),fg="#3C1414",bg="Antique White",width=12,height=1,command=stkinp)
        stkinptbtn.place(x=600,y=100)

        def sales():
            from sales import Class
            salesW=Toplevel()
            Class.D_sales(salesW)
        salesbtn=Button(cenframe,text="Sales",font=("Lato Regular",30),fg="#3C1414",bg="Antique White",width=12,height=1,command=sales)
        salesbtn.place(x=150,y=300)

        def stkpos():
            from stock_position import Class
            stkposW = Tk()
            Class.D_stock_pos(stkposW)
        stkposbtn=Button(cenframe,text="Stock Position",font=("Lato Regular",30),fg="#3C1414",bg="Antique White",width=12,height=1,command=stkpos)
        stkposbtn.place(x=600,y=300)

        closebtn=Button(MainW,text="Close",font=("Lato Regular",30),fg="Antique White",bg="#3C1414",command=MainW.destroy)
        closebtn.place(x=700,y=700)

        MainW.mainloop()

Class=Mainpage()
Class.D_mainpage()

