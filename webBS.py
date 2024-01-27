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
    tag_h2 = tag_div.find("h2")
    print(tag_h2.get_text()[0:27])

    tag_p = tag_div.find_all(["p"])[0:8]
    print()
    for i in tag_p:
        print(i.get_text(),"\n")

    return problems_after


# "Installing a parser" Scraping texts
def install_parser():
    tag_div = site.find("div", id="installing-a-parser")
    tag_h2 = tag_div.find("h2")
    print(tag_h2.get_text()[0:19])

    tag_p = tag_div.find_all(["p"])[0:8]
    print()
    for i in tag_p:
        print(i.get_text(),"\n")

    # to fix this
    table = tag_div.find_all("table", class_="docutils") # find table
    for i in table:
        print("-"*50,i.text,"-"*50)

    tag_p = tag_div.find_all(["p"])[8:10]
    print()
    for i in tag_p:
        print(i.get_text(),"\n")

    return install_parser


# "Making the soup" Scraping texts
def making_soup():
    tag_div = site.find("div", id="making-the-soup")
    tag_h1 = tag_div.find("h1")
    print(tag_h1.get_text()[0:15])

    tag_p1 = tag_div.find_all(["p"])[0:1]
    print()
    for i in tag_p1:
        print(i.get_text(),"\n")

    tag_div2 = tag_div.find_all("div", class_="highlight")[0:1] # Find div by div from one tag
    for tag in tag_div2:
        print(tag.get_text(),"\n")

    tag_p2 = tag_div.find_all(["p"])[1:2]
    print()
    for i in tag_p2:
        print(i.get_text(),"\n")

    tag_div2 = tag_div.find_all("div", class_="highlight")[1:2] # Find div by div from one tag
    for tag in tag_div2:
        print(tag.get_text(),"\n")

    tag_p2 = tag_div.find_all(["p"])[2:3]
    print()
    for i in tag_p2:
        print(i.get_text(),"\n")

    return making_soup


