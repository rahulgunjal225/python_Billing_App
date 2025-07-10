

from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Bill Application")
        bg_color = "#074463"
        title=Label(self.root,text="Bill Application",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #==============variables============
        #==============cosmetic============
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        
        #=======grocery======
        
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #==========cold drinks==========

        self.maza=IntVar()
        self.cock=IntVar()
        self.Thumbsup=IntVar()
        self.pepsi=IntVar()
        self.sprite=IntVar()
        self.RedBUll=IntVar()
        
        #=========Total product price & tax variables

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        

        #===========customer==========
        
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()
        
        
        
        
        
        
        #============customer datails frame
        f1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)
        
        cname_lb1=Label(f1,text="customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(f1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5)

        cphn_lb1=Label(f1,text=" Phone No",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_text=Entry(f1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5)

        c_bill_lb1=Label(f1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text=Entry(f1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5)

        bill_btn=Button(f1,text="search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
        
        

        #==================cosmatic,frame=============
        
        f2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmatic",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f2.place(x=5,y=180,width=325,height=380)

        bath_lb1=Label(f2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(f2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
      
        face_cream_lb1=Label(f2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(f2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lb1=Label(f2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(f2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lb1=Label(f2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(f2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lb1=Label(f2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(f2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lb1=Label(f2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(f2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



       #==================Grocery,frame=============
        
        f3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f3.place(x=340,y=180,width=325,height=380)

        g1_lb1=Label(f3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(f3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
      
        g6_cream_lb1=Label(f3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g6_cream_txt=Entry(f3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g2_w_lb1=Label(f3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g2_w_txt=Entry(f3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g3_s_lb1=Label(f3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g3_s_txt=Entry(f3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g4_g_lb1=Label(f3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g4_g_txt=Entry(f3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g5_lb1=Label(f3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(f3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #==================Cold Drink frame=============
        
        f4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f4.place(x=670,y=180,width=325,height=380)

        c1_lb1=Label(f4,text="Mazza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(f4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
      
        c6_cream_lb1=Label(f4,text="Cock",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c6_cream_txt=Entry(f4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c2_w_lb1=Label(f4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c2_w_txt=Entry(f4,width=10,textvariable=self.Thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c3_s_lb1=Label(f4,text="Pepsi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c3_s_txt=Entry(f4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c4_g_lb1=Label(f4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c4_g_txt=Entry(f4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c5_lb1=Label(f4,text="Red BUll",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(f4,width=10,textvariable=self.RedBUll,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



        #================Bill Area========================

        f5=Frame(self.root,bd=10,relief=GROOVE,)
        f5.place(x=1010,y=180,width=340,height=380)
        bill_title=Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scro_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scro_y.set)
        scro_y.pack(side=RIGHT,fill=Y)
        scro_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #=============Button Frame====================
        
        f6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Meanu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f6.place(x=0,y=560,relwidth=1,height=140)
        m1=Label(f6,text="Total cosmatic price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=0,sticky="w")
        m1_txt=Entry(f6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(f6,text="Total Grocery price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=0,sticky="w")
        m2_txt=Entry(f6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(f6,text="Total Cold Drinks price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=0,sticky="w")
        m3_txt=Entry(f6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1=Label(f6,text="Cosmatic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=0,sticky="w")
        c1_txt=Entry(f6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2=Label(f6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=0,sticky="w")
        c2_txt=Entry(f6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(f6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=0,sticky="w")
        c3_txt=Entry(f6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_f=Frame(f6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)

        Total_btn=Button(btn_f,command=self.total,text="total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)  
        GBil_btn=Button(btn_f,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=3,padx=5,pady=5)   
        self.welcome_bill()


    def total(self):

        self.c_S_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshan.get()*180

        self.total_cosmetic_price = float(
                                     self.c_S_p+
                                     self.c_fc_p+
                                     self.c_fw_p+
                                     self.c_hs_p+
                                     self.c_hg_p+
                                     self.c_bl_p
                                     ) 
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))
                
        
        self.g_r_p=self.rice.get()*40
        self.g_f_p=self.food_oil.get()*120
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*180
        self.g_s_p=self.sugar.get()*140
        self.g_t_p=self.tea.get()*180
    
            
        self.total_grocery_price = float(
                                   self.g_r_p +
                                   self.g_f_p+
                                   self.g_d_p +
                                   self.g_w_p +
                                   self.g_s_p+
                                   self.g_t_p
                                   )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))


       
        self.d_m_p=self.maza.get()*40
        self.d_s_p=self.sprite.get()*40
        self.d_c_p=self.cock.get()*60
        self.d_t_p=self.Thumbsup.get()*50
        self.d_p_p=self.pepsi.get()*80
        self.d_r_p=self.RedBUll.get()*150
       
    
        self.total_cold_drink_price = float(
                                      self.d_m_p+
                                      self.d_s_p+
                                      self.d_c_p+
                                      self.d_t_p+
                                      self.d_p_p+
                                      self.d_r_p
                                     )
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.c_tax=round((self.total_cold_drink_price * 0.05), 2)
        self.cold_drink_tax.set("Rs. " + str(self.c_tax))
        
        self.total_bill=float(   self.total_cosmetic_price+
                                 self.total_grocery_price+
                                 self.total_cold_drink_price+
                                 self.c_tax+
                                 self.g_tax+
                                 self.c_tax
                               ) 








    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\tWelcome Webcode Reatail\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n=====================================")
        self.txtarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n=====================================")


    def bill_area(self):
       if self.c_name.get()==""or self.c_phone.get()=="":
        messagebox.showerror("Error","customer details are must")
       elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
        messagebox.showerror("Error","No Product Puchased")    
           
           
       else:
            self.welcome_bill()
        #==========cosmatic=========
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_S_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")


            #==========grocery=========
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")


            #==========drinks=========
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Mazza\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
            if self.cock.get()!=0:
                self.txtarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.d_c_p}")
            if self.Thumbsup.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.Thumbsup.get()}\t\t{self.d_t_p}")
            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.d_p_p}")
            if self.RedBUll.get()!=0:
                self.txtarea.insert(END,f"\n Redd Bull\t\t{self.RedBUll.get()}\t\t{self.d_r_p}")


            self.txtarea.insert(END,f"\n-------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n cosmatic tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n grocery tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drink tax\t\t\t{self.cold_drink_tax.get()}")
        
            self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {self.total_bill}")
        

            self.txtarea.insert(END,f"\n-------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("save Bill","Do you want to save the bill?")
        if op>0:       
           self.bill_data=self.txtarea.get("1.0",END)
           f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
           f1.write(self.bill_data)
           f1.close()
           messagebox.showwarning("saved",f"Bill no :{self.bill_no.get()}saved successfully")
        else:
            return
           
    def find_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills/{i}","r")
                for d in f1:
                   self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bil No.")

    def clear_data(self):
       op=messagebox.askyesno("clear","Do you really want to clear?")
       if op>0:
            self.root.destroy()
       
       
            #==============cosmetic============
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            
            #=======grocery======
            
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #==========cold drinks==========

            self.maza.set(0)
            self.cock.set(0)
            self.Thumbsup.set(0)
            self.pepsi.set(0)
            self.sprite.set(0)
            self.RedBUll.set(0)
            
            #=========Total product price & tax variables

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            

            #===========customer==========
            
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()




                    # Create a label to display in the window          
        self.label = Label(self.root, text="Welcome to the Bill App!")
        self.label.pack()

             # Initialize the Tkinter root window
root = Tk()

         # Create an instance of the Bill_app class
obj = Bill_app(root)

  # Start the Tkinter main loop to show the window
root.mainloop()

    