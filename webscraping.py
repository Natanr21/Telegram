from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

# Buscar as informações
nav = webdriver.Chrome()
action_chains = ActionChains(nav)

link = 'https://estrelabet.com/ptb/bet/main'

nav.get(link)

time.sleep(3)

click_cookies = nav.find_element(By.XPATH,'//*[@id="cookies-bottom-modal"]/div/div[1]/a')
action_chains.click(click_cookies).perform()
time.sleep(5)

brasileirao23 = nav.find_element(By.XPATH,'//*[@id="container-main-right"]/league-card/div/div[1]/div/a')
action_chains.click(brasileirao23).perform()
time.sleep(10)



#print()
#
#//*[@id="trader-estrelabet"]

#<span class="sgl-ParticipantOddsOnly80_Odds">2.40</span>
# Salvar em um dicionário

# Bot Telegram