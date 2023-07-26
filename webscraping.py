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

time.sleep(15)

click_cookies = nav.find_element(By.XPATH,'//*[@id="cookies-bottom-modal"]/div/div[1]/a')
action_chains.click(click_cookies).perform()
time.sleep(5)

brasileirao23 = nav.find_element(By.XPATH,'//*[@id="container-main-right"]/league-card/div[2]/div[1]/div/a')
action_chains.click(brasileirao23).perform()
time.sleep(5)

div_mae = nav.find_element(By.XPATH, '//*[@id="container-main"]/fixtures/div')

html_content = div_mae.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')

times = soup.find_all('a' , class_='btn bet-btn waves-effect waves-light flex-item twoRow ng-star-inserted')
times_br = ['Empate','América MG','Athletico PR','Atlético MG','Bahia','Botafogo','Corinthians','Coritiba','Cruzeiro','Cuiabá','Flamengo','Fluminense','Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Bragantino','Santos','São Paulo','Vasco da Gama']
span_time = times.find_all('span')

if len(span_time) == 2:
    odds = span_time[0].text
    times = span_time[1].text

    print("Span 1:", odds)
    print("Span 2:", times)

else:
    print("Erro")

#odds = soup.find_all('span', class_='bet-btn-odd')
#odds_ok = []
#odds_br = 



#for time in times:
 #   times_ext = time.get_text()
  #  for team in times_br:
   #     if team == times_ext:
    #        timesbr23.append(times_ext)
        
     #   else:
      #      continue

#print(timesbr23)

#for odd in odds:
    #odds_ext = odd.get_text()
    #for time in times_br:

    # usar comparação lógica com números