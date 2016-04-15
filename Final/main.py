from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#Clase Principal Calculadora
class Calculadora(BoxLayout):
    def resultado(self, express):
        if not express: return

        try:
            #constructor de la pantalla donde saldran los numeros a calulcular
            self.pantalla.text = str(eval(express))
            #pequeña exepcion por si se da algun error con la pantalla por ejemplo         +-
        except Exception:
            self.pantalla.text = 'Error'

#aca solo es para  ponerle un icono y un nombre cuando se ejecuta el App
#se puede editar el titulo y las dimenciones del icono es de 512x512 pixeles puedes descargar unos de internet lo pegan en una carpeta junto al .Kv y .py
class CalculadoraApp(App):
    title = 'Calculadora Proyecto'
    icon = 'icono.png'

    def build(self):
        return Calculadora()

#se inicializa la aplicacion
if __name__ in '__main__':
    CalculadoraApp().run()
