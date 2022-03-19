#IMPORTING MODULES
from distutils.command.config import config
from tkinter import *
from tkinter import ttk
import sqlite3
#ROOT WINDOW
root=Tk()
root.title("Student Db")
root.geometry("948x722")
conn=sqlite3.connect('school.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS SCHOOL2(
	first_name text,
	last_name text,
 	class integer,
	section text,
	Date_of_birth date,
	Age integer,
	Gender text,
	Address text,
	Phone_number integer
	)""")
conn.commit()
#UPDATE FUNCTION TO UPDATE STUDENT DETAILS
def Update():
	conn=sqlite3.connect('school.db')
	c=conn.cursor()
	record_id=delete_box.get()
	c.execute("""UPDATE school2 SET
		first_name=:first,
		last_name=:last,
		class=:class,
		section=:section,
		Date_of_birth=:Date_of_birth,
		Age=:Age,
		Gender=:Gender,
		Address=:Adress,
		Phone_number=:Phone_number
			WHERE oid= :oid""",
			{
			 'first':f_name_update.get(),
			 'last':l_name_update.get(),
			 'class':clas_update.get(),
			 'section':section_update.get(),
			 'Date_of_birth':dob_update.get(),
			 'Age':age_update.get(),
			 'Gender':gender_update.get(),
			 'Adress':address_update.get(),
			 'Phone_number':phone_update.get(),
			 'oid':record_id
			 })
	conn.commit()
	conn.close()
	Edit.destroy()
#EDIT FUNCTION TO EDIT STUDENT DETAILS
def Edit():
	conn=sqlite3.connect('school.db')
	c=conn.cursor()
	record_id=delete_box.get()
	c.execute("SELECT * FROM SCHOOL2 WHERE oid= " + record_id)
	records=c.fetchall()
	global Edit
	Edit=Tk()
	Edit.title("Edit Details")
	Edit.geometry("450x250")
	global f_name_update
	global l_name_update
	global clas_update
	global section_update
	global age_update
	global gender_update
	global address_update
	global phone_update
	global dob_update
	f_name_update=Entry(Edit,width=30)
	f_name_update.grid(row=3,column=1)
	l_name_update=Entry(Edit,width=30)
	l_name_update.grid(row=4,column=1)
	clas_update=Entry(Edit,width=30)
	clas_update.grid(row=5,column=1)
	section_update=Entry(Edit,width=30)
	section_update.grid(row=6,column=1)
	dob_update=Entry(Edit,width=30)
	dob_update.grid(row=7,column=1)
	age_update=Entry(Edit,width=30)
	age_update.grid(row=8,column=1)
	gender_update=Entry(Edit,width=30)
	gender_update.grid(row=9,column=1)
	address_update=Entry(Edit,width=30)
	address_update.grid(row=10,column=1)
	phone_update=Entry(Edit,width=30)
	phone_update.grid(row=11,column=1)
	f_namelbl=Label(Edit,text="First Name")
	f_namelbl.grid(row=3,column=0)
	l_namelbl=Label(Edit,text="Last Name")
	l_namelbl.grid(row=4,column=0)
	classlbl=Label(Edit,text="Class")
	classlbl.grid(row=5,column=0)
	sectionlbl=Label(Edit,text="Roll Number")
	sectionlbl.grid(row=6,column=0)
	doblbl=Label(Edit,text="Date Of Birth")
	doblbl.grid(row=7,column=0)
	agelbl=Label(Edit,text="Age")
	agelbl.grid(row=8,column=0)
	genderlbl=Label(Edit,text="Gender")
	genderlbl.grid(row=9,column=0)
	adresslbl=Label(Edit,text="Address")
	adresslbl.grid(row=10,column=0)
	phonelbl=Label(Edit,text="Phone Number")
	phonelbl.grid(row=11,column=0)
	for record in records:
		f_name_update.insert(0,record[0])
		l_name_update.insert(0,record[1])
		clas_update.insert(0,record[2])
		section_update.insert(0,record[3])
		dob_update.insert(0,record[4])
		age_update.insert(0,record[5])
		gender_update.insert(0,record[6])
		address_update.insert(0,record[7])
		phone_update.insert(0,record[8])
	Save=Button(Edit,text="Save Changes",command=Update)
	Save.grid(row=13,column=0,columnspan=2, pady=10, padx=10, ipadx=137)
	conn.commit()
	conn.close()
#DELETE FUNCTION TO DELETE STUDENT DETAILS
def Delete():
	conn=sqlite3.connect('school.db')
	c=conn.cursor()
	c.execute("DELETE FROM SCHOOL2 WHERE oid = "+ delete_box.get())
	conn.commit()
	conn.close()
#SUBMIT FUNCTION TO SUBMIT STUDENT INFORMATION
def Submit():
	conn=sqlite3.connect('school.db')
	c=conn.cursor()
	c.execute("INSERT INTO SCHOOL2 VALUES	(:f_name,:l_name,:class,:section,:Date_of_birth,:Age,:Gender,:Address,:Phone_number)",
			{
			 'f_name':f_name.get(),
			 'l_name':l_name.get(),
			 'class':clas.get(),
			 'section':section.get(),
			 'Date_of_birth':dob.get(),
			 'Age':age.get(),
			 'Gender':gender.get(),
			 'Address':adress.get(),
			 'Phone_number':phone.get()
			 })
	conn.commit()
	conn.close()
	f_name.delete(0,END)
	l_name.delete(0,END)
	clas.delete(0,END)
	section.delete(0,END)
	gender.delete(0,END)
	age.delete(0,END)
	adress.delete(0,END)
	phone.delete(0,END)
	dob.delete(0,END)
#QUERY FUNCTION TO DISPLAY STUDENT DETAILS
def Query():
	conn=sqlite3.connect('school.db')
	c=conn.cursor()
	c.execute("SELECT *, oid FROM SCHOOL2")
	records=c.fetchall()
	tree = ttk.Treeview(Frame4, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10"), 	show='headings',selectmode="browse")
	style=ttk.Style()
	style.theme_use("clam")
	style.configure("Treeview",fieldbackground="black",rowheight=20)
	verscrlbar = ttk.Scrollbar(Frame4,
                           orient ="vertical",
                           command = tree.yview)
	verscrlbar.grid(row=3,column=2)
	tree.configure(yscrollcommand = verscrlbar.set)
	for row in records:
		print(row)
		tree.insert("",END, values=row)     
	tree.column("#1", anchor=CENTER,width=90)	
	tree.heading("#1", text="First_Name")
	tree.column("#2", anchor=CENTER,width=90)
	tree.heading("#2", text="Last_Name")
	tree.column("#3", anchor=CENTER,width=40)
	tree.heading("#3", text="Class")
	tree.column("#4", anchor=CENTER,width=48)
	tree.heading("#4",text="Section")
	tree.column("#5",anchor=CENTER,width=90)
	tree.heading("#5",text="Date_of_birth")
	tree.column("#6",anchor=CENTER,width=30)
	tree.heading("#6",text="Age")
	tree.column("#7",anchor=CENTER,width=50)
	tree.heading("#7",text="Gender")
	tree.column("#8",anchor=CENTER,width=300)
	tree.heading("#8",text="Address")
	tree.column("#9",anchor=CENTER,width=90)
	tree.heading("#9",text="Phone_number")
	tree.column("#10",anchor=CENTER,width=90)
	tree.heading("#10",text="Unique_ID")
	tree.grid(row=3,column=0)
	conn.commit()
	conn.close()
#FRONTEND OF THE APP USING TKINTER
Frame1=Frame(root,relief="solid",borderwidth=4,bg="black")
Frame1.grid(row=0,column=0)
Label2=Label(Frame1,text="Student Database Management",font=("Arial Black",30),bg="black",fg="white")
Label2.grid(row=0,column=0)
Frame2=Frame(Frame1,relief="solid",borderwidth=2,bg="black")
Frame2.grid(row=1,column=0)
Frame3=Frame(Frame1,relief="solid",borderwidth=2,bg="black")
Frame3.grid(row=2,column=0)
Frame4=Frame(Frame1,relief="solid",borderwidth=2,bg="black")
Frame4.grid(row=3,column=0)
f_name=Entry(Frame2,width=30)
f_name.grid(row=4,column=1)
l_name=Entry(Frame2,width=30)
l_name.grid(row=5,column=1)
clas=Entry(Frame2,width=30)
clas.grid(row=6,column=1)
section=Entry(Frame2,width=30)
section.grid(row=7,column=1)
dob=Entry(Frame2,width=30)
dob.grid(row=8,column=1)
age=Entry(Frame2,width=30)
age.grid(row=9,column=1)
gender=Entry(Frame2,width=30)
gender.grid(row=10,column=1)
adress=Entry(Frame2,width=30)
adress.grid(row=11,column=1)
phone=Entry(Frame2,width=30)
phone.grid(row=12,column=1)
delete_box=Entry(Frame3,width=30)
delete_box.grid(row=17,column=1)
f_namelbl=Label(Frame2,text="First Name",bg="black",fg="white",font=("Courier",10))
f_namelbl.grid(row=4,column=0)
l_namelbl=Label(Frame2,text="Last Name",bg="black",fg="white",font=("Courier",10))
l_namelbl.grid(row=5,column=0)
classlbl=Label(Frame2,text="Class",bg="black",fg="white",font=("Courier",10))
classlbl.grid(row=6,column=0)
sectionlbl=Label(Frame2,text="Section",bg="black",fg="white",font=("Courier",10))
sectionlbl.grid(row=7,column=0)
doblbl=Label(Frame2,text="Date Of Birth",bg="black",fg="white",font=("Courier",10))
doblbl.grid(row=8,column=0)
agelbl=Label(Frame2,text="Age",bg="black",fg="white",font=("Courier",10))
agelbl.grid(row=9,column=0)
genderlbl=Label(Frame2,text="Gender",bg="black",fg="white",font=("Courier",10))
genderlbl.grid(row=10,column=0)
adresslbl=Label(Frame2,text="Address",bg="black",fg="white",font=("Courier",10))
adresslbl.grid(row=11,column=0)
phonelbl=Label(Frame2,text="Phone Number",bg="black",fg="white",font=("Courier",10))
phonelbl.grid(row=12,column=0)
delete_box_lbl=Label(Frame3,text="Type Uid (Edit/Delete)",bg="black",fg="white",font=("Courier",10))
delete_box_lbl.grid(row=17,column=0)
Submit=Button(Frame2,text="Add To Database",command=Submit,relief="solid",font=("Courier",10))
Submit.grid(row=14,column=0,columnspan=2, pady=10, padx=10, ipadx=130)
query=Button(Frame4,text="Show Records",command=Query,relief="solid",font=("Courier",10))
query.grid(row=9,column=0,columnspan=2, pady=10, padx=10, ipadx=137)
delete=Button(Frame3,text="Delete Record",command=Delete,relief="solid",font=("Courier",10))
delete.grid(row=19,column=0,columnspan=2, pady=10, padx=10, ipadx=137)
edit=Button(Frame3,text="Edit Record",command=Edit,relief="solid",font=("Courier",10))
edit.grid(row=20,column=0,columnspan=2, pady=10, padx=10, ipadx=145)
conn.commit()
conn.close()
root.mainloop()
#END OF PROGRAM........................................................