# "Kinds of objects" Scraping texts
def Kind_obj():
    tag_div = site.find("div", id="kinds-of-objects")
    tag_h1 = tag_div.find("h1")
    print(tag_h1.get_text()[0:16])

    tag_p1 = tag_div.find_all(["p"])[0:2]
    print()
    for i in tag_p1:
        print(i.get_text(),"\n")

    tag_div2 = tag_div.find_all("div", class_="highlight")[0:1] # Find div by div from one tag
    for tag in tag_div2:
        print(tag.get_text(),"\n")

    tag_p2 = tag_div.find_all(["p"])[2:3]
    print()
    for i in tag_p2:
        print(i.get_text(),"\n")

    # "name section"
    def name():
        div_n = tag_div.find("div", id="name")
        name = div_n.find("h3")
        print(name.get_text()[0:4])

        tag_p1 = div_n.find_all(["p"])[0:1]
        print()
        for i in tag_p1:
            print(i.get_text(),"\n")

        div_n2 = div_n.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
        for tag in div_n2:
            print(tag.get_text(),"\n")

        tag_p2 = div_n.find_all(["p"])[1:2]
        print()
        for i in tag_p2:
            print(i.get_text(),"\n")

        div_n2 = div_n.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
        for tag in div_n2:
            print(tag.get_text(),"\n")

        return name
    
    # "attributes section"
    def attributes():
        div_att = tag_div.find("div", id="attributes")
        tag_h3 = div_att.find("h3")
        print(tag_h3.get_text()[0:10])

        tag_p1 = div_att.find_all(["p"])[0:1]
        print()
        for i in tag_p1:
            print(i.get_text(),"\n")

        div_at2 = div_att.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
        for tag in div_at2:
            print(tag.get_text(),"\n")

        tag_p2 = div_att.find_all(["p"])[1:2]
        print()
        for i in tag_p2:
            print(i.get_text(),"\n")

        div_at3 = div_att.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
        for tag in div_at3:
            print(tag.get_text(),"\n")

        tag_p2 = div_att.find_all(["p"])[2:3]
        print()
        for i in tag_p2:
            print(i.get_text(),"\n")

        div_at3 = div_att.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
        for tag in div_at3:
            print(tag.get_text(),"\n")

        return attributes
    
    # "multi valued attributes"
    def mult_val_attr():
        tag_mva = tag_div.find("div", id="multi-valued-attributes")
        tag_h4 = tag_mva.find("h4")
        print(tag_h4.get_text()[0:23])

        tag_p1 = tag_mva.find_all(["p"])[0:1]
        print()
        for i in tag_p1:
            print(i.get_text(),"\n")

        div_mva1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
        for tag in div_mva1:
            print(tag.get_text(),"\n")

        tag_p2 = tag_mva.find_all(["p"])[1:2]
        print()
        for i in tag_p2:
            print(i.get_text(),"\n")

        div_mva2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
        for tag in div_mva2:
            print(tag.get_text(),"\n")

        tag_p3 = tag_mva.find_all(["p"])[2:3]
        print()
        for i in tag_p3:
            print(i.get_text(),"\n")

        div_mva3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
        for tag in div_mva3:
            print(tag.get_text(),"\n")

        tag_p4 = tag_mva.find_all(["p"])[3:4]
        print()
        for i in tag_p4:
            print(i.get_text(),"\n")

        div_mva4 = tag_div.find_all("div", class_="highlight-default notranslate")[3:4] # Find div by div from one tag
        for tag in div_mva4:
            print(tag.get_text(),"\n")

        tag_p5 = tag_mva.find_all(["p"])[4:5]
        print()
        for i in tag_p5:
            print(i.get_text(),"\n")

        div_mva5 = tag_div.find_all("div", class_="highlight-default notranslate")[4:5] # Find div by div from one tag
        for tag in div_mva5:
            print(tag.get_text(),"\n")

        tag_p6 = tag_mva.find_all(["p"])[5:6]
        print()
        for i in tag_p6:
            print(i.get_text(),"\n")

        div_mva6 = tag_div.find_all("div", class_="highlight-default notranslate")[5:6] # Find div by div from one tag
        for tag in div_mva6:
            print(tag.get_text(),"\n")

        tag_p7 = tag_mva.find_all(["p"])[6:7]
        print()
        for i in tag_p7:
            print(i.get_text(),"\n")

        div_mva7 = tag_div.find_all("div", class_="highlight-default notranslate")[6:7] # Find div by div from one tag
        for tag in div_mva7:
            print(tag.get_text(),"\n")

        tag_p8 = tag_mva.find_all(["p"])[7:8]
        print()
        for i in tag_p8:
            print(i.get_text(),"\n")

        div_mva8 = tag_div.find_all("div", class_="highlight-default notranslate")[7:8] # Find div by div from one tag
        for tag in div_mva8:
            print(tag.get_text(),"\n")

        return mult_val_attr
    
    # "Navigablestring"
    def navigablestring():
        tag_mva = tag_div.find("div", id="navigablestring")
        tag_h4 = tag_mva.find("h2")
        print(tag_h4.get_text()[0:15])

        tag_p1 = tag_mva.find_all(["p"])[0:1]
        print()
        for i in tag_p1:
            print(i.get_text(),"\n")

        div_nav1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
        for tag in div_nav1:
            print(tag.get_text(),"\n")

        tag_p2 = tag_mva.find_all(["p"])[1:2]
        print()
        for i in tag_p2:
            print(i.get_text(),"\n")

        div_nav2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
        for tag in div_nav2:
            print(tag.get_text(),"\n")

        tag_p3 = tag_mva.find_all(["p"])[2:3]
        print()
        for i in tag_p3:
            print(i.get_text(),"\n")

        div_nav3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
        for tag in div_nav3:
            print(tag.get_text(),"\n")

        tag_p4 = tag_mva.find_all(["p"])[3:5]
        print()
        for i in tag_p4:
            print(i.get_text(),"\n")

        return navigablestring
    
    # "beautifulsoup"
    def beautifulsoup():
        tag_btf = tag_div.find("div", id="beautifulsoup")
        tag_h4 = tag_btf.find("h2")
        print(tag_h4.get_text()[0:13])
        
        tag_p1 = tag_btf.find_all(["p"])[0:2]
        print()
        for i in tag_p1:
            print(i.get_text(),"\n")

        div_btf1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
        for tag in div_btf1:
            print(tag.get_text(),"\n")

        tag_p2 = tag_btf.find_all(["p"])[2:3]
        print()
        for i in tag_p2:
            print(i.get_text(),"\n")

        div_btf2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
        for tag in div_btf2:
            print(tag.get_text(),"\n")

        return beautifulsoup

    # "Comments and other special strings"
    def comments_oss():
        tag_com = tag_div.find("div", id="comments-and-other-special-strings")
        tag_h4 = tag_com.find("h2")
        print(tag_h4.get_text()[0:34])

        tag_p1 = tag_com.find_all(["p"])[0:1]
        print()
        for i in tag_p1:
            print(i.get_text(),"\n")

        div_com1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
        for tag in div_com1:
            print(tag.get_text(),"\n")

        tag_p2 = tag_com.find_all(["p"])[1:2]
        print()
        for i in tag_p2:
            print(i.get_text(),"\n")

        div_com2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
        for tag in div_com2:
            print(tag.get_text(),"\n")

        tag_p3 = tag_com.find_all(["p"])[2:3]
        print()
        for i in tag_p3:
            print(i.get_text(),"\n")

        div_com3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
        for tag in div_com3:
            print(tag.get_text(),"\n")

        tag_p4 = tag_com.find_all(["p"])[3:4]
        print()
        for i in tag_p4:
            print(i.get_text(),"\n")

        div_com4 = tag_div.find_all("div", class_="highlight-default notranslate")[3:4] # Find div by div from one tag
        for tag in div_com4:
            print(tag.get_text(),"\n")

        return comments_oss

    name()
    attributes()
    mult_val_attr()
    navigablestring()
    beautifulsoup()
    comments_oss()
    return Kind_obj


