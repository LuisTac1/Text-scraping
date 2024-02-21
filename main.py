import definitions
"""

"""

list = ["help", "quick_start", "instal_bfs", "problems_after", "install_parser", "making_soup", "Kind_obj", "nav_tree", "search_tree", "all"]

definitions.first()
print("*Choose a section to view the scrape*".upper(),"\n")

for i in list:
    print(i)
    print("-"*30)

get_cmd = input("Enter the command: ")

# To see one scraped text
def acv_one():
    if get_cmd == list[0]:
        definitions.tag_help()

    elif get_cmd == list[1]:
        definitions.quick_start()

    elif get_cmd == list[2]:
        definitions.instal_bfs()

    elif get_cmd == list[3]:
        definitions.problems_after()

    elif get_cmd == list[4]:
        definitions.install_parser()

    elif get_cmd == list[5]:
        definitions.making_soup()

    elif get_cmd == list[6]:
        definitions.Kind_obj()

    elif get_cmd == list[7]:
        definitions.nav_tree()

    elif get_cmd == list[8]:
        definitions.search_tree()
    return acv_one

# To see all scraped text
def acv_all():
    if get_cmd == "all":
        definitions.first()
        definitions.tag_help()
        definitions.quick_start()
        definitions.instal_bfs()
        definitions.problems_after()
        definitions.install_parser()
        definitions.making_soup() 
        definitions.Kind_obj()
        definitions.nav_tree()
        definitions.search_tree()

    return acv_all

acv_one()
acv_all()
