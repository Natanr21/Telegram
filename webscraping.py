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

time.sleep(5)

click_cookies = nav.find_element(By.XPATH,'//*[@id="cookies-bottom-modal"]/div/div[1]/a')
action_chains.click(click_cookies).perform()
time.sleep(5)

brasileirao23 = nav.find_element(By.XPATH,'//*[@id="container-main-right"]/league-card/div/div[1]/div/a')
action_chains.click(brasileirao23).perform()
time.sleep(5)

div_mae = nav.find_element(By.XPATH, '//*[@id="container-main"]/fixtures/div')

html_content = div_mae.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')

times = soup.find_all('span' , class_='bet-btn-text')
times_br = ['Empate','América-MG','Athletico-PR','Atlético-MG','Bahia','Botafogo','Corinthians','Coritiba','Cruzeiro','Cuiabá','Flamengo','Fluminense','Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Bragantino','Santos','São Paulo','Vasco da Gama']

for time in times:
  if(time == times_br[]):
    print(time.get_text())
  else:
    print("-----------------")

#print()
#
#//*[@id="trader-estrelabet"]

#<span class="sgl-ParticipantOddsOnly80_Odds">2.40</span>
# Salvar em um dicionário

# Bot Telegram