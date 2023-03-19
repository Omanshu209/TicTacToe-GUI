from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.popup import Popup

KV = ("""
<URLPopup>:
    size_hint: .5,.5
    title: 'Result'
    auto_dismiss: False
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
       
        MDLabel:
            id:result
            text:''
            bold:True
            font_size: self.height/2
            halign:'center'
        
        MDBoxLayout:
            padding: 0
            spacing:10
            
            MDRectangleFlatButton:
                text: 'OK'
                pos_hint:{'center_x':.5}
                on_release: root.dismiss()
                
MDScreen:
	
	MDRectangleFlatButton:
		text:'T   I   C          T   A   C          T   O   E' 
		pos_hint:{'center_x':.5,'center_y':0.945}
		size_hint:.8,.05
		bold:True
	
	MDCard:
		size_hint:.95,.8
		pos_hint:{'center_x':.5,'center_y':.5}
		elevation:7
		padding:25
		spacing:25
		orientation:'vertical' 
		
		MDGridLayout:
			columns:3
			rows:3
			
			MDRectangleFlatButton:
				id:b1
				size_hint:.3,.25
				bold:True
				font_size: self.height/2
				on_press:
					app.displayXO(1)
				on_release:
					app.checkResult()
				
			MDRectangleFlatButton:
				id:b2
				size_hint:.3,.25
				bold:True
				font_size: self.height/2
				on_press:
					app.displayXO(2)
				on_release:
					app.checkResult()
			
			MDRectangleFlatButton:
				id:b3
				size_hint:.3,.25
				bold:True
				font_size: self.height/2
				on_press:
					app.displayXO(3)
				on_release:
					app.checkResult()
			
			MDRectangleFlatButton:
				id:b4
				size_hint:.3,.25
				bold:True
				font_size: self.height/2
				on_press:
					app.displayXO(4)
				on_release:
					app.checkResult()
		
			MDRectangleFlatButton:
				id:b5
				size_hint:.3,.25
				bold:True
				font_size: self.height/2
				on_press:
					app.displayXO(5)
				on_release:
					app.checkResult()
			
			MDRectangleFlatButton:
				id:b6
				size_hint:.3,.25
				bold:True
				font_size: self.height/2
				on_press:
					app.displayXO(6)
				on_release:
					app.checkResult()
			
			MDRectangleFlatButton:
				id:b7
				size_hint:.3,.25
				bold:True
				font_size: self.height/2
				on_press:
					app.displayXO(7)
				on_release:
					app.checkResult()
			
			MDRectangleFlatButton:
				id:b8
				size_hint:.3,.25
				bold:True
				font_size: self.height/2
				on_press:
					app.displayXO(8)
				on_release:
					app.checkResult()
				
			MDRectangleFlatButton:
				id:b9
				size_hint:.3,.25
				bold:True
				font_size: self.height/2
				on_press:
					app.displayXO(9)
				on_release:
					app.checkResult()
		
	MDRectangleFlatButton:
		text:'D   e   v   e   l   o   p   e   d       B   y       O   m   a   n   s   h   u' 
		pos_hint:{'center_x':.5,'center_y':0.045}
		size_hint:.8,.05
		font_size: self.height/2
		bold:True
""")

Turn = 'X'
nextP = False

class URLPopup(Popup):
    pass

class MainApp(MDApp):
	
	def build(self):
		self.theme_cls.theme_style = 'Dark' 
		self.theme_cls.primary_palette = 'DeepOrange'
		return Builder.load_string(KV)
		
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
				popup = URLPopup()
				popup.ids.result.text = f'{self.root.ids[f"b{winCases[i][0]}"].text} wins !'
				popup.open()
				self.clearWindow()
			elif self.root.ids.b1.text in ['X','O'] and self.root.ids.b2.text in ['X','O'] and self.root.ids.b3.text in ['X','O'] and self.root.ids.b4.text in ['X','O'] and self.root.ids.b5.text in ['X','O'] and self.root.ids.b6.text in ['X','O'] and self.root.ids.b7.text in ['X','O'] and self.root.ids.b8.text in ['X','O'] and self.root.ids.b9.text in ['X','O']:
				popup = URLPopup()
				popup.ids.result.text = f"Draw !"
				popup.open()
				self.clearWindow()
			
	def clearWindow(self):
		self.root.ids.b1.text=""
		self.root.ids.b2.text=""
		self.root.ids.b3.text=""
		self.root.ids.b4.text=""
		self.root.ids.b5.text=""
		self.root.ids.b6.text=""
		self.root.ids.b7.text=""
		self.root.ids.b8.text=""
		self.root.ids.b9.text=""
		
if __name__ == '__main__':
	MainApp().run()