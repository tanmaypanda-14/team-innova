from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from libs.screens.homepage import HomePage
from kivy.uix.screenmanager import ScreenManager

class Home(Screen):
	pass

class Crypto(Screen):
	pass

class WindowManager(ScreenManager):
	pass



class Crpytop(MDApp):
	def build(self):
		Window.size = [300, 600]
		self.load_all_kv_files()
		return HomePage()

	def load_all_kv_files(self):
		Builder.load_file('libs/screens/homepage.kv')
		Builder.load_file('libs/components/appbar.kv')


if __name__ == "__main__":
	Crpytop().run()