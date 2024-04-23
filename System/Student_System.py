from msilib.schema import ComboBox
from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox
import pymysql
from time import *
import customtkinter as ctk
import customtkinter 
from tkinter import *

from tkinter import font
from PIL import ImageTk, Image 
import time

def START ():
    #importing library
        

        w=Tk()

        #Using piece of code from old splash screen
        width_of_window = 430
        height_of_window = 250
        screen_width = w.winfo_screenwidth()
        screen_height = w.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        #w.configure(bg='#ED1B76')
        w.overrideredirect(1) #for hiding titlebar

        #new window to open

        Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
        label1=Label(w, text='Mohammed Alaa', fg='white', bg='#272727') #decorate it 
        label1.configure(font=("Game Of Squids", 25, "bold"))   #You need to install this font in your PC or try another one
        label1.place(x=80,y=110)
        label1plus = Label(w, text='Student System', fg='white', bg='#272727')
        label1plus.configure(font=("Game Of Squids", 25, "bold"))
        label1plus.place(x=80,y=75)

        label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
        label2.configure(font=("Calibri", 11))
        label2.place(x=10,y=215)

        #making animation

        image_a=ImageTk.PhotoImage(Image.open('c2.png'))
        image_b=ImageTk.PhotoImage(Image.open('c1.png'))




        for i in range(5) :
            l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=155)
            l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=155)
            l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=155)
            l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=155)
            w.update_idletasks()
            time.sleep(0.5)

            l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=155)
            l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=155)
            l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=155)
            l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=155)
            w.update_idletasks()
            time.sleep(0.5)

            l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=155)
            l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=155)
            l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=155)
            l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=155)
            w.update_idletasks()
            time.sleep(0.5)

            l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=155)
            l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=155)
            l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=155)
            l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=155)
            w.update_idletasks()
            time.sleep(0.5)


        import os 
        os.system("cls")
        w.destroy()
        w.mainloop()
#=====================================قســــــم بـــــرمــــــجـــــه الــــــــــــــــــــدوال===============================================
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

START()
#---------------fun important-------------------

def img():
    messagebox.showwarning('مهــــــــم للغـــــايه','  عفوا عزيزي المستخدم\n\n\n عليك ادخال معلومات صحيحه ودقيقه لان زر التعديل \n\nوتحديث البيانات غير مفعل  \n\nحاليا برجاء التاكد من صحه المعلومات  \n\nقبل الاضافه الي الحقول  لان لا يمكن التعديل عليها في الوقت الحالي \n') 
    messagebox.showwarning('ازالــــه حـــقـــل',
        'لا يمكنك ازاله كل حقول الجدول بمعني انك يمكنك ازاله كل الحقول بحيث يكون هناك حقل واحد في الجدول علي الاقل الا في حاله اغلاق التطبيق و الفتح مره اخري\n\n  مطور التطبيق محمد علاء محمد')
         

#--------------------------fun window-------------------
def smol():
        t= messagebox.askokcancel('تصغــير النـــافذه',"هل تريــد تصغــير النـــافذه\n") #مع العلم لم يتم اغلاق التطبيق",)# askretrycancel لاعاده المحاوله
        t = t
        if t ==  True:
            #debag = messagebox.showwarning(' النـــافذه',' تمــــام ستبقي النـــافذه في الأسفل')
            root.iconify()
        # elif t == False:
        #     messagebox.showinfo('OK','تمام لم يتم تصغــير النـــافذه')
 
#-------------------داله زر الحفظ في فريم البحث-----------------
def save_program():
    
    t= messagebox.askyesnocancel('Save-Data To Exit',"اغلاق البرنامج مع حفظ البيانات و التعديلات ",)# askretrycancel لاعاده المحاوله
    if t ==  True:
        sleep(1)
        
        quit()
           

       
#--------------داله عن المطور--------------
def about():
    messagebox.showinfo('About Developer','محمد علاء مطور تطبيقات سطح المكتب يمتلك خبره كامله حول مجال البرمجه بلغات برمجيه متعدده ')
    messagebox.askokcancel("WhatsApp", "https://wa.me/966538886324")
    


#--------------------داله الخروج من البرنامج----------------------**
#------------كود ترحيب او كود معرفه ان البرنامج تم القفااقفاله--------------------**

def info():
    close = messagebox.askyesno('Close Program','Do You Exit Of Program...?')
    
    if close == True:
        quit()
    


