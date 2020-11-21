#front end

from tkinter import*
import tkinter.messagebox
import DB_Backend



class Customer:

    def __init__(self, root):
        self.root = root
        self.root.title("Customer Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg = "cadet blue")

        custID = StringVar()
        firstName = StringVar()
        lastName = StringVar()
        dofB = StringVar()

#functions------------

        def iExit():
            iExit = tkinter.messagebox.askyesno("Customer Database Management System", "Confirm you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtcustID.delete(0, END)
            self.txtfirstName.delete(0, END)
            self.txtlastName.delete(0, END)
            self.txtdofB.delete(0, END)

        def addData():
            if(len(custID.get()) !=0):
                DB_Backend.addCustRec(custID.get(), firstName.get(), lastName.get(), dofB.get())
                customerlist.delete(0, END)
                customerlist.insert(END, (custID.get(), firstName.get(), lastName.get(), dofB.get()))
        
        def displayData():
                customerlist.delete(0, END)
                for row in DB_Backend.viewData():
                    customerlist.insert(END, row, str(""))

        def customerRec(event):
            global sd
            searchCust = customerlist.curselection() [0]
            sd = customerlist.get(searchCust)
            self.txtcustID.delete(0, END)
            self.txtcustID.insert(END, sd[1])
            self.txtfirstName.delete(0, END)
            self.txtfirstName.insert(END, sd[2])
            self.txtlastName.delete(0, END)
            self.txtlastName.insert(END, sd[3])
            self.txtdofB.delete(0, END)
            self.txtdofB.insert(END, sd[4])

        def deleteData():
            if(len(custID.get()) !=0):
                DB_Backend.deleteRec(sd[0])
                clearData()
                displayData()

        def searchDatabase():
            customerlist.delete(0, END)
            for row in DB_Backend.searchData (custID.get(), firstName.get(), lastName.get(), dofB.get()):
                customerlist.insert (END, row, str(""))

        def update():
            if(len(custID.get())!=0):
                DB_Backend.deleteRec(sd[0])
            if(len(custID.get())!=0):
                DB_Backend.addCustRec (custID.get(), firstName.get(), lastName.get(), dofB.get())
                customerlist.delete (0, END)
                customerlist.insert (END, (custID.get(), firstName.get(), lastName.get(), dofB.get()))
        

#frames---------------
        mainFrame = Frame (self.root, bg = "cadet blue")
        mainFrame.grid()

        titleFrame = Frame (mainFrame, bd = 2, padx = 54, pady = 8, bg = "Ghost White", relief = RIDGE)
        titleFrame.pack(side = TOP)

        self.lblTitle = Label(titleFrame, font = ("arial", 47, "bold"), text = "Customer Database Management System", bg = "Ghost White")
        self.lblTitle.grid()

        buttonFrame = Frame (mainFrame, bd = 2, width = 1350, height = 70, padx = 18, pady = 10, bg = "Ghost White", relief = RIDGE)
        buttonFrame.pack(side = BOTTOM)

        dataFrame = Frame (mainFrame, bd = 1, width = 1300, height = 400, padx = 20, pady = 20, bg = "cadet blue", relief = RIDGE)
        dataFrame.pack(side = BOTTOM)

        dataFrameLeft = LabelFrame (dataFrame, bd = 1, width = 1000, height = 600, padx = 20, bg = "Ghost White", relief = RIDGE, font = ("arial", 20, "bold"), text = "Customer Info\n")
        dataFrameLeft.pack(side = LEFT)

        dataFrameRight = LabelFrame (dataFrame, bd = 1, width = 450, height = 300, padx = 31, pady = 3, bg = "Ghost White", relief = RIDGE, font = ("arial", 20, "bold"), text = "Customer Details\n")
        dataFrameRight.pack(side = RIGHT)

#labels and entry widgets---------------

        self.lblcustID = Label(dataFrameLeft, font = ("arial", 20, "bold"),padx = 2, pady = 2, text = "Customer ID", bg = "Ghost White")
        self.lblcustID.grid(row = 0, column = 0, sticky = W)
        self.txtcustID = Entry(dataFrameLeft, font = ("arial", 20, "bold"), width = 39, textvariable = custID)
        self.txtcustID.grid(row = 0, column = 1)

        self.lblfirstName = Label(dataFrameLeft, font = ("arial", 20, "bold"),padx = 2, pady = 2, text = "First Name", bg = "Ghost White")
        self.lblfirstName.grid(row = 1, column = 0, stick = W)
        self.txtfirstName = Entry(dataFrameLeft, font = ("arial", 20, "bold"), width = 39, textvariable = firstName)
        self.txtfirstName.grid(row = 1, column = 1)

        self.lbllastName = Label(dataFrameLeft, font = ("arial", 20, "bold"),padx = 2, pady = 2, text = "Last Name", bg = "Ghost White")
        self.lbllastName.grid(row = 2, column = 0, sticky = W)
        self.txtlastName = Entry(dataFrameLeft, font = ("arial", 20, "bold"), width = 39, textvariable = lastName)
        self.txtlastName.grid(row = 2, column = 1)

        self.lbldofB = Label(dataFrameLeft, font = ("arial", 20, "bold"),padx = 2, pady = 2, text = "Date of Birth", bg = "Ghost White")
        self.lbldofB.grid(row = 3, column = 0, sticky = W)
        self.txtdofB = Entry(dataFrameLeft, font = ("arial", 20, "bold"), width = 39, textvariable = dofB)
        self.txtdofB.grid(row = 3, column = 1)

#Listbox and scrollbar widget---------------

        scrollbar = Scrollbar (dataFrameRight)
        scrollbar.grid(row = 0, column = 1, sticky = "ns")

        customerlist = Listbox (dataFrameRight, width = 41, height = 16, font = ("arial", 12, "bold"), yscrollcommand = scrollbar.set)
        customerlist.bind("<<ListboxSelect>>", customerRec)
        customerlist.grid(row = 0, column = 0, padx = 8)
        scrollbar.config(command = customerlist.yview)

#Button widget---------------

        self.btnAddDate = Button (buttonFrame, command = addData, text = "Add New", font = ("arial", 15, "bold"), height = 1, width = 10, bd = 4)
        self.btnAddDate.grid(row = 0, column =0)

        self.btnDisplayData = Button (buttonFrame, command = displayData, text = "Display", font = ("arial", 15, "bold"), height = 1, width = 10, bd = 4)
        self.btnDisplayData.grid(row = 0, column =1)
        
        self.btnClearData = Button (buttonFrame, command = clearData, text = "Clear", font = ("arial", 15, "bold"), height = 1, width = 10, bd = 4)
        self.btnClearData.grid(row = 0, column =2)

        self.btnDeleteData = Button (buttonFrame, command = deleteData, text = "Delete", font = ("arial", 15, "bold"), height = 1, width = 10, bd = 4)
        self.btnDeleteData.grid(row = 0, column =3)

        self.btnSearchData = Button (buttonFrame, command = searchDatabase, text = "Search", font = ("arial", 15, "bold"), height = 1, width = 10, bd = 4)
        self.btnSearchData.grid(row = 0, column =4)

        self.btnUpdateData = Button (buttonFrame, command = update, text = "Update", font = ("arial", 15, "bold"), height = 1, width = 10, bd = 4)
        self.btnUpdateData.grid(row = 0, column =5)

        self.btnExitData = Button (buttonFrame, command = iExit, text = "Exit", font = ("arial", 15, "bold"), height = 1, width = 10, bd = 4)
        self.btnExitData.grid(row = 0, column =6)



if __name__=="__main__":
    root = Tk()
    application = Customer(root)
    root.mainloop()
