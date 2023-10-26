from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Library:

    def __init__(self,root):
        self.root = root
        self.root.title("Library Management Systems")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')



        lbltitle=Label(self.root,text = "LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold")padx=2,pady=6)
        lbltitle.pack(side=Top,fill=x)

        frame = Frame(self.root,bd=12,relief=RIDGE,bg="powder blue")
        fram.place(x=0,y=130,width=1530,height=400)

        #=============================Members===============================

        DataFrameLeft = LabelFrame(frame,text = "Members",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",50,"bold")padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue",text = "Member Type" , font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=w)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["value"]=("Librarian","Student","Teachers")
        comMember.grid(row=0,column=1)

        lblPRN_no. = Label(DataFrameLeft, bg="powder blue",text = "Member Type" , font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_no..grid(row=1,column=1,sticky=w)

        txtPRN_no.=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29)
        txtPRn_no..grid(row=1,column=1)

        lblBookID = Label(DataFrameLeft, bg="powder blue",text = "Member Type" , font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBookID.grid(row=2,column=1,sticky=w)

        txtBookID=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29)
        txtBookID.grid(row=2,column=1)


        #===========================Transactions============================
        

        
        

        DataFrameRight = LabelFrame(frame,text = "Books with stock maintained",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",50,"bold")padx=2,pady=6)
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        lblBookprice = Label(DataFrameLeft, bg="powder blue",text = "Member Type" , font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBookprice.grid(row=0,column=1,sticky=w)

        txtBookprice=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29)
        txtBookprice.grid(row=0,column=1)

        frame = Frame(self.root,bd=12,relief=RIDGE,bg="powder blue")
        fram.place(x=0,y=530,width=1530,height=400)

        DataFrame = LabelFrame(frame,text = "Transactions",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",50,"bold")padx=2,pady=6)
        DataFrame.place(x=920,y=5,width=540,height=350)

        #========================Buttons===================================


        mebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        mebutton.place(x=0,y=530,width=1530,height=70)
        


        btnAddData=Button(Framebutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)


if __name__ =='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()

        
        
        

        

        

        

        

        

        
        






        
        
        






        
        




