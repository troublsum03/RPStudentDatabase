# Frontend

from tkinter import *
import tkinter.messagebox
#import stdDatabase


class Student:

	def __init__(self, root):
		self.root = root
		self.root.title("Students Database Management Systems")
		self.root.geometry("1350x750+0+0")
		self.root.config(bg="cadet blue")
		
		StdID = StringVar()
		Firstname = StringVar()
		Lastname = StringVar()
		DoB= StringVar()
		Age = StringVar()
		Gender = StringVar()
		Email = StringVar()
		Mobile = StringVar()

		#=====================================================Frames=====================================================
		MainFrame = Frame(self.root, bg="cadet blue")
		MainFrame.grid()

		TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief = RIDGE)
		TitFrame.pack(side=TOP)

		self.lblTit = Label(TitFrame ,font=('arial', 47, 'bold'),text="Student Database Management Systems",bg="Ghost White")
		self.lblTit.grid()

		ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief = RIDGE)
		ButtonFrame.pack(side=BOTTOM)

		DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief = RIDGE, bg="cadet blue")
		DataFrame.pack(side=BOTTOM)
		
		DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief = RIDGE, bg="Ghost White", font=('arial', 20, 'bold'), text="Student Info\n")
		DataFrameLeft.pack(side=LEFT)

		DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief = RIDGE, bg="Ghost White", font=('arial', 20, 'bold'), text="Student Details\n")
		DataFrameRight.pack(side=RIGHT)
		#=====================================================Labels and Entry Widget=====================================================
		self.lblStdID = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Student ID:", padx=2, pady=2, bg="Ghost White")
		self.lblStdID.grid(row=0, column=0, sticky=W)
		self.txtStdID = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
		self.txtStdID.grid(row=0, column=1)

		self.lblfna = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Firstname:", padx=2, pady=2, bg="Ghost White")
		self.lblfna.grid(row=1, column=0, sticky=W)
		self.txtfna = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
		self.txtfna.grid(row=1, column=1)

		self.lbllna = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Lastname:", padx=2, pady=2, bg="Ghost White")
		self.lbllna.grid(row=2, column=0, sticky=W)
		self.txtlna = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
		self.txtlna.grid(row=2, column=1)

		self.lblDoB = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Date of Birth:", padx=2, pady=3, bg="Ghost White")
		self.lblDoB.grid(row=3, column=0, sticky=W)
		self.txtDoB = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable = DoB, width=39)
		self.txtDoB.grid(row=3, column=1)

		self.lblAge = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Age:", padx=2, pady=3, bg="Ghost White")
		self.lblAge.grid(row=4, column=0, sticky=W)
		self.txtAge = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable = Age, width=39)
		self.txtAge.grid(row=4, column=1)

		self.lblGender = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=3, bg="Ghost White")
		self.lblGender.grid(row=5, column=0, sticky=W)
		self.txtGender = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable = Gender, width=39)
		self.txtGender.grid(row=5, column=1)

		self.lblEmail = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Email:", padx=2, pady=3, bg="Ghost White")
		self.lblEmail.grid(row=6, column=0, sticky=W)
		self.txtEmail = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable = Email, width=39)
		self.txtEmail.grid(row=6, column=1)

		self.lblMobile = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Mobile:", padx=2, pady=3, bg="Ghost White")
		self.lblMobile.grid(row=7, column=0, sticky=W)
		self.txtMobile = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable = Mobile, width=39)
		self.txtMobile.grid(row=7, column=1)
		#=====================================================ListBox & ScrollBar  Widget=====================================================
		scrollbar = ScrollBar(DataFrameRight)
		scrollbar.grid(row=0, column=1, sticky='ns')

		studentlist = Listbox(DataFrameRight, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
		studentlist.grid(row=0, column=0, padx=8)
		scrollbar.config(command = studentlist.yview)
		#=====================================================Button Widget=====================================================

		
if __name__=='__main__':
	root = Tk()
	application = Student(root)
	root.mainloop()