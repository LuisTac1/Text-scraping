import requests
from bs4 import BeautifulSoup

link = 'https://beautiful-soup-4.readthedocs.io/en/latest/#' #link do site a ser raspado
hearders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"} #requissição de usuario

requisition = requests.get(link, headers=hearders) # requisição do site e do navegador
print(requisition)
site = BeautifulSoup(requisition.text, "html.parser")


# "Description" Scraping texts
def first():
    print()
    page_title = site.find("title") #busca titulo h1
    print('***',page_title.get_text()[0:28].upper(),'***')

    print()
    tag_div = site.find("div", id="beautiful-soup-documentation")  # busca div da descrição breve
    tag_p = tag_div.find_all(["p"])[0:4] # funciona, pega a tag p até as linhas desejadas
    for i in tag_p:
        print(i.get_text(),"\n") # Funcionou pegou todas as tags p da div desejada

    return first


# "Help" Scraping texts
def tag_help():
    print()
    tag_div = site.find("div", id="getting-help") # find div from getting-help
    tag_h2 = tag_div.find(["h2"])

    print(tag_h2.get_text()[0:12])
    tag_p = tag_div.find_all(["p"])
    for i in tag_p:
        print(i.get_text(),"\n") 

    return tag_help


# "Quick Start" Scraping Text
def quick_start():
    print()
    tag_div = site.find(id="quick-start") # find div from quick-start
    tag_h2 = tag_div.find(["h1"])
    print(tag_h2.get_text()[0:11])

    tag_p = tag_div.find_all(["p"])[0:1]
    for i in tag_p:
        print(i.get_text())
    print()
    tag_div2 = tag_div.find_all("div", class_="highlight")[0:6] # Find div by div from one tag
    for tag in tag_div2:
        print(tag.get_text(),"\n")

    return quick_start


# "Installing Beautiful Soup" Scraping texts
def instal_bfs():
    tag_div = site.find("div", id="installing-beautiful-soup")
    tag_h1 = tag_div.find("h1")
    print(tag_h1.get_text()[0:25])

    tag_p = tag_div.find_all(["p"])[0:11]
    print()
    for i in tag_p:
        print(i.get_text(),"\n")

    return instal_bfs


# "Problems After Installation" Scraping texts
def problems_after():
    tag_div = site.find("div", id="problems-after-installation")
    tag_h1 = tag_div.find("h2")
    print(tag_h1.get_text()[0:27])

    tag_p = tag_div.find_all(["p"])[0:8]
    print()
    for i in tag_p:
        print(i.get_text(),"\n")

    return problems_after



first()
tag_help()
quick_start()
instal_bfs()
problems_after()


# for tag in text_1:
#     p = tag.get_text() # pega a teg p e outras merdas
#     print(p)

#print(text_1.p.get_text()) # pega a primeira teg p atravez da div