#==========================
#--------------------داله شراء البرنامج----------------------



def do():
    fil = Toplevel(root)
    fil.geometry('800x500')
    fil.title('لــــوحــه تــحــكم المعلـــم {@User -Control Board}')
    root['background'] = '#95a5a6'
    fil.iconbitmap('ls.ico')
    bt = Button(fil,text='BY / MOHAMED ALAA',bg='black',fg='#FFF',width='50')
    bt.pack()
    bt1 = Button(fil,text='الاعدادات غير متاااحه ')
    bt1.pack()

def hello ():
    print('Ok Save Auto')

#===================================== انتهاء قســــــم بـــــرمــــــجـــــه الــــــــــــــــــــدوال ===============================================

class Student:
    #----------------انشاء نافذه البرنامج-------------------
    def __init__(self,root):
        self.root = root  
        # self.root.geometry('2000x1080')  # مقاسات شاشه البرنامج
        self.root.state("zoomed") #full screen
        self.root.title('لــــوحــه تــحــكم المعلـــم {@User -Control Board}') # عنوان البرنامج
        self.root['background'] = '#FFF' # خلفيه البرنامج
        self.root.iconbitmap('ls.ico') # ايقونه البرنامج
        # self.root.resizable(False,False) # التحكم في عرض و طول البرنامج
        title = Label(self.root,
                text='{نـــــظــــــام تســـــجـــــيل الــــطـــــلاب واداره الـــــمـــــدرســه} ',
                fg='#fff',
                bg='#000000',# green color 28e416 , f6358d
                font=('arial',13,'bold')) # master للتحكم في مكان الليبل    option للتحكم في الخصائص
        title.pack(fill=X) # املاء النص الي العرض كامل
        # button_support =Label(self.root,command=print(about())) # رساله  تشغيل   
        # button_support.pack()
        #---------القائمه العلويه----------
        # button_top_support = ttk.Button(self.root,text='الطرق الشائعه',command=file_dialog)
        # button_top_support.place(x=1,y=1)
        

       
       
       #-4444$$$$$$$$%$%$%$%$$$$$$$$$$$$$$$$$$$%$%$%$%_------------------#
        #------------------ادوات التحكم بالبرنامج-----------------
        Manage_Frame = Frame(self.root,bg='#b2bec3',border='0',width=210) # Frame
        Manage_Frame.place(x=1137,y=25,width=210,height=495)
     #------------انشاء متغيرات الحقول-----------
       # يتم انشاء عدد الحقول حسب الموجود في البرنامج
       #-------------------------#
    #----------------------------------
        root.minsize(1000,1000) # الحد الاصغر للبرنامج من حيث العرض و الطول
        root.maxsize(2900,2900) # الحد الاكبر للبرنامج من حيث العرض و الطول
    #---------------------------------- 
       #-------------------------#
      
        self.id=StringVar()#1
        self.name=StringVar()#2
        self.phone=StringVar()#3
        self.note=StringVar()#4
        self.add=StringVar()#5
        self.pest=StringVar()#6
        self.Level=StringVar()#7
        self.gender=StringVar()#8  
        self.dell=StringVar()#9  
        self.se_by=StringVar()#10  
        self.se_var=StringVar()#10  
     #------------انتهاء اانشاء متغيرات الحقول -----------

                
        #-------ادوات التحكم ----------------
        #-------ادوات التحكم ----------------
        
        txt = Label(Manage_Frame,text='لوحـة ادخال البيانات ',bg='#54a0ff',fg='#fff',font=('PT Bold Heading',10,'bold'),width='22',justify='center')
        txt.place(x=-50,y=-0)
        id = Label(Manage_Frame,text=' : الــرقم التسـلـسـلـي ',width='20',bg='#FC427B',fg='#fff',font=('arial',11,'bold'),justify='center')#bg='#FC427B'
        id.place(x=-20,y=32)
        
        add = ttk.Entry(Manage_Frame,width='22',justify='center',textvariable=self.id)
        add.place(x=3,y=58)
        
        #---------------------#
        
        label_2 = Label(Manage_Frame,text=' : اســـم الطــالــب ',width='20',bg='#FC427B',fg='#fff',font=('arial',11,'bold'),justify='center')#bg='#FC427B'
        label_2.place(x=-10,y=83)
        number_phone = ttk.Entry(Manage_Frame,width='22',justify='center',textvariable=self.name)
        number_phone.place(x=3,y=109)
        
        #---------------------#: اســـم الطــالــب 
        
        label_3 = Label(Manage_Frame,text=' : رقم الــهــاتــف ',width='20',bg='#FC427B',fg='#fff',font=('arial',11,'bold'),justify='center')#bg='#FC427B'
        label_3.place(x=-10,y=134)
        name = ttk.Entry(Manage_Frame,width='22',justify='center',show="●",textvariable=self.phone)
        name.place(x=3,y=161)
        
        #---------------------#
        
        label_4 = Label(Manage_Frame,text=' :  ملاحظات علي الطالب  ',width='20',bg='#FC427B',fg='#fff',font=('arial',11,'bold'),justify='center')#bg='#FC427B'
        label_4.place(x=-20,y=187)
        note = ttk.Entry(Manage_Frame,width='22',justify='right',textvariable=self.note)#,font=('Calibri (Body)',7,'bold')
        note.place(x=3,y=215)
        
        #---------------------#
        
        label_5 = Label(Manage_Frame,text=' : عــنـوان الطــالــب   ',width='20',bg='#FC427B',fg='#fff',font=('arial',11,'bold'),justify='center')#bg='#FC427B'
        label_5.place(x=-10,y=241)
        add = ttk.Entry(Manage_Frame,width='22',justify='center',textvariable=self.add)
        add.place(x=3,y=268)
        
         #---------------------#
         
       
        test = Label(Manage_Frame,text='مــستــوي الطـــالــب',width='20',bd='2',justify='center',bg='#FC427B',fg='#fff',font=('arial',11,'bold'))
        test.place(x=-20,y=294)
        combo_gender2 = ttk.Combobox(Manage_Frame,width='20',justify='center',state='readonly',textvariable=self.pest)
        combo_gender2 ['value'] = ('إمتياز','ممتاز','جيد جداً','جيد','ضغيف','راسب')
        combo_gender2.place(x=0,y=320)
        # #-----------------------------------------------
        #---------------------#
        Level = test = Label(Manage_Frame,text='حــاله الطـــالــب',width='20',bd='2',justify='center',bg='#FC427B',fg='#fff',font=('arial',11,'bold'))
        Level.place(x=-20,y=344)
        Level = ttk.Combobox(Manage_Frame,width='20',justify='center',state='readonly',textvariable=self.Level)
        Level ['value'] = ('حاضر',' غائب')
        Level.place(x=0,y=370)
       
        #---------------------#
        gender = Label(Manage_Frame,text="  : اختر - اكتب جنس الطالب",width='20',bg='#6c5ce7',fg='#fff',font=('arial',11,'bold'),justify='center')
        gender.place(x=-25,y=393)
        combo_gender = ttk.Combobox(Manage_Frame,width='20',justify='center',state='readonly',textvariable=self.gender)
        combo_gender ['value'] = ('ذكر','أنثي','أفضل عدم التحديد')
        combo_gender.place(x=0,y=420)
        #---------------------#
                
        lb_delet = Label(Manage_Frame,text=' ID - حذف طالب: الإسم [x]',justify='center',bg='#fff',fg='#ff3838',width='20',font=('arial',11,'bold'),bd=2)
        lb_delet.place(x=-23,y=443)
        delete = ttk.Entry(Manage_Frame,justify='center',textvariable=self.dell)
        delete.place(x=2,y=468,width=139,height=22)
        
        #---------------------------------الانتهاء من ادوات التحكم و الادخال=--------------------------#@#@#
        
        #------------------------بدايه عمل شريط بحث--------------------------
        
        share_Frame=Frame(self.root,bg='#FFF')# فريم البحث 
        share_Frame.place(x=-5,y=25,width='1135',height='44')
        lb_share=Label(share_Frame,text=' :  البحث عن طالب عن طريق',bg='#fff',fg='#4834d4',justify='center',font=('Deco',11,'bold'),bd=6)
        lb_share.place(x=977,y=8)
        combo_share = ttk.Combobox(share_Frame,justify='left',state='readonly',textvariable=self.se_by)
        combo_share['value']=('ID','Name','Phone','Level')
        combo_share.place(x=840,y=12,width='140')
        #-----------------------------------------------#
        share_entry = ttk.Entry(share_Frame,justify='center',textvariable=self.se_var)
        share_entry.place(x=660,y=13,width='170')
        se_btn = ctk.CTkButton(share_Frame,text='بــحــث',font=('Deco',15,'bold'),fg_color="#00000f",text_color="#fff",command=self.search,width=95,height=22)# زر البحث
        # se_btn = Button(share_Frame,text='بــحــث',bg='#0066ff',fg='#fff',justify='center',font=('Deco',12,'bold'),bd='5',command=self.search)# زر البحث
        se_btn.place(x=560,y=12) 
        by = Label (share_Frame,text='All rights are Saved / Mohamed Alaa',fg='#192a56',bd='1',bg='#fff',font=('Arial',10,'bold'))#Arial Rounded MT Bold
        by.place(x=316,y=13)
        
        copy = Label(share_Frame,text='©',bg='#fff',fg="#000000",font=('Arial',14,'bold'))
        copy.place(x=297,y=9)
        #---------------------------#
        # def hr():
        #     btn_save["state"] = "disabled"
        #     btn_save["text"] = "Saved"
        #     btn_save["bg"] = "#66ccff"
        #     btn_save["fg"] = "#000000"
        #---------------------------#
        def saved_programm():
            messagebox.showinfo("Saved","Data Auto Save.....")
        btn_save = ctk.CTkButton(share_Frame,text='حـفـظ',bg_color='#FFF',hover_color="#445080",fg_color='#212429',font=('',15,'bold'),
        width=85,height=23,command=saved_programm)#exchange تنشيط
        btn_save.place(x=8,y=11)
        
        ch_ty = ctk.CTkButton(share_Frame,text='تصغــير النـــافذه',command=smol,width=85,height=23,font=("",15,"bold"),bg_color='#FFF',hover_color="#445080",fg_color='#212429')
        ch_ty.place(x=97,y=11)
        #watch تحميل
        
        icon_img =ctk.CTkButton(share_Frame,text='قبل الاستخدام',command=img,width=85,height=23,font=("",15,"bold"),bg_color='#FFF',hover_color="#445080",fg_color='#212429')
        icon_img.place(x=196,y=11)
                   
        #---------------------انتهاء شريط البحث--------------------------#
        
        
        #-------------------------------DEDELIS--------------------------------#
        
        #----------الأزرار---------#
        dit_Frame = Frame(self.root,bg='#fff')
        dit_Frame.place(x=1,y=70,width=1134,height=665)
        btn_Frame = Frame(self.root,bg='#b2bec3',bd='2')
        btn_Frame.place(x=1137,y=523,width='220',height='700')
        # btn_Frame.pack(fill=X)
        title1=Label(btn_Frame,text='لـوحة تـحكم المــالـك',width='15',justify='center',font=('Deco',12,'bold'),bg='#000000',fg='#fff')
        title1.place(x=-1)
        lb_add = Button(btn_Frame,text='إضــافه طـالـب',
                        width='13',
                        font=('Deco',11,'bold'),
                        bg='#2C3A47',
                        fg='#fff',
                        justify='center',
                        cursor='',
                        bd=5,
                        command=self.add_student)
        lb_add.place(x=4,y=31,height=30)
        # انتهاء زر اضافه طالب 
        lb_delete = Button(btn_Frame,text='حذف طـالـب',
                           width='13',
                           font=('Deco',11,'bold'),
                           bg='#d63031',fg='#fff',
                           justify='center',
                           cursor='',bd=5,
                           command=self.delete)
        lb_delete.place(x=4,y=63,height=28)
        # انتهاء زر حذف طالب
        update = Button(btn_Frame,text='  تعديل وتحديث البيانات',
                        width='13',
                        font=('Deco',11,'bold'),
                        bg='#2C3A47',
                        fg='#fff',
                        justify='center',
                        cursor='',
                        bd=5,
                        command=self.update_data)
        update.place(x=4,y=94,height=28)
        # انتهاء زر تعديل وتحديث
        lb_remove = Button(btn_Frame,text='افراغ جميع الحـقول',
                           width='13',
                           font=('Deco',11,'bold'),
                           bg='#1592CC',
                           fg='#fff',
                           justify='center',
                           cursor='',
                           bd=5,
                           command=self.clear)
        lb_remove.place(x=4,y=124,height=28)
        # انتهاء زر افراع الحقول
        lb_about = Button(btn_Frame,text=' عـن المطــور',
                          width='13',
                          font=('Deco',11,'bold'),
                          bg='#2C3A47',fg='#fff',
                          justify='center',
                          cursor='',
                          bd=5 ,
                          command=about)
        lb_about.place(x=4,y=151,height=28)
        # انتهاء زر عن المطور
      
        lb_close = Button(btn_Frame,text='اغلاق البرنامج',
                          width='13',
                          bg='#d63031',
                          fg='#fff',
                          justify='center',
                          font=('Deco',11,'bold'),
                          cursor='',
                          bd=5,
                          command=info)
        lb_close.place(x=4,y=180,height=28)#ff3838 - d63031 اللون الاحمر ودرجاته
        #----------------------------انتهاء من الأزرار----------------

        #----treeview-----,
        #--------التحكم في السكرول
        scroll_x=ttk.Scrollbar(dit_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(dit_Frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(dit_Frame,
                columns=('add','gender','Level','phone','note','name','id','pest'),
                xscrollcommand=scroll_x.set,
                yscrollcommand=scroll_y.set)
        self.student_table.place(x=18,y=0,width=1116,height=650)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        
        
        scroll_x.config(command=self.student_table.xview)#
        scroll_y.config(command=self.student_table.yview)
        #-----------------------------التحكم في العناوين-------------------عناوين البيانات
        self.student_table['show']='headings'
        self.student_table.heading('gender',text='حاله الطـــالـب',anchor='center')
        
        self.student_table.heading('id',text='إسم الطالب',anchor='center')
        self.student_table.heading('Level',text='مستوي الطـــالـب',anchor='center')
        self.student_table.heading('add',text='جنس الطـــالـب',anchor='center')
        self.student_table.heading('phone',text=' عنوان الطـــالـب',anchor='center')
        self.student_table.heading('pest',text=' الرقم التسلسلي',anchor='center')
        self.student_table.heading('note',text='ملاحظات علي الطـالـب',anchor='center')
        self.student_table.heading('name',text='رقم هاتف الطـــالـب',anchor='center')

        #----------------التحكم في عررض و طول العناوين
        self.student_table.column('add',width=10)
        self.student_table.column('gender',width=10)
        self.student_table.column('Level',width=10)
        self.student_table.column('phone',width=10)
        self.student_table.column('note',width=130)
        self.student_table.column('name',width=10)
        self.student_table.column('id',width=50)
        self.student_table.column('pest',width=10)
        self.student_table.bind("<ButtonRelease-1>",self.get_cu) # عند التحديد او الوقوف تظهر البيانات في الخانات الخاصه بها حسب كل حقل
        
      #----------------------------------------------------
      #----------------------------------------------------
      #----------------------------------------------------
      #----------------------------------------------------
      #-------------------connect + add---------------------------------
        self.fetch_all()
        
    def add_student(self): # الاتصال بقواعد البيانات
        #   Dialog = messagebox.askokcancel('Add Student','اضف طالب')
          con=pymysql.connect( host  = 'localhost',user  = 'root',password  = '',database = 'tk1')
          cur = con.cursor()
          
          # داله التنفيذ
          cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                    self.gender.get(),
                                    self.Level.get(),
                                    self.pest.get(),
                                    self.add.get(),
                                    self.note.get(),
                                    self.phone.get(),
                                    self.name.get(),
                                    self.id.get(),
                                    
                                    
                                ))
          con.commit()   
          self.fetch_all() # لاظهار الطالب في البرناج فور اضافته للقاعده جلب البيانات
          self.clear() # امسح اليانات من الخانه بعد الاضافه
          con.close() # ايقاف السيرفر
       
    def fetch_all(self): #داله اظهار البيانات في البرنامج 
        con=pymysql.connect( host  = 'localhost', user  = 'root', password  = '', database = 'tk1')
        cur = con.cursor()  
        cur.execute('select * from student ')    
        rows = cur.fetchall() # يجمع جميع البيانات
        if len (rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,value=row) # جلب البيانات من الداتا الي لبرنامج
                con.commit()
        con.close()        
        #------------------------------------الانتهاء من زر الاضافه-------------------------------    
    def delete(self):
         con=pymysql.connect( host  = 'localhost',user  = 'root',password  = '',database = 'tk1')
         cur = con.cursor()  
         delete = messagebox.askokcancel('ازاله طالب','هل تريد ازاله طالب بالفعل مع العلم لم يتم ارجاع الطالب الا ان تقوم بإضافته',icon='error')
         if delete == True:
             cur.execute('delete from student where name=%s',self.dell.get()) # مسح طالب
             cur.execute('delete from student where id=%s',self.dell.get()) # مسح طال
             self.id.set('')
             self.phone.set('')
             self.name.set('')
             self.note.set('')
             self.add.set('')
             self.pest.set('')
             self.gender.set('')
             self.Level.set('')
             self.dell.set('')
             self.se_by.set('') ,self.se_var.set('')
            #  messagebox.showwarning('OK',' اضغط لتتم ازاله الطالب بنجاح')
         elif delete == False:
             print();
         #----------------------فتح التطبيق لاظهار رساله مهمه----------------------داله 
         
       
 
         con.commit()
         self.fetch_all()
         con.close()
     #-----------------الانتهاء من داله مسح طالب وبدايه داله افراغ الحقول    
