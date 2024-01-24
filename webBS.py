import requests
from bs4 import BeautifulSoup

link = 'https://beautiful-soup-4.readthedocs.io/en/latest/#' #link do site a ser raspado
hearders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"} #requissição de usuario

requisition = requests.get(link, headers=hearders) # requisição do site e do navegador
print(requisition)
site = BeautifulSoup(requisition.text, "html.parser")

# Description Scraping
def first():
    print()
    page_title = site.find("title") #busca titulo h1
    print('***',page_title.get_text()[0:28].upper(),'***')

    print()
    tag_div = site.find("div", id="beautiful-soup-documentation")  # busca div da descrição breve
    tag_p = tag_div.find_all(["p"])[0:4] # funciona, pega a tag p até as linhas desejadas
    for i in tag_p:
        print(i.get_text()) # Funcionou pegou todas as tags p da div desejada
    return first

# Help Scraping
def tag_help():
    print()
    tag_div = site.find("div", id="getting-help") # find div from getting-help
    tag_h2 = tag_div.find(["h2"])
    print(tag_h2.get_text()[0:12])
    tag_p = tag_div.find_all(["p"])
    for i in tag_p:
        print(i.get_text()) 

    return tag_help

# Quick Start Scraping
def quick_start():
    print()
    tag_div = site.find(id="quick-start") # find div from quick-start
    tag_h2 = tag_div.find(["h1"])
    print(tag_h2.get_text()[0:11])

    tag_p = tag_div.find_all(["p"])[0:1]
    for i in tag_p:
        print(i.get_text())
    print()
    tag_div2 = tag_div.find_all("div", class_="highlight")[0:1] # Find div by div from one tag
    for tag in tag_div2:
        print(tag.get_text())


    tag_p2 = tag_div.find_all(["p"])[1:2]
    for i in tag_p2:
        print()
        print(i.get_text())
    print()
    tag_div3 = tag_div.find_all("div", class_="highlight")[1:2]
    for tag in tag_div3:
        print(tag.get_text())


    tag_p3 = tag_div.find_all(["p"])[2:3]
    for i in tag_p3:
        print()
        print(i.get_text())
    print()
    tag_div4 = tag_div.find_all("div", class_="highlight")[2:3]
    for tag in tag_div4:
        print(tag.get_text())


    tag_p4 = tag_div.find_all(["p"])[3:4]
    for i in tag_p4:
        print()
        print(i.get_text())
    print()
    tag_div2 = tag_div.find_all("div", class_="highlight")[3:4]
    for tag in tag_div2:
        print(tag.get_text())


    tag_p5 = tag_div.find_all(["p"])[4:5]
    for i in tag_p5:
        print()
        print(i.get_text())
    print()
    tag_div2 = tag_div.find_all("div", class_="highlight")[4:5]
    for tag in tag_div2:
        print(tag.get_text())


    tag_p6 = tag_div.find_all(["p"])[5:6]
    for i in tag_p6:
        print()
        print(i.get_text())

    return quick_start



first()
tag_help()
quick_start()



# for tag in text_1:
#     p = tag.get_text() # pega a teg p e outras merdas
#     print(p)

#print(text_1.p.get_text()) # pega a primeira teg p atravez da div