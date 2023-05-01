from bs4 import BeautifulSoup
import requests
import sys
def main():    
    
    #solicitando a versão do navegador
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    imobi = input ("Insira o fundo imobiliario")

    link=f"https://statusinvest.com.br/fundos-imobiliarios/{imobi}"
    
    req = requests.get(link, headers = headers)
    
    #precesso de requisição
    #print(req.text)
    site= BeautifulSoup(req.text, "html.parser")
    #leitor html
    #print(site.prettify())
    #organizando a pagina
    valorc = site.find("strong", class_ = "value" )
    #procurando o valor
    print(valorc.get_text())
    #escrevendo o valor da cota
if __name__== "__main__":
    main()
