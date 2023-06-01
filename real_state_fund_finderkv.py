from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from bs4 import BeautifulSoup
import requests
import sys

class MainApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.result = Label(text='Coloque o fundo imobiliario')
        self.layout.add_widget(self.result)

        self.input1 = TextInput(text='', multiline=False)
        self.layout.add_widget(self.input1)


        self.button = Button(text='Buscar')
        self.button.bind(on_press=self.add)
        self.layout.add_widget(self.button)

        return self.layout

    def add(self, instance):
        try:
            result = str(self.input1.text)
            # solicitando a versão do navegador
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}


            link = f"https://statusinvest.com.br/fundos-imobiliarios/{result}"

            req = requests.get(link, headers=headers)

            # precesso de requisição
            # print(req.text)
            site = BeautifulSoup(req.text, "html.parser")
            # leitor html
            # print(site.prettify())
            # organizando a pagina
            valorc = site.find("strong", class_="value")
            valora= (valorc.get_text())
            # procurando o valor
            self.result.text = str(valora)
            # escrevendo o valor da cota

        except ValueError:
            self.result.text = 'fundo invalido '

MainApp().run()
