import requests
from bs4 import BeautifulSoup

link = 'https://beautiful-soup-4.readthedocs.io/en/latest/#' # Website link to be scraped
hearders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"} # User request

requisition = requests.get(link, headers=hearders) # Website and browser request
print(requisition)
site = BeautifulSoup(requisition.text, "html.parser")


# "Description" Scraping texts
def first():
    print()
    page_title = site.find("title") # Get tag item
    print('***',page_title.get_text()[0:28].upper(),'***')

    print()
    tag_div = site.find("div", id="beautiful-soup-documentation")  
    tag_p = tag_div.find_all(["p"])[0:4] # Get the p tag to the desired lines
    for i in tag_p:
        print(i.get_text(),"\n")

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


    # "Going up" Scraping text
    def going_up():
        tag_div = site.find("div", id="going-up")
        tag_h3 = tag_div.find("h2")
        print(tag_h3.get_text()[0:8])
        
        tag_p = tag_div.find_all(["p"])[0:1]
        print()
        for i in tag_p:
            print(i.get_text(),"\n")
            
        # Parent
        def parent():
            tag_div = site.find("div", id="parent")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:7])

            tag_p1 = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_2:
                print(tag.get_text(),"\n")

            tag_p2 = tag_div.find_all(["p"])[1:2]
            print()
            for i in tag_p2:
                print(i.get_text(),"\n")

            div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
            for tag in div_3:
                print(tag.get_text(),"\n")

            tag_p3 = tag_div.find_all(["p"])[2:3]
            print()
            for i in tag_p3:
                print(i.get_text(),"\n")

            div_4 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
            for tag in div_4:
                print(tag.get_text(),"\n")

            tag_p4 = tag_div.find_all(["p"])[3:4]
            print()
            for i in tag_p4:
                print(i.get_text(),"\n")

            div_5 = tag_div.find_all("div", class_="highlight-default notranslate")[3:4] # Find div by div from one tag
            for tag in div_5:
                print(tag.get_text(),"\n")

            return parent
        
        #Parents
        def parents():
            tag_div = site.find("div", id="parents")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:7])

            tag_p1 = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_2:
                print(tag.get_text(),"\n")

            return parents
        
        parent()
        parents()
        return going_up

    # "Going sideways"
    def going_sideways():
        tag_div = site.find("div", id="going-sideways")
        tag_h3 = tag_div.find("h2")
        print(tag_h3.get_text()[0:14])

        tag_p1 = tag_div.find_all(["p"])[0:1]
        print()
        for i in tag_p1:
            print(i.get_text(),"\n")

        div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
        for tag in div_1:
            print(tag.get_text(),"\n")

        tag_p2 = tag_div.find_all(["p"])[1:2]
        print()
        for i in tag_p2:
            print(i.get_text(),"\n")


        def next_previous():
            tag_div = site.find("div", id="next-sibling-and-previous-sibling")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:31])

            tag_p1 = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p1:
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

            tag_p5 = tag_div.find_all(["p"])[4:5]
            print()
            for i in tag_p5:
                print(i.get_text(),"\n")

            div_5 = tag_div.find_all("div", class_="highlight-default notranslate")[4:5] # Find div by div from one tag
            for tag in div_5:
                print(tag.get_text(),"\n")
        
            tag_p6 = tag_div.find_all(["p"])[5:6]
            print()
            for i in tag_p6:
                print(i.get_text(),"\n")

            div_6 = tag_div.find_all("div", class_="highlight-default notranslate")[5:6] # Find div by div from one tag
            for tag in div_6:
                print(tag.get_text(),"\n")

            return next_previous

        def next_previous2():
            tag_div = site.find("div", id="next-siblings-and-previous-siblings")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:38])

            tag_p1 = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")

            return next_previous2
        
        next_previous()
        next_previous2()
        return going_sideways
    
    def going_b_for():
        tag_div = site.find("div", id="going-back-and-forth")
        tag_h3 = tag_div.find("h2")
        print(tag_h3.get_text()[0:20])

        tag_p1 = tag_div.find_all(["p"])[0:1]
        print()
        for i in tag_p1:
            print(i.get_text(),"\n")

        div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
        for tag in div_1:
            print(tag.get_text(),"\n")

        tag_p2 = tag_div.find_all(["p"])[1:2]
        print()
        for i in tag_p2:
            print(i.get_text(),"\n")
        

        def next_prev_element():
            tag_div = site.find("div", id="next-element-and-previous-element")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:34])

            tag_p1 = tag_div.find_all(["p"])[0:2]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")

            tag_p2 = tag_div.find_all(["p"])[2:3]
            print()
            for i in tag_p2:
                print(i.get_text(),"\n")

            div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
            for tag in div_2:
                print(tag.get_text(),"\n")
            
            tag_p3 = tag_div.find_all(["p"])[3:5]
            print()
            for i in tag_p3:
                print(i.get_text(),"\n")
            
            div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
            for tag in div_3:
                print(tag.get_text(),"\n")

            return next_prev_element


        def next_prev_element2():
            tag_div = site.find("div", id="next-elements-and-previous-elements")
            tag_h3 = tag_div.find("h3")
            print(tag_h3.get_text()[0:34])

            tag_p1 = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")
    
            return next_prev_element2
            
        next_prev_element()
        next_prev_element2()
        return going_b_for

    going_down()
    going_up()
    going_sideways()
    going_b_for()
    return nav_tree


