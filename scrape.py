import re
from selenium import webdriver # pip install selenium
import os

def main():

    i=1
    tag = input('Enter a category: ')
    
    while i < 51: #Disboard limits results to 50 pages 

        url = "https://disboard.org/servers/tag/" + tag + "/" + str(i)

        dr = webdriver.Chrome()
        dr.get(url)

        html = dr.page_source

        link = re.findall('<a href=\"/server/join/(.*?)\"',html)

        if len(andre) == 0:
            break

        f = open('PATH TO FILE', 'a') #Path to the output. For example: "C:\Users\Username\Desktop\Output.txt"
        for x in link:
            f.write("https://disboard.org/server/join/" + x + "\n")

        i+=1

    f.close()

main()
