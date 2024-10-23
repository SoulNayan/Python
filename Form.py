from tkinter import*
from tkinter import ttk
a=Tk()
a.geometry("480x520")
a.maxsize(480,520)
a.minsize(480,520)
# a.configure(bg="lightblue")

Head=Label(text="Registrstion Form",font=('Times New Roman',25,'bold'))
Head.place(x=120,y=5)


FirstName=Label(text="First Name:-",font=('Times New Roman',17))
FirstName.place(x=20,y=70)
#"font=('Arial 16')" This is to increse the size of entry box
FN=a.Entry(width=15,font=('Arial 16'),placeholder="Type your message...")
FN.place(x=140,y=74)

LastName=Label(text="Last Name:-",font=('Times New Roman',17))
LastName.place(x=20,y=120)
#"font=('Arial 16')" This is to increse the size of entry box
LN=Entry(width=15,font=('Arial 16'))
LN.place(x=140,y=124)

Email=Label(text="Email:-",font=('Times New Roman',17))
Email.place(x=20,y=170)
EM=Entry(width=30,font=('Arial 16'))
EM.place(x=100,y=170)

MobileNO=Label(text="Mobile NO:-",font=('Times New Roman',17))
MobileNO.place(x=20,y=220)
MM=Entry(width=25,font=('Arial 16'))
MM.place(x=150,y=220)


Gender=Label(text="Gender:-",font=('Times New Roman',17))
Gender.place(x=20,y=270)
ge=ttk.Checkbutton(a)
ge.place(x=120,y=276)
ge2=ttk.Checkbutton()
ge2.place(x=200,y=276)
male=Label(text="Male",font=('Times New Roman',14))
male.place(x=136,y=274)
Female=Label(text="Female",font=('Times New Roman',14))
Female.place(x=220,y=274)


DOB=Label(text="Date Of Birth:-",font=('Times New Roman',17))
DOB.place(x=20,y=320)
combo_varDate = StringVar()
comboDate= ttk.Combobox(a, textvariable=combo_varDate,width=5,font=('Arial 12'))
comboDate['values'] = ['Date','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
comboDate.current(0)
comboDate.place(x=180,y=324)

combo_varMonth = StringVar()
comboMonth= ttk.Combobox(a, textvariable=combo_varMonth,width=5,font=('Arial 12'))
comboMonth['values'] = ['Month','1','2','3','4','5','6','7','8','9','10','11','12']
comboMonth.current(0)
comboMonth.place(x=250,y=324)

combo_varYear = StringVar()
comboYear= ttk.Combobox(a, textvariable=combo_varYear,width=5,font=('Arial 12'))
comboYear['values'] = ['Year','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
comboYear.current(0)
comboYear.place(x=320,y=324)

PASS=Label(text="Password:-",font=('Times New Roman',17))
PASS.place(x=20,y=370)
PASS1=Entry(width=20,font=('Arial 16'),show="*")
PASS1.place(x=130,y=373)

Submit=Button(text="Submit",font=('Times New Roman',17))
Submit.place(x=180,y=440)
a.mainloop()