#==========================================
    def clear(self):
         self.id.set('')
         self.phone.set('')
         self.name.set('')
         self.note.set('')
         self.add.set('')
         self.pest.set('')
         self.gender.set('')
         self.Level.set('')
         self.dell.set('')
         self.se_by.set('')
         self.se_var.set('')
         
#---------------------انتهاء داله افراغ الحقول-----------------

#----------------------------- زر تعديل البيانات داله الكوسور بمعني ان عند الوقوف علي اي حقل يظهر في الحقول المدخله سابقا-----------------------------

    def get_cu(self,ev):
        cursor_row =   self.student_table.focus() # عند النقر علي الجدول 
        contents = self.student_table.item(cursor_row) # متغير يحمل بيانات الجدول  وجلب العناصر
        row = contents['values'] # الحصول علي البيانات اي المتغيرات عند التحديد
        self.id.set(row[7]) # مهمه الروه جلب البيانات من المتغيرات 
        self.name.set(row[6])
        self.phone.set(row[5])
        self.note.set(row[4])
        self.add.set(row[3])
        self.pest.set(row[2])
        self.Level.set(row[1])
        self.gender.set(row[0])
        
#---------------------داله تعديل وتحديث البيانات-------------------------------
    def update_data(self):
        messagebox.showerror("System Error","نأسف الخاصيه غير متاحه الآن انتظر التحديث")
        con=pymysql.connect( host  = 'localhost',user  = 'root',password  = '',database = 'tk1')
        cur = con.cursor()
          # داله التنفيذ
        cur.execute("update student set gender=%s, Level=%s , pest=%s, add=%s, note=%s, phone=%s, name=%s,where id=%s",(
                                     
                                    self.gender.get(),
                                    self.Level.get(),
                                    self.pest.get(),
                                    self.add.get(),
                                    self.note.get(),
                                    self.phone.get(),
                                    self.name.get(),
                                    self.id.get()
                                    ))
        con.commit()   
        # self.fetch_all() # لاظهار الطالب في البرناج فور اضافته للقاعده جلب البيانات
        # self.clear() # امسح اليانات من الخانه بعد الاضافه
        con.close() # ايقاف السيرفر
        #---------انتهاء داله تعديل البيانات ولكن يوجد خطا------------------
       
       # -------------------داله البحث داخل الجدول---------------------------
    def search(self): #داله اظهار البيانات في البرنامج 
            con=pymysql.connect( host  = 'localhost', user  = 'root', password  = '', database = 'tk1')
            cur = con.cursor()  
            cur.execute('select * from student where ' +
            str(self.se_by.get())+" LIKE '%"+str(self.se_var.get()+"%'"))           
               
            rows = cur.fetchall() # يجمع جميع البيانات
            if len (rows) !=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("",END,value=row) # جلب البيانات من الداتا الي لبرنامج
                con.commit()
            con.close()        

#----------------------------------انتهاء برمجه جميع ادوات المشروع والان برمجه شريط تحميل للدخول للبرنامج-----------#



############################################################################################

os.system('cls') # مسح التيرمينال
root =Tk()
ob = Student(root) # تعريف كلاس البرنامج للتشغيل


        
    
# تحت التطوير لمزيد من الاصدارات
root.mainloop()

# name=txt.get('1.0','end') خاصيه ارجاع قيمه النص الي الليبيل
#     lb1['text']=name

# Write.Print ('Welcome To My Prograg',Colors.purple_to_red,interval=0.2)

# BY / MOHAMDED ALAA (name):
