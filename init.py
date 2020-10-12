from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime


class Income_Tax:
    def __init__(self, root):
        self.root = root
        self.root.title('Bayelsa Personel Income Tax Calculator')
        self.root.geometry('1360x800+0+0')
        self.root.configure(background = 'light blue')
        
        #===================================Frame = wages============================
        MainFrame = Frame(self.root)
        MainFrame.grid()
        
        TitleFrame =Frame(MainFrame, bd =10, width =1355,bg='light blue', relief = RIDGE )
        TitleFrame.pack(side=TOP)
        
        self.lblTitle = Label(TitleFrame, width=45,font=('areial',35,'bold'), text='Personal Income Tax Calculator',
                             padx=11,fg='white',bg='light blue')
        self.lblTitle.grid()
        
        BottomFrame =LabelFrame(MainFrame, bd =10,pady=5,padx=35, width =1355,height= 70,bg='light blue', relief = RIDGE,
                               font = ('arial',20, 'bold'),text='Personal Tax Summary',fg='white')
        BottomFrame.pack(side=BOTTOM)
        
        MiddleFrame =LabelFrame(MainFrame, bd =10,pady=5,padx=35, width =1355,height= 100,bg='light blue', relief = RIDGE)
        MiddleFrame.pack(side=BOTTOM)
        
        DataFrame =LabelFrame(MainFrame, bd =10,padx=35,pady=5, width =1355,height= 400,bg='light blue', relief = RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        
        UpperFrameLeft =Frame(DataFrame, bd =10,padx=20, width =700,height= 220,relief = RIDGE)
        UpperFrameLeft.pack(side=LEFT)
        
        UpperFrameRight =Frame(DataFrame, bd =10,pady=4,padx=20, width =570,height= 220,bg='light blue', relief = RIDGE)
        UpperFrameRight.pack(side=RIGHT)
        
        LowerFrameRight =LabelFrame(MiddleFrame, bd =10,pady=4,padx=20, width =720,height= 220,bg='light blue', relief = RIDGE,
                                   font=('arial', 20, 'bold'))
        LowerFrameRight.pack(side=LEFT)
        
        LowerFrameleft =LabelFrame(MiddleFrame, bd =10,padx=20, width =550,height= 220, relief = RIDGE,
                                  font=('arial', 20, 'bold'))
        LowerFrameleft.pack(side=RIGHT)
        
        
        
        
        
        #===================================Variables============================
        TaxPeriod = StringVar()
        TaxCode = StringVar()
        Payment = StringVar()
        PayDate = StringVar()
        EmpRef = StringVar()
        MonTaxableWages = StringVar()
        TaxableWages = StringVar()
        TaxPaid = StringVar()
        PayBeforeTax = StringVar()
        NetPay = StringVar()
        GrossPay = StringVar()
        Deduction = StringVar()
        NINumber = StringVar()
        NICode = StringVar()
        Employer = StringVar()
        Employee = StringVar()
        JobTitle = StringVar()
        PayBeforeTax.set(1200)
        
        #===================================functions============================
        
        #===================================Widget============================
        self.lblTaxPeriod = Label(UpperFrameRight,font=('arial',18,'bold'), text='Tax Period',
                             fg='white',bg='light blue')
        self.lblTaxPeriod.grid(row=0,column=0,sticky=W)
        
        self.cboTaxPeriod =ttk.Combobox(UpperFrameRight,textvariable=TaxCode, state= 'readonly',font=('arial',22,'bold'),width=24)
        self.cboTaxPeriod['value']=('Select Tax Period','Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec')
        self.cboTaxPeriod.current(0)
        self.cboTaxPeriod.grid(row=0,column=1,pady=2)
        
        self.cboTaxCode =ttk.Combobox(UpperFrameRight,textvariable=TaxPeriod, state= 'readonly',font=('arial',22,'bold'),width=24)
        self.cboTaxCode['value']=('Select Tax Code','BY12100','BY12200','BY12300','BY12400','BY12500')
        self.cboTaxCode.current(0)
        self.cboTaxCode.grid(row=1,column=1,pady=2)
        
        self.lblPayDueDay = Label(UpperFrameRight,font=('arial',18,'bold'), text='NI Number',padx=1,pady=2,
                             fg='white',bg='light blue')
        self.lblPayDueDay.grid(row=2,column=0,sticky=W)
        
        
        self.txtNINumber = Entry(UpperFrameRight, width = 21,textvariable=NINumber, font=('arial',26,'bold'))
        self.txtNINumber.grid(row=2,column=1,pady=2)
        
        self.lblPayDueDay = Label(UpperFrameRight,font=('arial',18,'bold'), text='NI Code',padx=1,pady=2,
                             fg='white',bg='light blue')
        self.lblPayDueDay.grid(row=3,column=0,sticky=W)
        
        self.txtNICode = Entry(UpperFrameRight, width = 21,textvariable=NICode, font=('arial',26,'bold'))
        self.txtNICode.grid(row=3,column=1,pady=2)
        
        
       
        
        #===================================buttons============================


if __name__ == '__main__':
    root = Tk()
    application = Income_Tax(root)
    root.mainloop()
