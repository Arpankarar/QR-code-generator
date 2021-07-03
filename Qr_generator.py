from tkinter import*
import qrcode
from PIL import Image,ImageTk
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR-Generator | by Arpan Karar")
        self.root.resizable(False,False)
        
        title=Label(self.root,text= "   Qr Code Generator" , font =("times new roman",50),bg="#BEAEE2",fg="#053742",anchor="w").place(x=0,y=0,relwidth=1)
        #============= employee details window ==========
        
        
        #============== variables =====================
        
        self.var_emp_code = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()
        
        
        emp_Frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        emp_title=Label(emp_Frame,text= " Employee Details" , font =("goudy old style",30),fg="#053742").place(x=0,y=0,relwidth=1)
        
        lbl_emp_code=Label(emp_Frame,text= " Employee ID" , font =("goudy old style",15,'bold'),bg="white").place(x=20,y=60)
        lbl_name=Label(emp_Frame,text= " Name" , font =("goudy old style",15,'bold'),bg="white").place(x=20,y=100)
        lbl_department=Label(emp_Frame,text= " Department" , font =("goudy old style",15,'bold'),bg="white").place(x=20,y=140)
        lbl_designation=Label(emp_Frame,text= " Designation" , font =("goudy old style",15,'bold'),bg="white").place(x=20,y=180)
        
        txt_emp_code=Entry(emp_Frame, font =("goudy old style",15),textvariable=self.var_emp_code,bg="#EDF6E5").place(x=200,y=60)
        txt_name=Entry(emp_Frame, font =("goudy old style",15),textvariable=self.var_name,bg="#EDF6E5").place(x=200,y=100)
        txt_department=Entry(emp_Frame, font =("goudy old style",15),textvariable=self.var_department,bg="#EDF6E5").place(x=200,y=140)
        txt_designation=Entry(emp_Frame, font =("goudy old style",15),textvariable=self.var_designation,bg="#EDF6E5").place(x=200,y=180)
        
        
        btn_generator = Button(emp_Frame,text="QR Generator",command=self.generate,font=("times new roman",18,'bold'),bg="#0A1931",fg="white").place(x=80,y=250,width=200,height=40)
        btn_clear = Button(emp_Frame,text="Clear",command=self.clear,font=("times new roman",18,'bold'),bg="#4C4C6D",fg="white").place(x=290,y=250,width=150,height=40)
        
        self.msg=""
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",15),bg="white",fg="green")
        self.lbl_msg.place(x=0,y=300,relwidth=1)
        
        #    ==================Qr code frame=======================
        qr_Frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)
        qr_title=Label(qr_Frame,text= " Employee QR code" , font =("goudy old style",22),fg="#053742",anchor="w").place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text="QR code \nNot Available.",font=("times new roman",15),bg="#FFF5DA",fg="#053742",bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)
        
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
    
    def generate(self):
        if self.var_emp_code.get()=='' or self.var_name.get()==''or self.var_department.get()=='' or self.var_designation.get()=='' :
            self.msg='All Fields are required !!'
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qr_data =(f"Employee ID :{self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\nDesignation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            newsize=(180,180)
            qr_code=qr_code.resize(newsize)
            qr_code.save("Employee_QR/Emp_"+str(self.var_emp_code.get()+".png"))
            #============ qr code image update ===================
            self.im=ImageTk.PhotoImage(file="Employee_QR/Emp_"+str(self.var_emp_code.get()+".png"))
            self.qr_code.config(image=self.im)
            # ============ updating notification==================
            self.msg="QR Generated Successfully !!"
            self.lbl_msg.config(text=self.msg,fg="green")
    
        
root=Tk()
obj =Qr_Generator(root)
root.mainloop()