# "Searching the tree" Scraping text
def search_tree():
    tag_div = site.find("div", id="searching-the-tree")
    tag_h1 = tag_div.find("h1")
    print(tag_h1.get_text()[0:18])

    tag_p1 = tag_div.find_all(["p"])[0:2]
    print()
    for i in tag_p1:
        print(i.get_text(),"\n")

    div_tree1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
    for tag in div_tree1:
        print(tag.get_text(),"\n")

    tag_p2 = tag_div.find_all(["p"])[2:3]
    print()
    for i in tag_p2:
        print(i.get_text(),"\n")

    def Kinds_filters():
        tag_div = site.find("div", id="kinds-of-filters")
        tag_h1 = tag_div.find("h2")
        print(tag_h1.get_text()[0:16])

        tag_p1 = tag_div.find_all(["p"])[0:1]
        print()
        for i in tag_p1:
            print(i.get_text(),"\n")

        def a_string():
            tag_div = site.find("div", id="a-string")
            tag_h1 = tag_div.find("h3")
            print(tag_h1.get_text()[0:8])

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

            return a_string

        def reg_expres():
            tag_div = site.find("div", id="a-regular-expression")
            tag_h1 = tag_div.find("h3")
            print(tag_h1.get_text()[0:20])

            tag_p1 = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p1:
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

            return reg_expres
        
        def a_list():
            tag_div = site.find("div", id="a-list")
            tag_h1 = tag_div.find("h3")
            print(tag_h1.get_text()[0:6])

            tag_p1 = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")   
            
            return a_list
        
        def true():
            tag_div = site.find("div", id="true")
            tag_h1 = tag_div.find("h3")
            print(tag_h1.get_text()[0:6])

            tag_p1 = tag_div.find_all(["p"])[0:1]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")   
            
            return true
        
        def a_function():
            tag_div = site.find("div", id="a-function")
            tag_h1 = tag_div.find("h3")
            print(tag_h1.get_text()[0:6])

            tag_p1 = tag_div.find_all(["p"])[0:2]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")   

            tag_p2 = tag_div.find_all(["p"])[2:3]
            print()
            for i in tag_p2:
                print(i.get_text(),"\n")

            div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
            for tag in div_2:
                print(tag.get_text(),"\n")   

            tag_p3 = tag_div.find_all(["p"])[3:5]
            print()
            for i in tag_p3:
                print(i.get_text(),"\n")

            div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
            for tag in div_3:
                print(tag.get_text(),"\n") 

            tag_p4 = tag_div.find_all(["p"])[5:6]
            print()
            for i in tag_p4:
                print(i.get_text(),"\n")

            div_4 = tag_div.find_all("div", class_="highlight-default notranslate")[3:4] # Find div by div from one tag
            for tag in div_4:
                print(tag.get_text(),"\n") 

            tag_p5 = tag_div.find_all(["p"])[6:7]
            print()
            for i in tag_p5:
                print(i.get_text(),"\n")

            return a_function
        
        def find_all():
            tag_div = site.find("div", id="find-all")
            tag_h1 = tag_div.find("h2")
            print(tag_h1.get_text()[0:8])

            tag_p1 = tag_div.find_all(["p"])[0:2]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
            for tag in div_1:
                print(tag.get_text(),"\n")   

            tag_p1 = tag_div.find_all(["p"])[1:3]
            print()
            for i in tag_p1:
                print(i.get_text(),"\n")

            def the_name_arg():
                tag_div = site.find("div", id="the-name-argument")
                tag_h1 = tag_div.find("h3")
                print(tag_h1.get_text()[0:17])

                tag_p1 = tag_div.find_all(["p"])[0:2]
                print()
                for i in tag_p1:
                    print(i.get_text(),"\n")

                div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
                for tag in div_1:
                    print(tag.get_text(),"\n")  

                tag_p2 = tag_div.find_all(["p"])[2:3]
                print()
                for i in tag_p2:
                    print(i.get_text(),"\n")

                return the_name_arg

            def the_kword_args():
                tag_div = site.find("div", id="the-keyword-arguments")
                tag_h1 = tag_div.find("h3")
                print(tag_h1.get_text()[0:21])

                tag_p1 = tag_div.find_all(["p"])[0:1]
                print()
                for i in tag_p1:
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

                tag_p3 = tag_div.find_all(["p"])[2:4]
                print()
                for i in tag_p3:
                    print(i.get_text(),"\n")

                div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
                for tag in div_3:
                    print(tag.get_text(),"\n") 

                tag_p4 = tag_div.find_all(["p"])[4:5]
                print()
                for i in tag_p4:
                    print(i.get_text(),"\n")

                div_4 = tag_div.find_all("div", class_="highlight-default notranslate")[3:4] # Find div by div from one tag
                for tag in div_4:
                    print(tag.get_text(),"\n") 

                tag_p5 = tag_div.find_all(["p"])[5:6]
                print()
                for i in tag_p5:
                    print(i.get_text(),"\n")

                div_5 = tag_div.find_all("div", class_="highlight-default notranslate")[4:5] # Find div by div from one tag
                for tag in div_5:
                    print(tag.get_text(),"\n") 

                tag_p6 = tag_div.find_all(["p"])[6:7]
                print()
                for i in tag_p6:
                    print(i.get_text(),"\n")

                div_6 = tag_div.find_all("div", class_="highlight-default notranslate")[5:6] # Find div by div from one tag
                for tag in div_6:
                    print(tag.get_text(),"\n") 

                tag_p7 = tag_div.find_all(["p"])[7:8]
                print()
                for i in tag_p7:
                    print(i.get_text(),"\n")

                div_7 = tag_div.find_all("div", class_="highlight-default notranslate")[6:7] # Find div by div from one tag
                for tag in div_7:
                    print(tag.get_text(),"\n") 

                return the_kword_args            

            def searchcss_cls():
                tag_div = site.find("div", id="searching-by-css-class")
                tag_h1 = tag_div.find("h3")
                print(tag_h1.get_text()[0:22])

                tag_p1 = tag_div.find_all(["p"])[0:1]
                print()
                for i in tag_p1:
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

                tag_p5 = tag_div.find_all(["p"])[4:5]
                print()
                for i in tag_p5:
                    print(i.get_text(),"\n")

                div_5 = tag_div.find_all("div", class_="highlight-default notranslate")[4:5] # Find div by div from one tag
                for tag in div_5:
                    print(tag.get_text(),"\n") 

                tag_p6 = tag_div.find_all(["p"])[5:6]
                print()
                for i in tag_p6:
                    print(i.get_text(),"\n")

                div_6 = tag_div.find_all("div", class_="highlight-default notranslate")[5:6] # Find div by div from one tag
                for tag in div_6:
                    print(tag.get_text(),"\n") 

                tag_p7 = tag_div.find_all(["p"])[6:7]
                print()
                for i in tag_p7:
                    print(i.get_text(),"\n")

                div_7 = tag_div.find_all("div", class_="highlight-default notranslate")[6:7] # Find div by div from one tag
                for tag in div_7:
                    print(tag.get_text(),"\n") 

                return searchcss_cls


            def string_argument():
                tag_div = site.find("div", id="the-string-argument")
                tag_h1 = tag_div.find("h3")
                print(tag_h1.get_text()[0:19])

                tag_p1 = tag_div.find_all(["p"])[0:1]
                print()
                for i in tag_p1:
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

                return string_argument


            def limit_argument():
                tag_div = site.find("div", id="the-limit-argument")
                tag_h1 = tag_div.find("h3")
                print(tag_h1.get_text()[0:18])

                tag_p1 = tag_div.find_all(["p"])[0:2]
                print()
                for i in tag_p1:
                    print(i.get_text(),"\n")

                div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
                for tag in div_1:
                    print(tag.get_text(),"\n")

                return limit_argument

            def recursive_argument():
                tag_div = site.find("div", id="the-recursive-argument")
                tag_h1 = tag_div.find("h3")
                print(tag_h1.get_text()[0:22])

                tag_p1 = tag_div.find_all(["p"])[0:1]
                print()
                for i in tag_p1:
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

                tag_p3 = tag_div.find_all(["p"])[2:4]
                print()
                for i in tag_p3:
                    print(i.get_text(),"\n")

                return recursive_argument
            
            def call_tag_like():
                tag_div = site.find("div", id="calling-a-tag-is-like-calling-find-all")
                tag_h1 = tag_div.find("h2")
                print(tag_h1.get_text()[0:22])

                tag_p1 = tag_div.find_all(["p"])[0:1]
                print()
                for i in tag_p1:
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

                return call_tag_like

            def find():
                tag_div = site.find("div", id="find")
                tag_h1 = tag_div.find("h2")
                print(tag_h1.get_text()[0:6])

                tag_p1 = tag_div.find_all(["p"])[0:2]
                print()
                for i in tag_p1:
                    print(i.get_text(),"\n")

                div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
                for tag in div_1:
                    print(tag.get_text(),"\n")

                tag_p2 = tag_div.find_all(["p"])[2:4]
                print()
                for i in tag_p2:
                    print(i.get_text(),"\n")

                div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
                for tag in div_2:
                    print(tag.get_text(),"\n")

                tag_p3 = tag_div.find_all(["p"])[4:5]
                print()
                for i in tag_p3:
                    print(i.get_text(),"\n")

                div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
                for tag in div_3:
                    print(tag.get_text(),"\n")

                return find

            def find_parent():
                tag_div = site.find("div", id="find-parents-and-find-parent")
                tag_h1 = tag_div.find("h2")
                print(tag_h1.get_text()[0:30])

                tag_p1 = tag_div.find_all(["p"])[0:4]
                print()
                for i in tag_p1:
                    print(i.get_text(),"\n")

                div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
                for tag in div_1:
                    print(tag.get_text(),"\n")

                tag_p2 = tag_div.find_all(["p"])[4:6]
                print()
                for i in tag_p2:
                    print(i.get_text(),"\n")

                return find_parent

            def find_next_sibling():
                tag_div = site.find("div", id="find-next-siblings-and-find-next-sibling")
                tag_h1 = tag_div.find("h2")
                print(tag_h1.get_text()[0:30])

                tag_p1 = tag_div.find_all(["p"])[0:3]
                print()
                for i in tag_p1:
                    print(i.get_text(),"\n")

                div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
                for tag in div_1:
                    print(tag.get_text(),"\n")

                return find_next_sibling

            def find_prev_sibling():
                tag_div = site.find("div", id="find-previous-siblings-and-find-previous-sibling")
                tag_h1 = tag_div.find("h2")
                print(tag_h1.get_text()[0:50])

                tag_p1 = tag_div.find_all(["p"])[0:3]
                print()
                for i in tag_p1:
                    print(i.get_text(),"\n")

                div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
                for tag in div_1:
                    print(tag.get_text(),"\n")

                return find_prev_sibling

            def find_all_next():
                tag_div = site.find("div", id="find-all-next-and-find-next")
                tag_h1 = tag_div.find("h2")
                print(tag_h1.get_text()[0:31])

                tag_p1 = tag_div.find_all(["p"])[0:3]
                print()
                for i in tag_p1:
                    print(i.get_text(),"\n")

                div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
                for tag in div_1:
                    print(tag.get_text(),"\n")

                tag_p2 = tag_div.find_all(["p"])[3:4]
                print()
                for i in tag_p2:
                    print(i.get_text(),"\n")

                return find_all_next

            def find_all_prev():
                tag_div = site.find("div", id="find-all-previous-and-find-previous")
                tag_h1 = tag_div.find("h2")
                print(tag_h1.get_text()[0:37])

                tag_p1 = tag_div.find_all(["p"])[0:3]
                print()
                for i in tag_p1:
                    print(i.get_text(),"\n")

                div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
                for tag in div_1:
                    print(tag.get_text(),"\n")

                tag_p2 = tag_div.find_all(["p"])[3:4]
                print()
                for i in tag_p2:
                    print(i.get_text(),"\n")

                return find_all_prev
            
            def css_selectors():
                tag_div = site.find("div", id="css-selectors")
                tag_h1 = tag_div.find("h2")
                print(tag_h1.get_text()[0:13])


                tag_p1 = tag_div.find_all(["p"])[0:5]
                print()
                for i in tag_p1:
                    print(i.get_text(),"\n")

                div_1 = tag_div.find_all("div", class_="highlight-default notranslate")[0:1] # Find div by div from one tag
                for tag in div_1:
                    print(tag.get_text(),"\n")

                tag_p2 = tag_div.find_all(["p"])[5:6]
                print()
                for i in tag_p2:
                    print(i.get_text(),"\n")

                div_2 = tag_div.find_all("div", class_="highlight-default notranslate")[1:2] # Find div by div from one tag
                for tag in div_2:
                    print(tag.get_text(),"\n")

                tag_p3 = tag_div.find_all(["p"])[6:7]
                print()
                for i in tag_p3:
                    print(i.get_text(),"\n")

                div_3 = tag_div.find_all("div", class_="highlight-default notranslate")[2:3] # Find div by div from one tag
                for tag in div_3:
                    print(tag.get_text(),"\n")

                tag_p4 = tag_div.find_all(["p"])[7:8]
                print()
                for i in tag_p4:
                    print(i.get_text(),"\n")

                div_4 = tag_div.find_all("div", class_="highlight-default notranslate")[3:4] # Find div by div from one tag
                for tag in div_4:
                    print(tag.get_text(),"\n")

                tag_p5 = tag_div.find_all(["p"])[8:9]
                print()
                for i in tag_p5:
                    print(i.get_text(),"\n")

                div_5 = tag_div.find_all("div", class_="highlight-default notranslate")[4:5] # Find div by div from one tag
                for tag in div_5:
                    print(tag.get_text(),"\n")

                tag_p6 = tag_div.find_all(["p"])[9:10]
                print()
                for i in tag_p6:
                    print(i.get_text(),"\n")

                div_6 = tag_div.find_all("div", class_="highlight-default notranslate")[5:6] # Find div by div from one tag
                for tag in div_6:
                    print(tag.get_text(),"\n")

                tag_p7 = tag_div.find_all(["p"])[10:11]
                print()
                for i in tag_p7:
                    print(i.get_text(),"\n")

                div_7 = tag_div.find_all("div", class_="highlight-default notranslate")[6:7] # Find div by div from one tag
                for tag in div_7:
                    print(tag.get_text(),"\n")

                tag_p8 = tag_div.find_all(["p"])[11:12]
                print()
                for i in tag_p8:
                    print(i.get_text(),"\n")

                div_8 = tag_div.find_all("div", class_="highlight-default notranslate")[7:8] # Find div by div from one tag
                for tag in div_8:
                    print(tag.get_text(),"\n")

                tag_p9 = tag_div.find_all(["p"])[12:13]
                print()
                for i in tag_p9:
                    print(i.get_text(),"\n")

                div_9 = tag_div.find_all("div", class_="highlight-default notranslate")[8:9] # Find div by div from one tag
                for tag in div_9:
                    print(tag.get_text(),"\n")

                tag_p10 = tag_div.find_all(["p"])[13:14]
                print()
                for i in tag_p10:
                    print(i.get_text(),"\n")

                div_10 = tag_div.find_all("div", class_="highlight-default notranslate")[9:10] # Find div by div from one tag
                for tag in div_10:
                    print(tag.get_text(),"\n")

                tag_p11 = tag_div.find_all(["p"])[14:15]
                print()
                for i in tag_p11:
                    print(i.get_text(),"\n")

                div_11 = tag_div.find_all("div", class_="highlight-default notranslate")[10:11] # Find div by div from one tag
                for tag in div_11:
                    print(tag.get_text(),"\n")

                tag_p12 = tag_div.find_all(["p"])[15:16]
                print()
                for i in tag_p12:
                    print(i.get_text(),"\n")

                div_12 = tag_div.find_all("div", class_="highlight-default notranslate")[11:12] # Find div by div from one tag
                for tag in div_12:
                    print(tag.get_text(),"\n")

                tag_p13 = tag_div.find_all(["p"])[16:17]
                print()
                for i in tag_p13:
                    print(i.get_text(),"\n")

                return css_selectors

            the_name_arg()
            the_kword_args()
            searchcss_cls()
            string_argument()
            limit_argument()
            recursive_argument()
            call_tag_like()
            find()
            find_parent()
            find_next_sibling()
            find_prev_sibling()
            find_all_next()
            find_all_prev()
            css_selectors()
            return find_all
        
        a_string()
        reg_expres()
        a_list()
        true()
        a_function()
        find_all()
        return Kinds_filters
    
    Kinds_filters()
    return search_tree


first()
tag_help()
quick_start()
instal_bfs()
problems_after()
install_parser()
making_soup() # daqui pra cima corrigir e melhorar
Kind_obj()
nav_tree()
search_tree()
