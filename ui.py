from tkinter import *

root = Tk()
root.resizable(False, False)
root.configure(background="#00001a")

class calc:
	def clearall(self):
		self.e.delete(0,END)
		
	def clear1(self):
		self.txt=self.e.get()[:-1]
		self.e.delete(0,END)
		self.e.insert(0,self.txt)
		
	def action(self,argi):
		self.e.insert(END,argi)
		
	def __init__(self,master):
		master.title('Calculator')
		master.geometry()
		self.e = Entry(master, font=('arial', 12, 'bold'), justify='right')
		self.e.grid(row=0,column=0,columnspan=4,pady=4,ipadx= 25, ipady= 6)
		self.e.focus_set()


		Button(master,text="=",width=12,height=3, font=('arial', 12, 'bold'), fg="black",
				bg="#99c2ff",command=lambda:self.equals()).grid(
									row=5, column=2,columnspan=2)

		Button(master,text='AC',width=5,height=3, font=('arial', 12, 'bold'), 
						fg="black", bg="#99c2ff",
			command=lambda:self.clearall()).grid(row=4, column=1)

		Button(master,text='C',width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.clear1()).grid(row=4, column=2)

		Button(master,text="+",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action('+')).grid(row=4, column=3)

		Button(master,text="x",width=5,height=3, font=('arial', 12, 'bold'), 
					fg="black", bg="#99c2ff",
					command=lambda:self.action('x')).grid(row=2, column=3)

		Button(master,text="-",width=5,height=3, font=('arial', 12, 'bold'), 
					fg="black", bg="#99c2ff",
					command=lambda:self.action('-')).grid(row=3, column=3)

		Button(master,text="÷",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action('/')).grid(row=1, column=3)

		Button(master,text="7",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action('7')).grid(row=1, column=0)

		Button(master,text="8",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action(8)).grid(row=1, column=1)

		Button(master,text="9",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action(9)).grid(row=1, column=2)

		Button(master,text="4",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action(4)).grid(row=2, column=0)

		Button(master,text="5",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action(5)).grid(row=2, column=1)

		Button(master,text="6",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action(6)).grid(row=2, column=2)

		Button(master,text="1",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action(1)).grid(row=3, column=0)

		Button(master,text="2",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action(2)).grid(row=3, column=1)

		Button(master,text="3",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action(3)).grid(row=3, column=2)

		Button(master,text="0",width=5,height=3, font=('arial', 12, 'bold'), 
				fg="black", bg="#99c2ff",
				command=lambda:self.action(0)).grid(row=4, column=0)

		Button(master,text=".",width=12,height=3, font=('arial', 12, 'bold'), 
                   fg="black",bg="#99c2ff",
                   command=lambda:self.action('.')).grid(row=5, column=0, columnspan=2)

obj=calc(root) 

root.mainloop()
