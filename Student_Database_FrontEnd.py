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
		
		
if __name__=='__main__':
	root = Tk()
	application = Student(root)
	root.mainloop()