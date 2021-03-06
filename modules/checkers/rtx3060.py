import requests, os, sys, time
from main import tools
from bs4 import BeautifulSoup

base_name = "GeForce RTX 3060" # GPU Name here, Example: GeForce RTX 3070 Ti
url = "https://www.evga.com/products/product.aspx?pn=12G-P5-3655-KR" # Site URL of the evga.com gpu page
price_element = "LFrame_spanFinalPrice" # Put the price element here, Example: LFrame_spanFinalPrice

def main():
    tools.clear()
    timedelay = int(input("Enter the time delay in seconds: "))
    tools.clear()
    tools.printCheckingTitle(base_name)
    print("Checking GPU on: https://www.evga.com/\n")

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    stock_info = soup.find(class_="message message-information") # The ID of the stock element

    if stock_info is None:
        tools.nogpustock(base_name)
    else:
        tools.hasgpustock(base_name)
        
    while True:
        price = soup.find(id=price_element).get_text() # The ID of the price element to grab 
        price = price.replace(' ', '') # removing all spaces

        tools.showGpuPrice(price)
        time.sleep(timedelay)