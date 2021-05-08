import requests, colorama, sys, os
from bs4 import BeautifulSoup

def main():
    #input
    products = []
    inp = ""
    if len(sys.argv) > 1:
        for j in range(1, len(sys.argv)):
            inp += sys.argv[j]
            inp += " "
    else:
        inp = input("What do you want to search for?")

    #setting up beautifulsoup
    os.system("cls")
    url = 'https://www.alza.cz/search.htm?exps=' + inp.strip()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    #grid with products
    grid = soup.find(id='boxes')
    if grid is None:
        print("No results for %s"%inp)
        sys.exit()

    boxes = grid.find_all(name = "div", class_ = "box")

    #going through products
    for box in boxes:
        #top and bottom part of product
        top = box.find(name = 'div', class_='top')
        bottom = box.find(name = 'div', class_='bottom')

        #getting name and price of product
        name = top.find(name = 'a', text=True, href=True)    
        price = bottom.find(class_= "c2")

        #getting availabitlity
        avail = bottom.find('div', class_ = "avl")

        #setting variables
        namet = name.text
        pricet = ''
        link = 'https://www.alza.cz/' + name['href']
        tavailability = avail.find('span').text
        description = top.find('div', class_='Description').text.strip()

        #printing data
        print(namet)
        try:
            print(price.text)
            pricet = price.text
        except:
            print("No price data")
            pricet = "No price data"
        print(link)
        print(tavailability)
        print()

        #adding to list
        products.append({'name' : namet, 'price' : pricet, 'link' : link, 'availability' : tavailability, 'description' : description})


    #getting printable parts
    keys = ""
    if len(products) > 0:
        for item in products[0]:
            keys += item + " "


    #choosing output
    cont = True
    while cont:
        choices = input("What do you want to visit?\n%s\nE to exit\n"%(keys.strip())).split()
        os.system('cls')

        #printing selected info
        for product in products:
            for choice in choices:
                #exit
                if choice.lower() == 'e':
                    cont = False
                    break

                else:
                    try:
                        print(product[choice.lower()])
                    except:
                        print("No data of type %s"%choice)
            
            if not cont:
                break
            print()

if __name__ == "__main__":
    main()