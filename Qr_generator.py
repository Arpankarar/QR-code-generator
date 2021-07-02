from tkinter import*
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR-Generator | by Arpan Karar")
        self.root.resizable(False,False)
        
        title=Label(self.root,text= "   Qr Code Generator" , font =("times roman",50),bg="#BEAEE2",fg="#053742",anchor="w").place(x=0,y=0,relwidth=1)
        #============= employee details window ==========
        emp_Frame = Frame(self.root,bd=2,relief=RIDGE)
        emp_Frame.place(x=50,y=100,width=500,height=380)
root=Tk()
obj =Qr_Generator(root)
root.mainloop()