from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Buscar as informações
nav = webdriver.Chrome()

link = 'https://br.betano.com/'

nav.get(link)

time.sleep(1)

quit_ad = nav.find_elements_by_xpath('//*[@id="landing-page-modal"]/div/div[1]/button/svg').click()

#quit_ad.click()

time.sleep(15)

#print()



#<span class="sgl-ParticipantOddsOnly80_Odds">2.40</span>
# Salvar em um dicionário

# Bot Telegram