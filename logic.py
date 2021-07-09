class calc:
	def replacing_values(self):
			self.expression = self.e.get()
			self.newtext=self.expression.replace('/','/')
			self.newtext=self.newtext.replace('x','*')		

	def equals(self):
			self.replacing_values()
			try:
				self.value= eval(self.newtext) 
			except SyntaxError:
				self.e.delete(0,END)
