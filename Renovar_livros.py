#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from twilio.rest import Client
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)



login = ['seu_login','seu_login']
senha = ['sua_senha','sua_senha']

for i in range(2):
    navegador.get(r'Site da universidade onde vai renovar os livros')
    navegador.find_element(By.ID,'id_login').send_keys(login[i]) 
    navegador.find_element(By.ID,'id_senhaLogin').send_keys(senha[i]) 
    navegador.find_element(By.ID,'button').click()

    #vamos descobrir a quantidade de livro que temos 
    renovar = len(navegador.find_elements(By.CLASS_NAME,'btn_renovar'))

    # vamos renovar a quantidade de livro que temos
    for i in range(renovar):
        navegador.find_element(By.XPATH,f'//*[@id="botao_renovar{i+1}"]/center/input').click()
        time.sleep(2)
        navegador.find_element(By.ID,'btn_gravar4').click()

    # vamos pegar os livros que temos 
    livros = []
    for i in range(renovar):
        livro = navegador.find_element(By.XPATH,f'//*[@id="Accordion1"]/div[1]/div[2]/table/tbody/tr[{i+2}]/td[2]/a').text
        livros.append(livro)
    
    #vamos pegar a data da próxima renovação
    data = navegador.find_element(By.XPATH,f'//*[@id="Accordion1"]/div[1]/div[2]/table/tbody/tr[2]/td[3]').text

    account_sid = 'sid'
    token = 'token'

    client = Client(account_sid, token)

    message = client.messages.create(
      to="seu número",
      from_="número do seu token",
     body=f"Seus livros {livros} foram renovados até {data}")
    
    print(message.sid)
    
navegador.close()


# In[ ]:




