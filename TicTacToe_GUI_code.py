from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.popup import Popup

Turn = 'X'
nextP = False

class ResultPopup(Popup):
    pass

class MainApp(MDApp):
	
	def build(self):
		self.theme_cls.theme_style = 'Dark' 
		self.theme_cls.primary_palette = 'DeepOrange'
		return Builder.load_file("Design.kv")
		
	def displayXO(self,b):
		global Turn,nextP
		
		if self.root.ids[f"b{b}"].text not in ['X','O']:
			self.root.ids[f"b{b}"].text = Turn
			nextP = True
			
		else:
			nextP = False
			
		if Turn == 'X' and nextP == True:
			Turn = 'O'
			
		elif Turn == 'O' and nextP == True:
			Turn = 'X'
			
	def checkResult(self):
		winCases = [[1,2,3],[1,7,4],[4,6,5],[7,8,9],[2,5,8],[3,9,6],[1,5,9],[3,5,7]]
		
		for i in range(8):
			
			if self.root.ids[f"b{winCases[i][0]}"].text == self.root.ids[f"b{winCases[i][1]}"].text and self.root.ids[f"b{winCases[i][0]}"].text == self.root.ids[f"b{winCases[i][2]}"].text and self.root.ids[f"b{winCases[i][1]}"].text == self.root.ids[f"b{winCases[i][2]}"].text and self.root.ids[f"b{winCases[i][0]}"].text in ['X','O'] and self.root.ids[f"b{winCases[i][1]}"].text in ['X','O'] and self.root.ids[f"b{winCases[i][2]}"].text in ['X','O']:
				popup = ResultPopup()
				popup.ids.result.text = f'{self.root.ids[f"b{winCases[i][0]}"].text} wins !'
				popup.open()
				self.clearWindow()
				
			elif self.root.ids.b1.text in ['X','O'] and self.root.ids.b2.text in ['X','O'] and self.root.ids.b3.text in ['X','O'] and self.root.ids.b4.text in ['X','O'] and self.root.ids.b5.text in ['X','O'] and self.root.ids.b6.text in ['X','O'] and self.root.ids.b7.text in ['X','O'] and self.root.ids.b8.text in ['X','O'] and self.root.ids.b9.text in ['X','O']:
				popup = ResultPopup()
				popup.ids.result.text = "Draw !"
				popup.open()
				self.clearWindow()
			
	def clearWindow(self):
		for i in range(9):
			self.root.ids[f"b{i+1}"].text = ""
		
if __name__ == '__main__':
	MainApp().run()