# "Navigating the tree" Scraping text
def nav_tree():
    tag_div = site.find("div", id="navigating-the-tree")
    tag_h1 = tag_div.find("h1")
    print(tag_h1.get_text()[0:19])

    tag_p1 = tag_div.find_all(["p"])[0:1]
    print()
    for i in tag_p1:
        print(i.get_text(),"\n")

    div_tree1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
    for tag in div_tree1:
        print(tag.get_text(),"\n")

    tag_p2 = tag_div.find_all(["p"])[1:2]
    print()
    for i in tag_p2:
        print(i.get_text(),"\n")

    # "Going down"
    def going_down():
        tag_div_down = site.find("div", id="going-down")
        tag_h1 = tag_div_down.find("h2")
        print(tag_h1.get_text()[0:10])
        
        tag_p_d = tag_div_down.find_all(["p"])[0:2]
        print()
        for i in tag_p_d:
            print(i.get_text(),"\n")

        # "Navigating using tag names"
        def nav_tag_nam():
            tag_div = site.find("div", id="navigating-using-tag-names")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:26])

            tag_p = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")

            tag_p2 = tag_div.find_all(["p"])[1:2]
            print()
            for i in tag_p2:
                print(i.get_text(),"\n")

            div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
            for tag in div_2:
                print(tag.get_text(),"\n")

            tag_p3 = tag_div.find_all(["p"])[2:3]
            print()
            for i in tag_p3:
                print(i.get_text(),"\n")

            div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
            for tag in div_3:
                print(tag.get_text(),"\n")

            tag_p4 = tag_div.find_all(["p"])[3:4]
            print()
            for i in tag_p4:
                print(i.get_text(),"\n")

            div_4 = tag_div.find_all("div", class_="highlight-default notranslate")[3:4] # Find div by div from one tag
            for tag in div_4:
                print(tag.get_text(),"\n")

            return nav_tag_nam
        
        # "Contents_and_children"
        def contents_and_children():
            tag_div = site.find("div", id="contents-and-children")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:23])

            tag_p = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")

            tag_p2 = tag_div.find_all(["p"])[1:2]
            print()
            for i in tag_p2:
                print(i.get_text(),"\n")

            div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
            for tag in div_2:
                print(tag.get_text(),"\n")

            tag_p3 = tag_div.find_all(["p"])[2:3]
            print()
            for i in tag_p3:
                print(i.get_text(),"\n")

            div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
            for tag in div_3:
                print(tag.get_text(),"\n")

            tag_p4 = tag_div.find_all(["p"])[3:4]
            print()
            for i in tag_p4:
                print(i.get_text(),"\n")

            div_4 = tag_div.find_all("div", class_="highlight-default notranslate")[3:4] # Find div by div from one tag
            for tag in div_4:
                print(tag.get_text(),"\n")

            return contents_and_children

        # "descendants"
        def descendants():
            tag_div = site.find("div", id="contents-and-children")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:10])

            tag_p = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")

            tag_p2 = tag_div.find_all(["p"])[1:2]
            print()
            for i in tag_p2:
                print(i.get_text(),"\n")

            div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
            for tag in div_2:
                print(tag.get_text(),"\n")

            tag_p3 = tag_div.find_all(["p"])[2:3]
            print()
            for i in tag_p3:
                print(i.get_text(),"\n")

            div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
            for tag in div_3:
                print(tag.get_text(),"\n")

            return descendants

        # "string"
        def string():
            tag_div = site.find("div", id="string")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:7])

            tag_p = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")

            tag_p2 = tag_div.find_all(["p"])[1:2]
            print()
            for i in tag_p2:
                print(i.get_text(),"\n")

            div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
            for tag in div_2:
                print(tag.get_text(),"\n")

            tag_p3 = tag_div.find_all(["p"])[2:3]
            print()
            for i in tag_p3:
                print(i.get_text(),"\n")

            div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
            for tag in div_3:
                print(tag.get_text(),"\n")

            return string

        # ".strings and stripped_strings"
        def strings_strip():
            tag_div = site.find("div", id="strings-and-stripped-strings")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:29])

            tag_p = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")

            tag_p2 = tag_div.find_all(["p"])[1:2]
            print()
            for i in tag_p2:
                print(i.get_text(),"\n")

            div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
            for tag in div_2:
                print(tag.get_text(),"\n")

            tag_p3 = tag_div.find_all(["p"])[2:3]
            print()
            for i in tag_p3:
                print(i.get_text(),"\n")

            return strings_strip

        nav_tag_nam()
        contents_and_children()
        descendants()
        string()
        strings_strip()
        return going_down

#########################################################
    # Continuar "Going up"
    def going_up():
        tag_div = site.find("div", id="going-up")
        tag_h3 = tag_div.find("h2")
        print(tag_h3.get_text()[0:8])
        
        tag_p = tag_div.find_all(["p"])[0:1]
        print()
        for i in tag_p:
            print(i.get_text(),"\n")

        return going_up
    

    # Continuar "Going sideways"
    def going_sideways():

        return going_sideways
    
    # Continuar "Going back and forth"
    def going_b_for():

        return going_b_for

    going_down()
    going_up
    going_sideways
    going_b_for

    return nav_tree


first
tag_help
quick_start
instal_bfs
problems_after
install_parser
making_soup # daqui pra cima corrigir e melhorar
Kind_obj
nav_tree()
